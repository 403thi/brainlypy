import brainlypy

brainlypy.set_lang('us') # the default lang is english (us brainly), so you don't even need to use the function.

def get_obj_variables():
    results = brainlypy.search('value of x') # search question : return 'Results' object
    print(dir(results))
    # results object
    # ['questions']
    print(dir(results.questions[0]))
    # question object
    # ['answers', 'answers_count', 'attachments', 'author', 'can_be_answered', 'can_comment', 'content', 'created', 'databaseid', 'edu_level', 'is_authors_first_question', 'is_closed', 'last_activity', 'points', 'points_for_answer', 'points_for_best_answer']
    print(dir(results.questions[0].answers[0]))
    # answer object
    # ['attachments', 'author', 'author_databaseid', 'content', 'is_best', 'is_confirmed', 'rates_count', 'rating', 'thanks_count']

def full_example():
    results = brainlypy.search(query='value of x', first=2) # 'first' parameter is to indicate the amount of expected results. Default: 1
    for question in results.questions:
        print(question)
        print(f'QUESTION: {question.content}')
        print(f'ATTACHMENTS: {question.attachments}')
        c = 1
        for a in question.answers:
            print(f'ANSWER {c}')
            print(f'AUTHOR: {a.author}')
            print(f'CONTENT: {a.content}')
            print(f'RATING: {a.rating} (VOTES: {a.rates_count})')
            print(f'THANKS COUNT: {a.thanks_count}')
            print(f'IS BEST? {a.is_best}')
            print(f'IS CONFIRMED? {a.is_confirmed}')
            print(f'ATTACHMENTS: {a.attachments}')
            c += 1

get_obj_variables()
full_example()
