import telebot
from Parsing import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import threading
import time

with open('Token', 'r') as f:
    token = f.read()

bot = telebot.TeleBot(token)

subscriptions = []


@bot.message_handler(commands=['start'])
def start(message):
    send_main_menu(message)


def send_main_menu(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("all")
    button2 = KeyboardButton("Exact Crypto")
    button3 = KeyboardButton("Subscribe to Crypto")
    button4 = KeyboardButton("Unsubscribe")
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(
        message.chat.id,
        "Hello, Choose option",
        reply_markup=keyboard
    )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() == "all":
        bot.send_message(message.chat.id, 'Wait a bit.. Parsing data')
        result = get_all_crypto()
        response = ''
        for name, price in result.items():
            response += f'{name} - {price}\n'
        bot.send_message(message.chat.id, response)
    elif message.text == "Exact Crypto":
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        for crypto in Crypto_list.keys():
            keyboard.add(KeyboardButton(crypto))
        keyboard.add(KeyboardButton("Back"))
        bot.send_message(
            message.chat.id,
            "Choose a cryptocurrency:",
            reply_markup=keyboard
        )
    elif message.text in Crypto_list.keys():
        crypto_info = get_crypto(message.text)
        if crypto_info and message.text in crypto_info:
            bot.send_message(message.chat.id, f"{message.text}: {crypto_info[message.text]}")
        else:
            bot.send_message(message.chat.id, "Data not found for this cryptocurrency.")
    elif message.text == "Back":
        send_main_menu(message)
    elif message.text == "Subscribe to Crypto":
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        for crypto in Crypto_list.keys():
            keyboard.add(KeyboardButton(crypto+'_sub'))
        keyboard.add(KeyboardButton("Back"))
        bot.send_message(
            message.chat.id,
            "Choose a cryptocurrency to subscribe:",
            reply_markup=keyboard
        )
    elif message.text == "Unsubscribe":
        for index,i in enumerate(subscriptions):
            if list(i.items())[0][0] == message.chat.id:
                del subscriptions[index]
        bot.send_message(message.chat.id, "Unsubscribe from all your subscriptions.")
    elif message.text[-4:] =='_sub':
        subscriptions.append({message.chat.id : message.text[:-4]})
        bot.send_message(message.chat.id,f'U subscribed to this cryptocurrency, {message.text[:-4]}')

def send_updates():
    while True:
        print('Update')
        print(subscriptions)
        for i in subscriptions:
            for user_id,crypto in i.items():
                print(f'For {user_id}, {crypto}')
                fetch = get_crypto(crypto)
                if fetch :
                    bot.send_message(user_id, f"Update for {crypto}: {fetch}")
                else:
                    bot.send_message(user_id, f"Could not fetch data for {crypto}.")
        time.sleep(5)



thread = threading.Thread(target=send_updates)
thread.daemon = True
thread.start()

bot.polling(none_stop=True)