import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        
        
        
def run_discord_bot():
    token = 'MTE0NDQ1MzcxNjIxNzQ0MjQwNQ.GrxywK.-w3CVH6Hjsls7tT0yycivh3h7r9b0Km8XSWsWo'
    
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
        print(user_message[0])
        print('-------------------------')
        print(f"{username} disse: '{user_message}' ({channel})")
        
        # if user_message[0] == '?':
        #     user_message = user_message[1:]
        #     await send_message(message, user_message, is_private=True)
        # else:
        await send_message(message, user_message, is_private=False)

        
    client.run(token)