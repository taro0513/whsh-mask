import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)
import json 
from DetectionSetting import DetectionSetting
line_bot_api = LineBotApi(DetectionSetting['LineBotApi'])
headers = { "Authorization": "Bearer /BtVRFWZOKbBcO/4OCml3nnqQCHTDYa51kvnE7B258rNBXfG4PPf+0kHYh62lVag0DmuCp4r4myEFSDsahZ58dFoaTaG79Gb4LeiN/QHeKvtEocOAboK7etFBGHxnAWfcMm+ci5QzrX4hRHhekq6EwdB04t89/1O/w1cDnyilFU=",
            "Content-Type": "application/json" }

def richmenu_Start(menu_id):
    req = requests.request('POST', f'https://api.line.me/v2/bot/user/all/richmenu/{menu_id}', 
                       headers=headers)
    return req.text

def body_Set():
    body = {
        "size": {"width": 2500, "height": 1686},
        "selected": "true",
        "name": "Controller",
        "chatBarText": "Controller",
        "areas":[
            {
            "bounds": {"x": 551, "y": 325, "width": 321, "height": 321},
            "action": {"type": "message", "text": "up"}
            },
            {
            "bounds": {"x": 876, "y": 651, "width": 321, "height": 321},
            "action": {"type": "message", "text": "right"}
            },
            {
            "bounds": {"x": 551, "y": 972, "width": 321, "height": 321},
            "action": {"type": "message", "text": "down"}
            },
            {
            "bounds": {"x": 225, "y": 651, "width": 321, "height": 321},
            "action": {"type": "message", "text": "left"}
            },
            {
            "bounds": {"x": 1433, "y": 657, "width": 367, "height": 367},
            "action": {"type": "message", "text": "btn b"}
            },
            {
            "bounds": {"x": 1907, "y": 657, "width": 367, "height": 367},
            "action": {"type": "message", "text": "btn a"}
            }
        ]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                        headers=headers,data=json.dumps(body).encode('utf-8'))

    return req.text

def body_Remove(menu_id:str) -> None:
    line_bot_api.delete_rich_menu(menu_id)

def richmenu_Search():
    rich_menu_list = line_bot_api.get_rich_menu_list()
    for rich_menu in rich_menu_list:
        print(rich_menu.rich_menu_id)
    return rich_menu_list

def image_Set(menu_id:str):
    with open("buttonr.jpg", 'rb') as f:
        line_bot_api.set_rich_menu_image(menu_id, "image/jpeg", f)

# print(body_Set())
# richmenu_Search()
# image_Set('richmenu-801c12aad422b60f20a2380f4dee64de')
# print(richmenu_Start('richmenu-801c12aad422b60f20a2380f4dee64de'))
# body_Remove('richmenu-801c12aad422b60f20a2380f4dee64de')