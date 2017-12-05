# -*- coding: utf-8 -*-
from flask import current_app
from requests_toolbelt import MultipartEncoder
import json
import requests


class Bot():
    def send_message(self, recipient_id, message):
        '''Enviar mensagem de texto para o destinatário especificado.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/text-message

        Entrada:
            recipient_id: id do destinatário para enviar para
            message: mensagem para enviar
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'text': message
            }
        }
        return self.send(payload)

    def send_generic_message(self, recipient_id, elements):
        '''Send generic messages to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/generic-template

        Entrada:
            recipient_id: id do destinatário para enviar para
            elements: elementos genéricos de mensagem para enviar
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": elements
                    }
                }
            }
        }
        return self.send(payload)

    def send_button_message(self, recipient_id, text, buttons):
        '''Enviar mensagem de texto para o destinatário especificado.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/button-template

        Entrada:
            recipient_id: id do destinatário para enviar para
            text: mensagem para enviar
            buttons: botões para enviar
        Saída:
            Resposta da API como <dict>
        '''

        payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": text,
                        "buttons": buttons
                    }
                }
            }
        }
        return self.send(payload)

    def send_image(self, recipient_id, image_path):
        '''Enviar uma imagem para o destinatário especificado. A imagem deve ser PNG, JPEG ou GIF.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/image-attachment

        Entrada:
            recipient_id: id do destinatário para enviar para
            image_path: caminho para a imagem a ser enviada
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': json.dumps(
                {
                    'id': recipient_id
                }
            ),
            'message': json.dumps(
                {
                    'attachment': {
                        'type': 'image',
                        'payload': {}
                    }
                }
            ),
            'filedata': (image_path, open(image_path, 'rb'))
        }
        multipart_data = MultipartEncoder(payload)
        multipart_header = {
            'Content-Type': multipart_data.content_type
        }
        return requests.post(self.base_url, data=multipart_data, headers=multipart_header).json()

    def send_image_url(self, recipient_id, image_url):
        '''Enviar uma imagem para o destinatário especificado usando a URL. A imagem deve ser PNG, JPEG ou GIF.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/image-attachment

        Entrada:
            recipient_id: id do destinatário para enviar para
            image_url: url da imagem a ser enviada
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': json.dumps(
                {
                    'id': recipient_id
                }
            ),
            'message': json.dumps(
                {
                    'attachment': {
                        'type': 'image',
                        'payload': {
                            'url': image_url
                        }
                    }
                }
            )
        }
        return self.send(payload)

    def send_action(self, recipient_id, action):
        '''Enviar indicadores de digitação ou enviar recibos de leitura para o destinatário. A imagem deve ser PNG ou JPEG.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions

        Entrada:
            recipient_id: id do destinatário para enviar para
            action: tipo da ação (mark_seen, typing_on, typing_off)
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': {
                'id': recipient_id
            },
            'sender_action': action
        }
        return self.send(payload)

    def send_audio(self, recipient_id, audio_path):
        '''Enviar áudio para o destinatário especificado. O áudio deve ser MP3 ou WAV
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/audio-attachment

        Entrada:
            recipient_id: id do destinatário para enviar para
            audio_path: caminho para o áudio a ser enviado
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': json.dumps(
                {
                    'id': recipient_id
                }
            ),
            'message': json.dumps(
                {
                    'attachment': {
                        'type': 'audio',
                        'payload': {}
                    }
                }
            ),
            'filedata': (audio_path, open(audio_path, 'rb'))
        }
        multipart_data = MultipartEncoder(payload)
        multipart_header = {
            'Content-Type': multipart_data.content_type
        }
        return requests.post(self.base_url, data=multipart_data, headers=multipart_header).json()

    def send_audio_url(self, recipient_id, audio_url):
        '''Enviar áudio para o destinatário especificado usando a URL. O áudio deve ser MP3 ou WAV
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/audio-attachment

        Entrada:
            recipient_id: id do destinatário para enviar para
            audio_url: Url de áudio a ser enviado
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': json.dumps(
                {
                    'id': recipient_id
                }
            ),
            'message': json.dumps(
                {
                    'attachment': {
                        'type': 'audio',
                        'payload': {
                            'url': audio_url
                        }
                    }
                }
            )
        }
        return self.send(payload)

    def send_video(self, recipient_id, video_path):
        '''Enviar vídeo para o destinatário especificado. O vídeo deve ser MP4 ou MOV.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/video-attachment

        Entrada:
            recipient_id: id do destinatário para enviar para
            video_path: caminho para o vídeo a ser enviado
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': json.dumps(
                {
                    'id': recipient_id
                }
            ),
            'message': json.dumps(
                {
                    'attachment': {
                        'type': 'audio',
                        'payload': {}
                    }
                }
            ),
            'filedata': (video_path, open(video_path, 'rb'))
        }
        multipart_data = MultipartEncoder(payload)
        multipart_header = {
            'Content-Type': multipart_data.content_type
        }
        return requests.post(self.base_url, data=multipart_data, headers=multipart_header).json()

    def send_video_url(self, recipient_id, video_url):
        '''Enviar vídeo para o destinatário especificado usando a URL. O vídeo deve ser MP4 ou MOV.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/video-attachment

        Entrada:
            recipient_id: id do destinatário para enviar para
            video_url: urk de vídeo a ser enviado
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': json.dumps(
                {
                    'id': recipient_id
                }
            ),
            'message': json.dumps(
                {
                    'attachment': {
                        'type': 'audio',
                        'payload': {
                            'url': video_url
                        }
                    }
                }
            )
        }
        return self.send(payload)

    def send_file(self, recipient_id, file_path):
        '''Enviar o arquivo para o destinatário especificado.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/file-attachment

        Entrada:
            recipient_id: id do destinatário para enviar para
            file_path: caminho para o arquivo a ser enviado
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': json.dumps(
                {
                    'id': recipient_id
                }
            ),
            'message': json.dumps(
                {
                    'attachment': {
                        'type': 'file',
                        'payload': {}
                    }
                }
            ),
            'filedata': (file_path, open(file_path, 'rb'))
        }
        multipart_data = MultipartEncoder(payload)
        multipart_header = {
            'Content-Type': multipart_data.content_type
        }
        return requests.post(self.base_url, data=multipart_data, headers=multipart_header).json()

    def send_file_url(self, recipient_id, file_url):
        '''Envie o arquivo para o destinatário especificado usando a URL.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/file-attachment

        Entrada:
            recipient_id: id do destinatário para enviar para
            file_url: url do arquivo a ser enviado
        Saída:
            Resposta da API como <dict>
        '''
        payload = {
            'recipient': json.dumps(
                {
                    'id': recipient_id
                }
            ),
            'message': json.dumps(
                {
                    'attachment': {
                        'type': 'file',
                        'payload': {
                            'url': file_url
                        }
                    }
                }
            )
        }
        return self.send(payload)

    def send(self, payload):
        '''
            Enviar requisição.
        '''
        request_endpoint = 'https://graph.facebook.com/v2.10/me/messages'
        response = requests.post(
            request_endpoint,
            params={'access_token': current_app.config['FB_ACCESS_TOKEN']},
            json=payload
        )
        result = response.json()
        return result

    def get_profile(self, user_id):
        request_endpoint = 'https://graph.facebook.com/v2.10/' + user_id
        response = requests.get(
            request_endpoint,
            params={'access_token': current_app.config['FB_ACCESS_TOKEN']}
        )
        if response.status_code == 200:
            user_profile = response.json()
            return user_profile
        return None
