import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import emoji
import random
import time

def sendmessage(phoneNumber, msg, hour, minute):
    try:
        pywhatkit.sendwhatmsg(phoneNumber, msg, hour, minute)
        time.sleep(10)
        pyautogui.click()
        time.sleep(1)
        Controller().press(Key.enter)
        Controller().release(Key.enter)
        time.sleep(1)
        print("Сообщение отправлено!")
    except Exception as e:
        print(str(e))

message = random.choice(['Привет,как ты?',
             'Как твой день?',
             emoji.emojize('Люблю тебя :sparkling_heart:'),
             emoji.emojize(':red_heart:", variant="emoji_type'),
             emoji.emojize(':beating_heart:'),
             emoji.emojize(':smiling_face_with_heart-eyes:')])

phoneNumber = str(input('На какой номер вы хотели бы отправить сообщение? номер должен содержать телефонный код страны  '))
numberOfMessages = int(input('Сколько раз вы хотели бы отправить сообщение?  '))
startingHour = int(input('Этот скрипт отправляет сообщения случайным образом в течение 2 часов.\nВ котором часу вы хотели бы начать?  '))
endingHour = int(input('В котором часу вы хотели бы остановиться?  '))

while numberOfMessages != 0:
    hour = random.randrange(startingHour, endingHour)
    minute = random.randrange(0, 60)
    numberOfMessages -= 1
    sendmessage(phoneNumber, emoji.emojize('Люблю тебя :sparkling_heart:'), hour, minute)