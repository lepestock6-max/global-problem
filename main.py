import telebot
from config import token
from logic import send_picture_to_bot, send_mem_to_bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(token)



@bot.message_handler(commands=["start"])
def start_bot(message):
    bot.send_message(message.chat.id, "Привет! надеюсь ты почитал обо мне в гитхабе если нет то здесь краткая инфа обо мне -> Я бот помошник по теме глобального потепления")

@bot.message_handler(commands=["help"])
def start_help(message):
    bot.send_message(message.chat.id, """
    /mem - мемы по теме Глобальному Потеплению 
    /picture - картинки с правилами/советами по теме Глобальному Потеплению 
    /solution - помощь в решении проблемы глобального потепления
    /test - тест по теме Глобальному Потеплению
    """)

@bot.message_handler(commands=["picture"])
def start_picture(message):
    with open(f"/pictures/{send_picture_to_bot()}", "rb", encoding="utf-8") as photo:
    bot.send_message(message.chat.id, "Я отправляю тебе картинки с правилами/овтетами по теме Глобальному Потеплению")

@bot.message_handler(commands=["mem"])
def start_picture(message):
    with open(f"/mem/{send_picture_to_bot()}", "rb", encoding="utf-8") as photo:
    bot.send_message(message.chat.id, "Я отправляю тебе полезные и интересные мемы по теме Глобальному Потеплению")

@bot.message_handler(commands=["test"])
def start_bot(message):
    bot.send_message(message.chat.id, "Привет! готов пройти тест по теме глобального потепления? ответь кнопками")

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())



bot.polling()

