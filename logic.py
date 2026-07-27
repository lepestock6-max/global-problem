import os, random

def send_picture_to_bot() -> str:
    images = os.listdir("pictures")  # ["1.png"]
    image = random.choice(images)
    return image


def send_mem_to_bot() -> str:
    images = os.listdir("mem")  # ["1.png"]
    image = random.choice(mem)
    return image