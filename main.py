from nltk.chat.util import Chat
from fastapi import FastAPI

# import nltk
# nltk.download()

reflections_pt = {'eu': 'você',
                  'eu sou': 'você é',
                  'eu era': 'você era',
                  "eu iria": 'você iria',
                  "eu irei": 'você irá',
                  'meu': 'seu',
                  'você': 'eu',
                  'você é': 'eu sou',
                  'você era': 'eu era',
                  "você irá": 'eu irei',
                  'seu': 'meu'}

pairs = [
    [r'ola', ['Bem-vindo! Qual o seu nome?']],
    [r'Meu nome é (.*)', ['Olá %1 ! Em que posso ti ajudar?', ]],
]

def chatbot_responde(chat, interacao):
    if interacao == 'sair':
        return 'Até breve!'
    
    resposta = chat.respond(interacao)
    
    if resposta is None:
        return 'Desculpa! Não entendi a sua pergunta!'
    else:
        return resposta

chat = Chat(pairs, reflections_pt)

app = FastAPI()

@app.get("/teste/{interacao}")
async def receber_string(interacao: str):
    return {"message": f"Você enviou a string: {interacao}"}

@app.get('/chatbot/{interacao}')
async def responde_chatbot(interacao: str):
    resposta = chatbot_responde(Chat(pairs, reflections_pt), interacao)
    return {'message': f'{resposta}'}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8050)