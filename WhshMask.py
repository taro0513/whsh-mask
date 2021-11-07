from flask import Flask, request, abort
from linebot import (
    LineBotApi,
    WebhookHandler)
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from Message.MessageReply import reply
from Message.Process import Process
from Config import config
from Drawpic import drawpic
pic = drawpic()

DetectionSetting = config(section='Bot').data()
app = Flask(__name__)
line_bot_api = LineBotApi(DetectionSetting['LineBotApi'])
handler = WebhookHandler(DetectionSetting['WebhookHandler'])

@app.route("/callback", methods=['POST'])
def callback():
    #X-Line-Signature <- [數位簽章](https://zh.wikipedia.org/zh-tw/%E6%95%B8%E4%BD%8D%E7%B0%BD%E7%AB%A0)
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try: handler.handle(body, signature)
    except InvalidSignatureError: abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    content = eval(str(event))
    print('Message ID  :{}'.format(content['message']['id']))
    print('Message TEXT:{}'.format(content['message']['text']))
    print('Message TYPE:{}'.format(content['message']['type']))
    message = str(Process.distinguish(content['message']['text']))
    if content['message']['text'] == 'S:GUI': line_bot_api.reply_message(event.reply_token,reply.GUI2())
    elif 'Y:' in content['message']['text'] : line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content['message']['text'].split(':')[1]))
    elif 'test' in content['message']['text'] : 
        pic.drax()
        url  = pic.upload()
        line_bot_api.reply_message(event.reply_token,reply.test(url))
    else:
        try:line_bot_api.reply_message(event.reply_token,message)
        except:line_bot_api.reply_message(event.reply_token,reply.nothis())

@handler.add(MessageEvent, message=ImageMessage)
def shandle_message(event):
    print('\n'+str(event))
    message = TextSendMessage(text='stest')
    line_bot_api.reply_message(event.reply_token,message)



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
