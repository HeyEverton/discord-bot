import discord
import responses
import commands

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_responses(user_message, message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(f"EXCEPTION IN SEND MESSAGES: {e}")
        
async def send_commands(message, user_message):
    try:
        if message.author == 'deskimon':
            print(message.author)
            print('----------------17 ')
            print('sou eu que enviou a mensagem')
        else: 
            print(message.author)
            print('----------------21 ')
            print('não foi eu que enviou a mensagem')
        response = commands.handle_commands(user_message, message)
        await message.channel.send(response)
        # else:
        #     await message.channel.send('Desculpe! eu só posso responder ao usuário `deskimode`')
    except Exception as e:
        print(f"EXCEPTION IN HANDLE COMMANDS: {e}")
        
def run_discord_bot():
    token = 'MTE0NDQ1MzcxNjIxNzQ0MjQwNQ.GKZDid.a8qJH-Nbb5fodOIjax9IokKCiS2hCS54UCTDjo'
    
    intents = discord.Intents.default()
    intents.message_content = True  
    
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} agora está rodando!')
        
        
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
    
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        if '?' in user_message[0]:
            await send_commands(message, user_message)
        
        print('--------------55')
        print(f"{username} disse: '{user_message}' em ({channel})")
        
        # if user_message[0] == '?':
        #     user_message = user_message[1:]
        #     await send_message(message, user_message, is_private=True)
        # else:
        # await send_message(message, user_message, is_private=False)

        
    client.run(token)