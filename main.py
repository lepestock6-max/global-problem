import telebot
from config import token
from logic import send_picture_to_bot, send_mem_to_bot, send_voice 
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import sovet
import os
import pyttsx3

engine = pyttsx3.init() 

bot = telebot.TeleBot(token)

answers = {}

def get_markup(options):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2  
    for option in options:       
        button = InlineKeyboardButton(text=option, callback_data=option)
        markup.add(button)
    return markup

#приветсвие бота
@bot.message_handler(commands=["start"])
def start_bot(message):
  bot.send_message(
      message.chat.id,
      "Привет! надеюсь ты почитал обо мне в гитхабе если нет то здесь краткая"
      " инфа обо мне -> Я бот помощник по теме глобального потепления",
  )
#голосовое сообщение
  chat_id = message.chat.id
  voice_text = "Привет! Я бот помощник по теме глобального потепления."


  file_path = create_welcome_voice(voice_text)

  with open(file_path, "rb") as voice_file:
    bot.send_voice(chat_id, voice_file)

#список всех команд
@bot.message_handler(commands=["help"])
def start_help(message):
    bot.send_message(message.chat.id, """
    /mem - мемы по теме Глобальному Потеплению 
    /picture - картинки с правилами/советами по теме Глобальному Потеплению 
    /solution - помощь в решении проблемы глобального потепления(совет дня)
    /test - тест по теме Глобальному Потеплению
    """)


#выдаёт рандомную картинку

@bot.message_handler(commands=["picture"])
def start_picture(message):
    with open(f"/pictures/{send_picture_to_bot()}", "rb", encoding="utf-8") as file:
        bot.send_photo(message.chat.id, file)


#выдаёт рандомный мем

@bot.message_handler(commands=["mem"])
def start_mem(message):
    with open(f"/mem/{send_picture_to_bot()}", "rb", encoding="utf-8") as photo:
        bot.send_photo(message.chat.id, photo)



#тест(мини игра)

@bot.message_handler(commands=['test'])
def handle_test(message):
    question = "Что больше всего ускоряет глобальное потепление?"
    options = ["Посадка новых деревьев в лесах", "Сжигание нефти, газа и угля", "Использование солнечных батарей", "Поездки на велосипедах"]
    
    
    markup = get_markup(options)
    bot.send_message(message.chat.id, question, reply_markup=markup)
    
    
    answers[message.chat.id] = None  

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.message.chat.id
    selected_option = call.data  
    answers[user_id] = selected_option
    
    response = f"Вы выбрали: {selected_option}"

    if len(answers) > 1:
        response += "Продолжаем опрос? (да/нет)"
        bot.send_message(user_id, response, reply_markup=get_markup(options))
    else:
        response += "Спасибо за участие!"

    bot.answer_callback_query(call.id, response)


#команда с советами дня

@bot.message_handler(commands=['solution'])
def send_welcome(message):
    bot.reply_to(message, "Привет! я дам тебе совет дня, просто напиши /sov")

@bot.message_handler(commands=['sov'])
def send_tip(message):
    chosen_sov = random.choice(sovet)
    bot.reply_to(message, chosen_sov)

bot.infinity_polling()
