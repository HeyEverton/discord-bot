import discord
from discord.ext import commands
import responses
from datetime import datetime
import random

intents = discord.Intents.default()
intents.message_content = True  
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
client = commands.Bot(command_prefix = '?', intents=intents)

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_responses(user_message, message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        



def run_discord_bot():
    token = 'xxxxxxxxxxx'
    
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
            title = f'Olá {ctx.author}! Eu sou um bot em desenvolvimento e tenho alguns **comandos**!',
            description = description_embed,
            colour = discord.Colour.purple(),
        )
        embed.set_author(
            name = 'Bot do Hamlet',
            icon_url = 'https://i.imgur.com/Fr4rWRC.jpg'
        )
        embed.set_thumbnail(url="https://i.imgur.com/8MsmjyF.gif")

        embed.add_field(
            name = "`?criador`",
            value = "Este é o comando para ver as informações do meu **criador**! ",
            inline = False
        )
        embed.add_field(
            name = "`?filmes`",
            value = 'Este é o comando para ver a lista de filmes que o Hamlet já assistiu em [LIVE](https://www.twitch.tv/hamletarl) !',
            inline = False
        )
        embed.add_field(
            name = "`?regras`",
            value = 'Veja as regras do servidor!',
            inline = False
        )
        embed.add_field(
            name = "`?oi`",
            value = 'O comando para um saudoso oi!',
            inline = False
        )
        
        embed.add_field(
            name = "`?comandos`",
            value = 'Este é o comando para ver a lista de comandos que eu consigo executar!',
            inline = False
        )
        embed.add_field(
            name = "`?sugestao`",
            value = 'Tem alguma sugestão de comando para o bot?',
            inline = False
        )
        
        embed.add_field(
            name = '`?ajuda`',
            value = 'Comando para ajuda',
            inline = False
        )
        await ctx.send(embed = embed)
        
    @client.command()
    async def criador(ctx):
        
        description_embed = "Para mais informações, por favor visite o [o meu Github](https://github.com/HeyEverton)" 
        embed = discord.Embed(
            title = 'Sou eu! o garoto de programas!',
            description = description_embed,
            colour = discord.Colour.red(),
        )
        
        embed.set_author(
            name = 'daskimode',
            icon_url = 'https://i.imgur.com/nB28sLG.jpg'
        )
        
        embed.set_thumbnail(url="https://i.imgur.com/8MsmjyF.gif")
        await ctx.send(embed = embed)
        
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
                        { 'phrase': 'Sofremos mais na imaginação do que na realidade.' },
                        { 'phrase': 'A vida é breve, mas cabe nela muito mais do que somos capazes de viver.' },
                    ]
                },
                {
                    'book_name': 'xxxxxseneca',
                    'short_description': 'yyyyy',
                    'cover_image': 'https://http2.mlstatic.com/D_NQ_NP_782373-MLU50457184108_062022-O.webp',
                    'famous_phrases': [
                        { 'phrase': 'Sofremos mais na imaginação do que na realidade.' },
                        { 'phrase': 'A vida é breve, mas cabe nela muito mais do que somos capazes de viver.' },
                    ]
                },
            ],
            
        },
        {   
            'book_author': 'Platão',
            'books': [
                {
                    'book_name': 'A República',
                    'short_description': 'xxxxxx',
                    'cover_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs8KboHnyFMzX2-Dqlrpc0btSfC9hp0OZhoA&usqp=CAU',
                    'famous_phrases': [
                        { 'phrase': 'platao frase 1' },
                        { 'phrase': 'platao frase 2' },
                    ]
                },
            ],
            
        },
        
        
            # 'O Banquete, de Platão',
            # 'Retórica, de Aristoteles',
            # 'Hamlet, de William Shakespeare',
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
            title = book_name,
            description = short_description,
            colour = discord.Colour.purple(),
        )
        
        embed.set_author(
            name = philosopher,
            icon_url = 'https://i.imgur.com/8MsmjyF.gif'
        )
        
        embed.add_field(
            name = f"Uma frase famosa do livro {book_name}",
            value = famous_phrase,
            inline = False
        )
        
        embed.set_thumbnail(url = cover_image)

        
        await ctx.send(embed = embed)


    client.run(token)