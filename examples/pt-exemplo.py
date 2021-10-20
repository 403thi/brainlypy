
import brainlypy

brainlypy.set_lang('pt')

def obter_variaveis_do_obj():
    results = brainlypy.search('valor de x') # pesquisa a pergunta : retorna um objeto 'Results'
    print(dir(results))
    # results object
    # ['questions']
    print(dir(results.questions[0]))
    # question object
    # ['answers', 'answers_count', 'attachments', 'author', 'can_be_answered', 'can_comment', 'content', 'created', 'databaseid', 'edu_level', 'is_authors_first_question', 'is_closed', 'last_activity', 'points', 'points_for_answer', 'points_for_best_answer']
    print(dir(results.questions[0].answers[0]))
    # answer object
    # ['attachments', 'author', 'author_databaseid', 'content', 'is_best', 'is_confirmed', 'rates_count', 'rating', 'thanks_count']

def exemplo_completo():
    results = brainlypy.search(query='descubra o valor de x', first=2) # o paramêtro 'first' é para indicar a quantidade de respostas esperadas. Padrão: 1
    for questao in results.questions:
        print(questao)
        print(f'QUESTÃO: {questao.content}')
        print(f'ANEXOS: {questao.attachments}')
        c = 1
        for a in questao.answers:
            print(f'RESPOSTA {c}')
            print(f'AUTHOR: {a.author}')
            print(f'CONTEUDO: {a.content}')
            print(f'AVALIAÇÃO: {a.rating} (VOTOS: {a.rates_count})')
            print(f'QUANTIDADE DE "OBRIGADOS": {a.thanks_count}')
            print(f'É A MELHOR RESPOSTA? {a.is_best}')
            print(f'É UMA RESPOSTA CONFIRMADA? {a.is_confirmed}')
            print(f'ANEXOS: {a.attachments}')
            c += 1

obter_variaveis_do_obj()
exemplo_completo()
