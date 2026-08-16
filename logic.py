import os, random, pyttsx3

#функция отправки случайной картинки
def send_picture_to_bot() -> str:
    images = os.listdir("pictures")  # ["1.png"]
    image = random.choice(images)
    return image

#функция отправки случайново мема
def send_mem_to_bot() -> str:
    mem = os.listdir("mem")  # ["1.png"]
    image = random.choice(mem)
    return image

#функция отправки голосового сообщения
def send_voice(text, filename="welcome.wav"):
  engine = pyttsx3.init()
  
  engine.save_to_file(text, filename)
  engine.runAndWait()

  return filename
