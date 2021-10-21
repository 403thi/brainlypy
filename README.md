# brainlypy
Library to scrape brainly.com graphql API. 

## Requirements
+ Python >= 3.6

## Install
Install via pip on terminal
```
pip install brainlypy
```

## Simple use [EN]
```python
import brainlypy
brainlypy.set_lang('us')
# "pt" to portuguese, "us" to english, "es" to spanish, "id" to indonesian.
# default is 'us'
results = brainlypy.search('value of x')
question = results.questions[0]
print('URL: '+'https://brainly.com/task/'+str(question.databaseid))
print('QUESTION:',question)
print('ANSWER 1:', question.answers[0])
if question.answers_count == 2:
    print('ANSWER 2:', question.answers[1])
# output is:
'''
URL: https://brainly.com/question/24550771
QUESTION: Plz help will Mark brainlest!!

A. As x decreases in value, f(x) increases in value. As x increases in value, f(x) decreases in value.
[ reduced to not take up too much space ]
D. As x decreases in value, f(x) decreases in value. As x increases in value, f(x) increases in value.

ANSWER 1: Answer:
A
Step-by-step explanation:
Well considering how the graph looks, from the x-axis(0,0), the line(x) moves upwards on the left before itf(x) moves downwards on the right
'''
```

## Uso simples [PT]
```python
import brainlypy
brainlypy.set_lang('pt')
# "pt" para português, "us" para inglês, "es" para espanhol, "id" para indonésio.
# o padrão é 'us' (inglês)
results = brainlypy.search('valor de x')
question = results.questions[0]
print('URL: '+'https://brainly.com.br/tarefa/'+str(question.databaseid))
print('QUESTÃO:',question)
print('RESPOSTA 1:', question.answers[0])
if question.answers_count == 2:
    print('RESPOSTA 2:', question.answers[1])
# SAÍDA:
'''
URL: https://brainly.com.br/tarefa/5430425
QUESTÃO: Número primo x número primo = 21
Número primo x número primo = 34
Descubra A e B.

RESPOSTA 1: resposta
a)3×7=21
b)2×17=34


RESPOSTA 2: Resposta:
a- 3×7=21
b-2×17=34
'''
```
# [More exemples / Mais exemplos](https://github.com/thiagopyy/brainlypy/tree/main/examples)
