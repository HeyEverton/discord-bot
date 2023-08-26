import random

def handle_responses(content_message, user_message_content)-> str:
    p_message = content_message.lower()
    if user_message_content.author == 'deskimon':
        print('sou eu mesmo que enviei a mensagem')
        
    # print('-----------------')
    # print(user_message_content)
    _word = 'bot do hamlet'
    if _word in p_message:
        return 'Quem me invoca? quer uma recomendação de livro? use `?recomenda`'
    
    if p_message == '?recomenda' :
        livros = [
            'Sobre a Brevidade da Vida, de Sêneca',
            'A República, de Platão',
            'O Banquete, de Platão',
            'Retórica, de Aristoteles',
            'Hamlet, de William Shakespeare',
        ]
        return livros[0]
    
    # if p_message == 'roll':
    #     return str(f'{random.randrange(1, 6)} Usuários deste servidor são filosofinhos... 🤖')
    
    if p_message == '?obrigado':
        return "eu sabo muito! "
    
    philosophers = [
        {   
            'real_name': 'Aristóteles',
            'command_name': '?aristoteles',
            'accent_name': '?aristóteles',
            'phrases': [
                {'phrase': 'Só sei que nada sei.'},
                {'phrase': 'O homem é, por natureza, um animal político.'},
                {'phrase': 'O sábio nunca diz tudo o que pensa, mas pensa tudo o que diz.'},
                {'phrase': 'O prazer no trabalho aperfeiçoa a obra.'},
                {'phrase': 'O ignorante afirma, o sábio duvida, o sensato reflete.'},
                {'phrase': 'Ter muitos amigos é não ter nenhum.'},
                {'phrase': 'É fazendo que se aprende a fazer aquilo que se deve aprender a fazer.'},
                {'phrase': 'A educação tem raízes amargas, mas os seus frutos são doces.'},
                {'phrase': 'Nós somos aquilo que fazemos repetidamente. Excelência então não é um modo de agir, mas um hábito.'},
                {'phrase': 'Nosso caráter é o resultado da nossa conduta.'},
                {'phrase': 'As pessoas dividem-se entre aquelas que poupam como se vivessem para sempre e aquelas que gastam como se fossem morrer amanhã.'},
            ]
        },
        {
            'real_name': 'Platão',
            'command_name': '?platao',
            'accent_name': '?platão',
            'phrases': [
                {'phrase': 'A democracia sofre quando não educados.'},
                {'phrase': 'A pena que os bons sofrem é assistir à injustiça.'},
                {'phrase': 'Tente mover o mundo - o primeiro passo será mover a si mesmo.'},
                {'phrase': 'De todos os animais selvagens, o homem jovem é o mais difícil de domar.'},
                {'phrase': 'Onde não há igualdade, a amizade não perdura.'},
                {'phrase': 'Tudo quanto vive provém daquilo que morreu.'},
                {'phrase': 'Opinião é o meio entre conhecimento e ignorância.'},
                {'phrase': 'Coragem é saber o que não temer.'},
                {'phrase': 'O sábio fala porque tem alguma coisa a dizer; o tolo porque tem que dizer alguma coisa.'},
                {'phrase': 'Quem é capaz de ver o todo é filosofo; quem não, não.'},
                {'phrase': 'O livro é um mestre que fala mas que não responde.'},
            ]
        },
        {
            'real_name': 'Sêneca',
            'command_name': '?seneca',
            'accent_name': '?sêneca',
            'phrases': [
                {'phrase': 'Toda crueldade surge de uma fraqueza.'},
                {'phrase': 'Sofremos mais na imaginação do que na realidade.'},
                {'phrase': 'Se a pessoa não sabe para qual porto está navegando, não há vento favorável.'},
                {'phrase': 'Nada é mais honrado do que um coração agradecido.'},
                {'phrase': 'Enquanto estamos adiando, a vida passa rapidamente.'},
                {'phrase': 'É melhor vencer nossa dor do que enganá-la.'},
                {'phrase': 'O tempo cura o que a razão não consegue.'},
                {'phrase': 'Coisas que eram difíceis de suportar são doces de lembrar.'},
                {'phrase': 'Nós aprendemos não na escola, mas na vida.'},
            ]
        },
        {
        'real_name': 'Hamlet',
        'command_name': '?hamlet',
        'accent_name': '',
        'phrases': [
            {'phrase': 'Ser ou não ser, eis a questão.'},
            {'phrase': 'Faça o pix, se não, faça o L! https://tipa.ai/hamletarl'}
        ]
        },
        {
            'real_name': 'Sócrates',
            'command_name': '?socrates',
            'accent_name': '?sócrates',
            'phrases': [
                {'phrase': 'Ser ou não ser, eis a questão.'},
                {'phrase': 'Faça o pix, se não, faça o L! https://tipa.ai/hamletarl'}
            ]
        },
    ]
    for p in philosophers: 
        if p_message == p['command_name']:
            random.shuffle(p['phrases'])
            return f"O filósofo {p['real_name']} uma vez disse: {p['phrases'][0]['phrase']}"
        elif p_message == p['accent_name']:
            return f"O filósofo {p['real_name']} uma vez disse: {p['phrases'][0]['phrase']}"
            
        
    if p_message == '?ajuda':
        return "`Precisa de ajuda com algo? contate nossos moderadores!`"
    
    if p_message == '?filmes':
        return 'Confira a lista de filmes que o Hamlet já assistiu em LIVE! https://letterboxd.com/hamletarl/'
    
    _good_night = 'boa noite'
    if _good_night in p_message:
        return 'Boa noite! vamos filosofar mais outra vez!'
    