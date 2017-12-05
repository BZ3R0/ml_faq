# -*- coding: utf-8 -*-
from flask import Blueprint, request, current_app, render_template
from chatbot.lib.functions import Bot
from ..app import db
from ..model.aprendizado import Aprendizado
import traceback

mod_bot = Blueprint('mod_bot', __name__)


@mod_bot.route('/')
def home():
    '''
        Página inicial de apresentação
    '''
    return render_template('index.html')


@mod_bot.route('/verify', methods=['GET'])
def handle_verification():
    '''
        Valida token de acesso
    '''
    if request.args.get('hub.verify_token') == current_app.config['FB_VERIFY_TOKEN']:
        return request.args.get('hub.challenge'), 200
    return 'Erro ao verificar Token'


@mod_bot.route('/verify', methods=['POST'])
def handle_messages():
    '''
        Recebe mensagens enviadas pelo messenger
    '''
    try:
        # Requisição recebida pelo messenger, o corpo da mensagem
        data = request.json
        # Verifica se é a mensagem que o usuário enviou, ou se é outro tipo de requisição
        if ((len(data['entry']) > 0) and ('messaging' in data['entry'][0])):
            messaging_event = data['entry'][0]['messaging'][0]
            if 'message' in messaging_event and 'is_echo' not in messaging_event['message']:
                # ID do usuário que enviou a mensagem, para poder respondê-lo
                sender_id = messaging_event['sender']['id']
                # Texto que o usuário envia pelo messenger
                message = messaging_event['message']['text']
                # Obtén os dados do usuário
                user = Bot().get_profile(sender_id)
                # Tratar pergunta para responder
                aprendizado = Aprendizado.query.filter_by(active=True).first()
                if aprendizado:
                    aprendizado.answer = message
                    aprendizado.active = False
                    db.session.commit()
                    answer = 'Muito obrigado, aprendi uma coisa nova ;)'
                else:
                    aprendizado = Aprendizado.query.filter_by(question=message).first()
                    if aprendizado:
                        answer = aprendizado.answer
                    else:
                        answer = user['first_name'] + ', me desculpe, mas não sei a resposta para a sua pergunta, por favor me informe a reposta para poder aprender :)'
                        q = Aprendizado(message, None, True)
                        db.session.add(q)
                        db.session.commit()
                # Ativa os 3 pontinhos, para parecer uma resposta mais humana
                Bot().send_action(sender_id, 'typing_on')
                # Responde usuário
                Bot().send_message(sender_id, answer)
    except Exception as e:
        print(traceback.format_exc())
    return ''
