import telebot
import logging
import io
import os
from pyzbar.pyzbar import decode
from os import listdir
from os.path import isfile, join
from io import BytesIO
from PIL import Image
import dataset
import time
import pyotp

# logger = telebot.logger
# telebot.logger.setLevel(logging.INFO)

db = dataset.connect('sqlite:///totpqr.db')

TOKEN = "1919133218:AAH2xE7vGW4Y9IvNrhwtFMF9moCP2gTIzB0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
        bot.send_message(message.chat.id, "Привет! Отправь мне QR-code.",)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
        chat_id = message.chat.id

        bot.send_message(message.chat.id, "Принял картинку.")
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        qrcode(downloaded_file)



def qrcode(downloaded_file):
        barcode = decode(Image.open(io.BytesIO(downloaded_file)))
        for decoded in barcode:
                data = decoded.data
                data = str(data)
                text = (data[data.find('\''):]).replace('\'', '')
                print(text)
                


#def totp_g():
#   0    totp = pyotp.TOTP(barcode)
#       totp.now() '
bot.polling()
