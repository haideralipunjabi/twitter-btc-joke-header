from requests.api import get
import tweepy
from datetime import datetime
from dateutil.relativedelta import relativedelta
from PIL import Image, ImageDraw, ImageFont
import os
import requests

API = "https://api.cryptonator.com/api/full/btc-usd"

BASE_DIR = os.path.dirname(__file__)
COLORS  = {
    "FOREGROUND": "#57cc8a",
    "BACKGROUND": "#242930",
    "WHITE": "#FFFFFF",
}
FONTS = {
    "TITLE": ImageFont.truetype(os.path.join(BASE_DIR,"fonts/OpenSans-Regular.ttf"),40),
    "NUMBERS": ImageFont.truetype(os.path.join(BASE_DIR,"fonts/OpenSans-ExtraBold.ttf"),60),
    "SUBTITLE": ImageFont.truetype(os.path.join(BASE_DIR,"fonts/OpenSans-Light.ttf"),20),
}

def get_prices():
    r = requests.get(API,headers={'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'})
    data = r.json()
    price = round(float(data['ticker']['price']))
    change = round(float(data['ticker']['change']))
    return [price-change,price,price+change]

def drawheader(data):
    img = Image.new('RGB',(1500,500),color=COLORS['BACKGROUND'])
    d = ImageDraw.Draw(img)
    d.text((750,200), "A boy asked his bitcoin-investing dad for 1 bitcoin for his birthday",fill=COLORS['FOREGROUND'],font=FONTS["TITLE"],anchor="mm")
    d.multiline_text((750,300),f"Dad: What? {'${:,}'.format(data[0])}??? {'${:,}'.format(data[1])} is a lot of money!\nWhat do you need {'${:,}'.format(data[2])} for anyway?", fill=COLORS['FOREGROUND'],font=FONTS["TITLE"],anchor="mm",align="center")
    d.multiline_text((750,450),"This Header Image has been generated using code. The code runs every 5 minutes\nCode: github.com/haideralipunjabi/twitter-btc-joke-header",fill=COLORS["WHITE"],font=FONTS["SUBTITLE"],anchor="mm",align="center")


    img.save("header.png")

drawheader(get_prices())