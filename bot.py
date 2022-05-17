import telebot
import random
import db
import time
from telebot import types

#main variables
TOKEN = ""
bot = telebot.TeleBot(TOKEN)
chats = {}
#initializing database
database = db.db("Chatdb1")

#making super letters to normal text
#making funny insertions :D
#sending normal message



@bot.inline_handler(func=lambda c: True)
def default_query(call):
    try:
        cock = types.InlineQueryResultArticle('1', 'Cock Size',
                                types.InputTextMessageContent(cockSize(call), parse_mode = 'MarkdownV2'),
                                description = "Random cocksize generator",
                                thumb_url = "https://dictionary.cambridge.org"
                                "/ru/images/thumb/cocker_noun_002_07370.jpg?version=5.0.239:")
        gay = types.InlineQueryResultArticle('2', 'Gay Percentage',
                                types.InputTextMessageContent(gaySize(call), parse_mode = 'MarkdownV2'),
                                description = "Random gay generator",
                                thumb_url = "https://upload.wikimedia.org/wikip"
                                "edia/commons/thumb/1/12/LGBT_flag_square.svg/"
                                "2048px-LGBT_flag_square.svg.png")
#        bcock = types.InlineQueryResultArticle('3', 'Smallest cock',
#                                types.InputTextMessageContent('Cock is good2'),
#                                description = "Smallest cock in this chat",
#                                thumb_url = "https://cs11.pikabu.ru/post_img"
#                                "/big/2020/07/27/7/1595846674164769836.png")
#        bgay = types.InlineQueryResultArticle('4', 'Gayest Gay',
#                                types.InputTextMessageContent('Gay is perfect'),
#                                description = "Gayest gay in the chat",
#                                thumb_url = "https://pyxis.nymag.com/v1/imgs"
#                                "/e1a/46e/df11faaaf2f297b5f608e9968bd9b8f124"
#                                "-30-heman.rsquare.w330.jpg")
        bot.answer_inline_query(call.id, [cock, gay], is_personal = True, cache_time = 3600 * 4)
    except Exception as e:
        print(e)

def cockSize(message):
    try:
        name_seq = ['Членес', 'Пенис', 'Пиструн', 'Писюн']
        emoji_seq = ['\U0001F60A', '\U0001F60D', '\U0001F632', '\U0001F925']
        user = strReplace(message.from_user.username)
        result = random.choice(name_seq)+' у @'+user+' *'+str(random.randint(0, 40))+'см*\. '+ random.choice(emoji_seq)
    except Exception as e:
        print(e)
    return result
def gaySize(message):
    try:
        chat_id = "AnyChat"
        user = strReplace(message.from_user.username)
        result = '@' + user + ' сегодня гей на *'+str(random.randint(0, 100))+'%*\! \U0001F3F3\uFE0F\u200D\U0001F308'
    except Exception as e:
        print(e)
    return result

def strReplace(str):
    replacement = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for x in replacement:
        str = str.replace(x, '\\'+ x)
    return str

bot.infinity_polling()
