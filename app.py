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
    
     
    if event.message.text == "學院": reply = LocationSendMessage(title='台北市職能發展學院',address='台北市士林區士東路301號',latitude=25.1142633,longitude=121.535708)
    if event.message.text == "訂餐": reply = TextSendMessage(text="https://docs.google.com/spreadsheets/d/1tZUHTwKpXWIzQ1qbAi0SYfypfGnpULZti3uvomdTlvU/edit#gid=0")
    if event.message.text == "貼圖": reply = StickerSendMessage(package_id='11538',sticker_id='51626494')
    if event.message.text == "鳳城": reply = FlexSendMessage(alt_text='鳳城燒臘天母店',contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scontent-tpe1-1.xx.fbcdn.net/v/t1.18169-9/19554156_1401102563270671_3293336136946307640_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=e3f864&_nc_ohc=qUoUS--zcLwAX81qUgn&_nc_ht=scontent-tpe1-1.xx&oh=00_AT-lY8Dc9o1JGokXXl58OR0jFTClPtgSphkKcc-EIveA2g&oe=632B79AF",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://zh-tw.facebook.com/spring73512/"
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
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "來去訂餐",
          "uri": "https://docs.google.com/spreadsheets/d/1tZUHTwKpXWIzQ1qbAi0SYfypfGnpULZti3uvomdTlvU/edit#gid=0"
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
    if event.message.text == "良食堂": reply = FlexSendMessage(alt_text='良食堂',contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://img4.foodbevg.com/511/560/2818029725115604.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://www.instagram.com/lungshihtan/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "良食堂",
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
            "text": "台日式便當",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
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
                "text": "台北市士林區福華路145號1樓",
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
                "text": "11:00 - 13:30, 16:30 - 19:30(六日公休)",
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
                "flex": 1,
                "size": "sm",
                "color": "#aaaaaa"
              },
              {
                "type": "text",
                "text": "(02)2838-3009",
                "flex": 5,
                "wrap": True,
                "color": "#666666",  
                "size": "sm"
              }
            ]
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
          "uri": "https://www.foodpanda.com.tw/restaurant/pdm8/liang-shi-tang-1"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "來去訂餐",
          "uri": "https://docs.google.com/spreadsheets/d/1tZUHTwKpXWIzQ1qbAi0SYfypfGnpULZti3uvomdTlvU/edit#gid=0"
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
