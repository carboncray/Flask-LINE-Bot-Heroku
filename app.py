import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

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
    get_message = event.message.text
    reply = TextSendMessage(text=f"{get_message}")   
    
     
    if event.message.text == "學院": reply = LocationSendMessage(title='台北市職能發展學院',address='台北市士林區士東路301號',latitude=25.1147168,longitude=121.5325171)
    if event.message.text == "訂餐": reply = TextSendMessage(text="https://docs.google.com/spreadsheets/d/1kzhcIPBUlz2_U34-KQzhPWio4IQC5HHwwXPMMdzIe30/edit#gid=0")
    if event.message.text == "貼圖": reply = StickerSendMessage(package_id='11538',sticker_id='51626494')
    if event.message.text == "鳳城": reply = FlexSendMessage(alt_text='鳳城燒臘天母店',contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "鳳城燒臘",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0,
            "text": "粵菜"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Place",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "台北市士林區天母北路16號",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Time",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "11:00 - 20:45",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "TEL",
                "color": "#aaaaaa",
                "flex": 1,
                "size": "sm"
              },
              {
                "type": "text",
                "text": "(02)2872-7500",
                "wrap": True,  
                "color": "#666666",
                "flex": 5,
                "size": "sm"
              }
            ],
            "spacing": "sm"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "foodpanda",
          "uri": "https://www.foodpanda.com.tw/restaurant/pi6f/feng-cheng-shao-la-yue-cai-tai-bei-tian-mu-dian?utm_source=google&utm_medium=organic&utm_campaign=google_reserve_place_order_action"
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
})
    line_bot_api.reply_message(event.reply_token, reply)
