import json, re
from urllib.parse import unquote
from requests import get, post
from bs4 import BeautifulSoup
from .exceptions import *
from html import unescape
'''
MIT License

Copyright (c) 2021 thiagopyy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
HEADERS = {'User-Agent':'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}

GRAPHQL_URLS = {
    'pt':'https://brainly.com.br/graphql/pt',
    'us':'https://brainly.com/graphql/us',
    'es':'https://brainly.lat/graphql/es',
    'id':'https://brainly.co.id/graphql/id'
}

TAGS = re.compile(r'<[^>]+>')

lang = 'us'
def set_lang(language='us'):
    global lang
    if language not in GRAPHQL_URLS:
        raise LangException
    else:
        lang = language
    return None

def search(query, first:int=1):
    after = None
    BODY = {'operationName': 'SearchQuery', 'variables': {'query': query, 'after': after, 'first': first}, 'query': 'query SearchQuery($query: String!, $first: Int!, $after: ID) {\nquestionSearch(query: $query, first: $first, after: $after) {edges {node{\n\t\tdatabaseId\n\t\tauthor{\n\t\t\tnick\n\t\t\tdatabaseId}\ncontent\ncanComment\ncontent\npoints\ncreated\nlastActivity\nisClosed\nisAuthorsFirstQuestion\ncanBeAnswered\nattachments{url}\npointsForAnswer\npointsForBestAnswer\neduLevel\nanswers{nodes{content\nauthor{nick\ndatabaseId}\npoints\nisConfirmed\nisBest\nrating\nratesCount\nthanksCount\ncreated\nattachments{url}}}}}}}'}
    response = post(url=GRAPHQL_URLS[lang], headers=HEADERS, json=BODY)
    json = response.json()
    return Results(json, first)

def format_html(html):
    html = html.replace('\n','')
    try:
        html = html.replace('<br />','\n')
        html = html.replace('</p><p>', '\n')
    except: pass
    finally:
        html = unescape(html)
        html = TAGS.sub('', html)
        return html

class Results():
    def __init__(self, json, first):
        self.questions = []
        for c in range(0, first):
            self.questions.append(Question(json, c))

class Question():
    def __init__(self, json, index) -> None:
        if json == {'data': {'questionSearch': {'edges': []}}}:
            raise NoResults()
        try: source = json['data']['questionSearch']['edges'][index]['node']
        except: return
        answers_source = source['answers']['nodes']
        c = 0
        self.content = format_html(source['content'])
        self.databaseid = source['databaseId']
        self.author = {
            'nick':source['author']['nick'],
            'databaseId':source['author']['databaseId']
        }
        try: self.attachments = source['attachments'][0]
        except: self.attachments = source['attachments']
        self.can_be_answered = source['canBeAnswered']
        self.is_authors_first_question = source['isAuthorsFirstQuestion']
        self.can_comment = source['canComment']
        self.is_closed = source['isClosed']
        self.points = source['points']
        self.created = source['created']
        self.last_activity = source['lastActivity']
        self.points_for_answer = source['pointsForAnswer']
        self.points_for_best_answer = source['pointsForBestAnswer']
        self.edu_level = source['eduLevel']
        self.answers_count = len(answers_source)
        self.answers = []
        for i in answers_source:
            self.answers.append(Answer(answers_source[c]))
            c += 1
    def __str__(self) -> str:
        return self.content

class Answer():
    def __init__(self, json) -> None:
        import json as j
        self.content = format_html(json['content'])
        try: 
            self.author = json['author']['nick']
            self.author_databaseid = json['author']['databaseId']
        except: 
            try: 
                self.author = json['author']
            except:
                self.author = None
            finally:
                self.author_databaseid = None
        self.is_confirmed = json['isConfirmed']
        self.is_best = json['isBest']
        self.thanks_count = json['thanksCount']
        self.rating = json['rating']
        self.rates_count = json['ratesCount']
        try: self.attachments = json['attachments'][0]
        except: self.attachments = json['attachments']
    def __str__(self) -> str:
        return self.content
