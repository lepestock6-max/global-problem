import telebot
from config import token
from logic import send_picture_to_bot, send_mem_to_bot


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

bot.polling()
