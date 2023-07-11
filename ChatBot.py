from nltk.chat.util import Chat
import os

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


class ChatBot(Chat):

    def __init__(self,nome, pairs, reflections= reflections_pt):
        super().__init__(pairs, reflections)
        self._nome = nome
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value



class Pairs():
    
    def __init__(self, nome = None, pairs = []):
        self._nome = nome
        self._pairs = pairs
        self.adiconar_conversa('sair', 'Até breve')
    
    def adiconar_conversa(self, pergunta, resposta): 
        self._pairs.append(self._criar_conversa(pergunta, resposta))

    def _criar_conversa(self, _pergunta, _resposta):
        return [r''.join(_pergunta), _resposta]
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value
    
    @property
    def pairs(self):
        return self._pairs
    

if __name__ == '__main__':
    os.system('cls')

    pairs_teste = Pairs('Teste')
    pairs_teste.adiconar_conversa('Olá', 'Bem-vindo! Em que posso ti ajudar?')
    print(pairs_teste.pairs)
    
    chat = ChatBot('Teste', pairs_teste.pairs)

    print(chat.nome)
    
    chat.nome = 'Teste_2'
    print(chat.nome)