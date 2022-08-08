import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    line_bot_api.reply_message(event.reply_token,TextSendMessage(message))


    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
  
    if event.message.text == "訂餐":
        reply = TextSendMessage(text="https://docs.google.com/spreadsheets/d/1kzhcIPBUlz2_U34-KQzhPWio4IQC5HHwwXPMMdzIe30/edit#gid=0")
    line_bot_api.reply_message(event.reply_token, reply)

