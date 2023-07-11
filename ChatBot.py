from nltk.chat.util import Chat

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

# pairs_pt = [
#     [
#      r'oi|olá|opa',
#      ['olá', 'como vai?', 'tudo bem?']
#     ],
#     [
#      r'qual é o seu nome?',
#      ['Meu nome é Chat e eu sou um chatbot']
#     ],  
#     [
#      r'(.*) idade?',
#      ['Não tenho idade pois sou um chatbot']
#     ], 
#     [
#      r'meu nome é (.*)',
#      ['Olá %1, como você está hoje?']
#     ],  
#     [
#      r'eu trabalho na empresa (.*)',
#      ['Eu conheço a empresa %1']
#     ], 
#     [
#      r'(.*) (cidade|país)',
#      ['Porto União, Brasil']
#     ], 
#     [
#      r'quit',
#      ['Até breve', 'Foi bom conversar com você. Até breve!']
#     ]     
# ]



class ChatBot(Chat):

    def __init__(self,nome, pairs, reflections= reflections_pt):
        super().__init__(pairs, reflections)
        self._nome = nome



class Pairs():
    
    def __init__(self, nome = None):
        self._nome = nome
        self.pairs = []
        self.adiconar_conversa('sair', 'Até breve')
    
    def adiconar_conversa(self, pergunta, resposta): 
        self.pairs.append(self._criar_conversa(pergunta, resposta))

    def _criar_conversa(self, _pergunta, _resposta):
        return [r''.join(_pergunta), _resposta]
    
    def retorna_pairs(self):
        return self.pairs
    

if __name__ == '__main__':
    pairs_teste = Pairs('Teste')
    pairs_teste.adiconar_conversa('Olá', 'Bem-vindo! Em que posso ti ajudar?')
    
    chat = ChatBot('Teste', pairs_teste.retorna_pairs())