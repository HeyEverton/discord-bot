import random

def handle_responses(message)-> str:
    p_message = message.lower()
    
    if p_message == 'oi bot do hamlet':
        return 'Oi! tudo bem? filosofias...'
    
    if p_message == 'roll':
        return str(f'{random.randrange(1, 6)} Usuários deste servidor são filosofinhos... 🤖')
    
    if p_message == 'gostou hamlet?':
        return "`Sou um robô bip bop 🤖`"
    
    if p_message == '!ajuda':
        return "`Está é uma mensagem de ajuda`"
    
    