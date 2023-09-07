from flask import Flask, jsonify
from chatbot import chatbot_responde, chat

app = Flask(__name__)

@app.route('/chatbot/<string:interacao>', methods=['GET'])
def responde_chatbot(interacao):
    resposta = chatbot_responde(chat, interacao)
    return jsonify({"resposta": resposta})

if __name__ == '__main__':
    app.run(debug=True, port=5500)
