import json
import time
import requests
import steammarket as sm
from telegram.ext import Updater, CommandHandler
import telegram
import telebot
import config

bot = telegram.Bot(token='1228847437:AAGtjcYRpU4BaPdQe-gUIcThCudTpamvHec')

items_name = []

# def printDic(dic):
#     for item_name, item_count in dic.items():
#         print(item_name, item_count)

dic = {}

def process_name_step(message):
    chat_id = message.chat.id
    invent = message.text
    text = ''
    dic_item_name_count = {}
    inv_price = 0
    items_name = []

    list_ = getInventory(invent)

    for i in list_:
        name = i[0]
        items_name.append(i[0])
        dic_item_name_count[name] = i[1]

    for i in range(len(lootfarm_json_data)):
        if lootfarm_json_data[i]['name'] in items_name:
            text += lootfarm_json_data[i]['name'] + '  # ' + str(dic_item_name_count[lootfarm_json_data[i]['name']]) + ' #  ' + str(lootfarm_json_data[i]['price'] / 100) + '$' + '\n'

    #print(text)
    bot.send_message(chat_id=chat_id, text=text)


def getInventory(steamid):
    data = requests.get(
        "https://steamcommunity.com/id/{}/inventory/json/730/2?l=english&count=5000".format(steamid))
    json_data = json.loads(data.text)
    descriptions = json_data["rgDescriptions"]
    #print(descriptions)
    for item in descriptions:
        item_name = (descriptions[item]["market_hash_name"])
        if item_name not in items_name:
            items_name.append(item_name)
            item_count = (getItemAmount(descriptions[item]["classid"], json_data))
            dic[item_name] = item_count
        else:
            continue
    list_item = []
    for item in descriptions:
        temp_str = [descriptions[item]["market_hash_name"], getItemAmount(descriptions[item]["classid"], json_data)]
        list_item.append(temp_str)
    return list_item


def getItemAmount(classid, json_data):
    inventory = json_data["rgInventory"]
    count = 0
    for item in inventory:
        if inventory[item]["classid"] == classid:
            count += 1
    return count


lootfarm_invent = requests.get('https://loot.farm/fullprice.json')
lootfarm_json_data = json.loads(lootfarm_invent.text)

#printDic(dic)
inv_price = 0

API_TOKEN = '1228847437:AAGtjcYRpU4BaPdQe-gUIcThCudTpamvHec'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}
# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    #380630505992
    if len(message.text) == 12:
        process_name_step(message)

    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
bot.polling()
#print(getInventory(''))
#print(list_)

#list_ = [['Sealed Graffiti | Double (Wire Blue)', 1], ['CS20 Case', 3], ['SG 553 | Waves Perforated (Field-Tested)', 1], ['Danger Zone Case', 8], ['AK-47 | Redline (Field-Tested)', 1], ['StatTrak™ M4A4 | Magnesium (Minimal Wear)', 1], ['Souvenir Glock-18 | Night (Field-Tested)', 1], ['Sealed Graffiti | Take Flight (Monster Purple)', 1], ['USP-S | Flashback (Minimal Wear)', 1], ['Graffiti | Eye Spy (Dust Brown)', 1], ['Prisma Case', 4], ['Buckshot | NSWC SEAL', 1], ['MAC-10 | Silver (Factory New)', 1], ['Sealed Graffiti | Piggles (Desert Amber)', 1], ['Nova | Sand Dune (Field-Tested)', 1], ['Spectrum Case', 5], ['Clutch Case', 6], ['Spectrum 2 Case', 3], ['AK-47 | Safari Mesh (Field-Tested)', 1], ['MP9 | Sand Dashed (Minimal Wear)', 1], ['Enforcer | Phoenix', 1], ['Sealed Graffiti | Noscope (Tiger Orange)', 1], ['Graffiti | Cocky (Monster Purple)', 1], ['Tec-9 | Groundwater (Field-Tested)', 2], ['FAMAS | Colony (Well-Worn)', 1], ['Sealed Graffiti | Cocky (Brick Red)', 1], ['Shadow Case', 5], ['Sealed Graffiti | Worry (Frog Green)', 1], ['AUG | Contractor (Minimal Wear)', 1], ['Sealed Graffiti | Sheriff (Tiger Orange)', 1], ['2019 Service Medal', 1], ['Sealed Graffiti | Ninja (Monarch Blue)', 1], ['SCAR-20 | Sand Mesh (Field-Tested)', 1], ['Sealed Graffiti | Death Sentence (Tiger Orange)', 1], ['Sealed Graffiti | GLHF (Bazooka Pink)', 2], ['Souvenir P250 | Sand Dune (Field-Tested)', 1], ['Souvenir UMP-45 | Scorched (Battle-Scarred)', 1], ['Sealed Graffiti | GTG (Monarch Blue)', 1], ['Sealed Graffiti | Bling (Jungle Green)', 1], ['Sealed Graffiti | Take Flight (Cash Green)', 1], ['Sealed Graffiti | Quickdraw (Blood Red)', 1], ['Loyalty Badge', 1], ['Sealed Graffiti | Keep the Change (Jungle Green)', 1], ['AWP | Safari Mesh (Battle-Scarred)', 1], ['SSG 08 | Blue Spruce (Battle-Scarred)', 1], ['Sealed Graffiti | QQ (Princess Pink)', 1], ['Gamma Case', 5], ['Five-SeveN | Forest Night (Field-Tested)', 1], ['R8 Revolver | Bone Mask (Field-Tested)', 1], ['Sealed Graffiti | Eat It (Dust Brown)', 1], ['Chroma 3 Case', 5], ['Sealed Graffiti | Sorry (War Pig Pink)', 1], ['Sealed Graffiti | Chess King (Wire Blue)', 1], ['Sealed Graffiti | Keep the Change (Frog Green)', 1], ['Gamma 2 Case', 4], ['Sealed Graffiti | X-Axes (Monster Purple)', 1], ['2018 Service Medal', 1], ['Sealed Graffiti | Eat It (SWAT Blue)', 1], ['PP-Bizon | Urban Dashed (Field-Tested)', 1], ['Sealed Graffiti | Double (Dust Brown)', 1], ['Sealed Graffiti | Mr. Teeth (Tiger Orange)', 1], ['Sealed Graffiti | Take Flight (Brick Red)', 1], ['Sealed Graffiti | QQ (Frog Green)', 1], ['Sealed Graffiti | GGWP (Princess Pink)', 1], ['Sealed Graffiti | Eco (Monarch Blue)', 1], ['Sealed Graffiti | GTG (Blood Red)', 1], ['Sealed Graffiti | Bling (Dust Brown)', 1], ['2017 Service Medal', 1]]






