import telebot
import random
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
        cock = types.InlineQueryResultArticle('1', 'Brain',
                                types.InputTextMessageContent(brainSize(call), parse_mode = 'MarkdownV2'),
                                description = "Random brain generator",
                                thumb_url = "https://dictionary.cambridge.org"
                                "/ru/images/thumb/cocker_noun_002_07370.jpg?version=5.0.239:")
        gay = types.InlineQueryResultArticle('2', 'Person Percentage',
                                types.InputTextMessageContent(personSize(call), parse_mode = 'MarkdownV2'),
                                description = "Random person generator",
                                thumb_url = "https://upload.wikimedia.org/wikip"
                                "edia/commons/thumb/1/12/LGBT_flag_square.svg/"
                                "2048px-LGBT_flag_square.svg.png")
        bot.answer_inline_query(call.id, [brain, person], is_personal = True, cache_time = 3600 * 4)
    except Exception as e:
        print(e)

def brainSize(message):
    try:
        name_seq = ['Мозг', 'Думательная мышца', 'Череп']
        emoji_seq = ['\U0001F60A', '\U0001F60D', '\U0001F632', '\U0001F925']
        user = strReplace(message.from_user.username)
        result = random.choice(name_seq)+' у @'+user+' *'+str(random.randint(0, 40))+'см в  обхвате*\. '+ random.choice(emoji_seq)
    except Exception as e:
        print(e)
    return result
def personSize(message):
    try:
        chat_id = "AnyChat"
        user = strReplace(message.from_user.username)
        result = '@' + user + ' сегодня человек на *'+str(random.randint(0, 100))+'%*\! \U0001F3F3\uFE0F\u200D\U0001F308'
    except Exception as e:
        print(e)
    return result

def strReplace(str):
    replacement = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for x in replacement:
        str = str.replace(x, '\\'+ x)
    return str

bot.infinity_polling()
