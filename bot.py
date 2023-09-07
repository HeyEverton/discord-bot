import discord
from discord.ext import commands
import responses
from datetime import datetime
import random

intents = discord.Intents.default()
intents.message_content = True
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
client = commands.Bot(command_prefix='?', intents=intents)


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_responses(user_message, message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    token = ''

    @client.event
    async def on_ready():
        print('-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f"{client.user} agora está rodando: {current_time}")
        print('-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Desculpe, esse comando não foi reconhecido. Digite `?comandos` para ver a lista de comandos disponíveis.")
        else:
            print(error)
    # @client.event
    # async def on_message(message):
    #     if message.author == client.user:
    #         return

    #     username = str(message.author)
    #     user_message = str(message.content)
    #     channel = str(message.channel)
    #     # print('-----------------------')
    #     print(f"{username} disse: '{user_message}' em ({channel})")

    #     await send_message(message, user_message, is_private=False)

    @client.command()
    async def oi(ctx):
        print(f'{ctx.author} ')
        await ctx.send(f'Olá {ctx.author}! quer saber meus comandos? digite `?comandos`')

    @client.command()
    async def comandos(ctx):
        description_embed = "vou ganhar consciência..."
        embed = discord.Embed(
            title=f'Olá {ctx.author}! Eu sou um bot de filosofias e tenho alguns **comandos**!',
            description=description_embed,
            colour=discord.Colour.purple(),
        )
        embed.set_author(
            name='Bot do Hamlet',
            icon_url='https://i.imgur.com/Fr4rWRC.jpg'
        )
        embed.set_thumbnail(url="https://i.imgur.com/8MsmjyF.gif")

        embed.add_field(
            name="`?criador`",
            value="Este é o comando para ver as informações do meu **criador**! ",
            inline=False
        )
        embed.add_field(
            name="`?filmes`",
            value='Este é o comando para ver a lista de filmes que o Hamlet já assistiu em [LIVE](https://www.twitch.tv/hamletarl) !',
            inline=False
        )
        embed.add_field(
            name="`?regras`",
            value='Veja as regras do servidor!',
            inline=False
        )
        embed.add_field(
            name="`?livros`",
            value='Confira recomendações de bons livros que o Hamlet dá!',
            inline=False
        )
        embed.add_field(
            name="`?oi`",
            value='O comando para um saudoso oi!',
            inline=False
        )

        embed.add_field(
            name="`?comandos`",
            value='Este é o comando para ver a lista de comandos que eu consigo executar!',
            inline=False
        )
        embed.add_field(
            name="`?sugestao`",
            value='Tem alguma sugestão de comando para o bot?',
            inline=False
        )

        embed.add_field(
            name='`?ajuda`',
            value='Comando para ajuda',
            inline=False
        )
        await ctx.send(embed=embed)

    @client.command()
    async def criador(ctx):
        description_embed = "Para mais informações, por favor visite o [o meu Github](https://github.com/HeyEverton)"
        embed = discord.Embed(
            title='Sou eu! o garoto de programas!',
            description=description_embed,
            colour=discord.Colour.red(),
        )

        embed.set_author(
            name='daskimode',
            icon_url='https://i.imgur.com/nB28sLG.jpg'
        )

        embed.set_thumbnail(url="https://i.imgur.com/8MsmjyF.gif")
        await ctx.send(embed=embed)

    @client.command()
    async def filmes(ctx):
        await ctx.send('Para ver todos os filmes que o Hamlet já viu, acesse a [Lista de Filmes](https://letterboxd.com/hamletarl/)')

    @client.command()
    async def ajuda(ctx):
        await ctx.send('Precisa de alguma ajuda no nosso servidor do discord? Contate algum moderador!')

    @client.command()
    async def regras(ctx):
        await ctx.send('Não sabe as regras? Veja o canal <#1143041155773255700> ')

    @client.command()
    async def sugestao(ctx):
        await ctx.send('Abra uma [Issue](https://github.com/HeyEverton/discord-bot/issues/new) no repositório do bot!')

    @client.command()
    async def recomenda(ctx):
        await ctx.send('Hmm... Estou pensando... 🤔')
        books = [
            {
                'book_author': 'Sêneca',
                'books': [
                    {
                        'book_name': 'Sobre a brevidade da Vida.',
                        'short_description': 'xxxxxx',
                        'cover_image': 'https://http2.mlstatic.com/D_NQ_NP_782373-MLU50457184108_062022-O.webp',
                        'famous_phrases': [
                            {'phrase': 'Sofremos mais na imaginação do que na realidade.'},
                            {'phrase': 'A vida é breve, mas cabe nela muito mais do que somos capazes de viver.'},
                        ]
                    },
                    {
                        'book_name': 'Cartas a Lucílio',
                        'short_description': 'yyyyy',
                        'cover_image': 'https://http2.mlstatic.com/D_NQ_NP_782373-MLU50457184108_062022-O.webp',
                        'famous_phrases': [
                            {'phrase': 'Sofremos mais na imaginação do que na realidade.'},
                            {'phrase': 'A vida é breve, mas cabe nela muito mais do que somos capazes de viver.'},
                        ]
                    },
                    {
                        'book_name': 'Diálogos',
                        'short_description': 'zzzzz',
                        'cover_image': 'https://example.com/cover3.jpg',
                        'famous_phrases': [
                            {'phrase': 'Não existe vento favorável para quem não sabe para onde vai.'},
                            {'phrase': 'Aprender sem pensar é tempo perdido.'},
                        ]
                    },
                    {
                        'book_name': 'A Ira',
                        'short_description': 'wwwww',
                        'cover_image': 'https://example.com/cover4.jpg',
                        'famous_phrases': [
                            {'phrase': 'A ira é breve loucura.'},
                            {'phrase': 'Quem não perdoa, destrói a ponte sobre a qual ele próprio deve passar.'},
                        ]
                    },
                ]
            },
            {
                'book_author': 'Platão',
                'books': [
                    {
                        'book_name': 'A República',
                        'short_description': 'qqqqq',
                        'cover_image': 'https://example.com/cover5.jpg',
                        'famous_phrases': [
                            {'phrase': 'O homem é a medida de todas as coisas.'},
                            {'phrase': 'A democracia é a pior forma de governo, exceto todas as outras.'},
                        ]
                    },
                    {
                        'book_name': 'Fedro',
                        'short_description': 'ppppp',
                        'cover_image': 'https://example.com/cover6.jpg',
                        'famous_phrases': [
                            {'phrase': 'A verdade é bela, sem dúvida; mas tão difícil de conseguir que a falsidade é muitas vezes preferível.'},
                            {'phrase': 'O amor é um desejo inato de procriar, tanto na alma como no corpo.'},
                        ]
                    },
                    {
                        'book_name': 'Mênon',
                        'short_description': 'ooooo',
                        'cover_image': 'https://example.com/cover7.jpg',
                        'famous_phrases': [
                            {'phrase': 'Nada mais do que um homem pode se esquecer com mais facilidade do que sua própria ignorância.'},
                            {'phrase': 'O homem sábio fala porque tem algo a dizer; o tolo, porque tem que dizer alguma coisa.'},
                        ]
                    },
                ]
            },
            {
                'book_author': 'Aristóteles',
                'books': [
                    {
                        'book_name': 'Ética a Nicômaco',
                        'short_description': 'nnnnn',
                        'cover_image': 'https://example.com/cover8.jpg',
                        'famous_phrases': [
                            {'phrase': 'O homem é por natureza um animal político.'},
                            {'phrase': 'A amizade é um bem de grande valor.'},
                        ]
                    },
                    {
                        'book_name': 'Política',
                        'short_description': 'mmmmm',
                        'cover_image': 'https://example.com/cover9.jpg',
                        'famous_phrases': [
                            {'phrase': 'A virtude está no meio.'},
                            {'phrase': 'A cidade é composta por almas, não edifícios.'},
                        ]
                    },
                    {
                        'book_name': 'Poética',
                        'short_description': 'lllll',
                        'cover_image': 'https://example.com/cover10.jpg',
                        'famous_phrases': [
                            {'phrase': 'A tragédia é uma representação de uma ação elevada e completa.'},
                            {'phrase': 'A poesia é algo mais filosófico e sério do que a história.'},
                        ]
                    },
                ]
            },
            {
                'book_author': 'Epicuro',
                'books': [
                    {
                        'book_name': 'Carta sobre a Felicidade',
                        'short_description': 'kkkkk',
                        'cover_image': 'https://example.com/cover11.jpg',
                        'famous_phrases': [
                            {'phrase': 'Não é o jovem mais forte nem o homem que não sente dor que é feliz, mas sim o homem que sabe ser feliz.'},
                            {'phrase': 'A supressão do desejo é a eliminação da dor.'},
                        ]
                    },
                    {
                        'book_name': 'A Doutrina Secreta',
                        'short_description': 'jjjjj',
                        'cover_image': 'https://example.com/cover12.jpg',
                        'famous_phrases': [
                            {'phrase': 'A morte não é nada para nós, pois, quando existimos, a morte não existe, e quando a morte existe, não existimos mais.'},
                            {'phrase': 'Não procurem na busca da felicidade a realização dos desejos do corpo, mas sim a eliminação deles.'},
                        ]
                    },
                    {
                        'book_name': 'A Máxima Felicidade',
                        'short_description': 'iiiii',
                        'cover_image': 'https://example.com/cover13.jpg',
                        'famous_phrases': [
                            {'phrase': 'Comer e beber sem moderação não nos dá alegria, mas provoca-nos tormento.'},
                            {'phrase': 'A sabedoria é a fonte da felicidade.'},
                        ]
                    },
                ]
            },
        ]
        await ctx.send('Já sei! acho que um bom livro é...')
        random.shuffle(books)
        for b in books:
            philosopher = b['book_author']
            random.shuffle(b['books'])
            random_book = b['books'][0]
            book_name = random_book['book_name']
            short_description = random_book['short_description']
            cover_image = random_book['cover_image']
            random.shuffle(random_book['famous_phrases'])
            famous_phrase = random_book['famous_phrases'][0]['phrase']

        embed = discord.Embed(
            title=book_name,
            description=short_description,
            colour=discord.Colour.purple(),
        )

        embed.set_author(
            name=philosopher,
            icon_url='https://i.imgur.com/8MsmjyF.gif'
        )

        embed.add_field(
            name=f"Uma frase famosa do livro {book_name}",
            value=famous_phrase,
            inline=False
        )

        embed.set_thumbnail(url=cover_image)

        await ctx.send(embed=embed)
        
    @client.command()
    async def aristoteles(ctx):
        phrases = [
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
        random.shuffle(phrases)
        await ctx.send(f"O filósofo Aristóteles uma vez disse: {phrases[0]['phrase']}")
    
    @client.command()
    async def livros(ctx):
        await ctx.send('Veja recomendações de livros que o próprio Hamlet recomenda! no canal <#1146669066870853742>')
    client.run(token)
