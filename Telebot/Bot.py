import telebot
from env import TOKEN, CHAT_ID
from Database import Database
from signal import signal, SIGINT
from datetime import datetime
import os

bot = telebot.TeleBot(TOKEN)

class Bot:
    def __init__(self, database):
        self.token 		= TOKEN
        self.chat_id 	= CHAT_ID
        self.bot 	    = bot
        self.database   = database
        self.is_stopped = False
        self.updater    = None
        self.running    = False

        """
        Send a message when the command /start or /help is issued.
        """
        @bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            msg = self.reply_to(message, "Welcome !")

        """
        Send last data when the command /last is issued.
        """
        @bot.message_handler(commands=['last'])
        def send_last(message):
            lastData   = self.database.getLastData()
            time 	   = datetime.fromtimestamp(lastData["time"]).strftime("%d/%m/%Y %H:%M:%S")
            msgToSend  = "Last data:\n"
            msgToSend += "\tTime: " + time + "\n"
            msgToSend += "\tTemperature: " + str(lastData["temperature"]) + " °C\n"
            msgToSend += "\tHumidity: " + str(lastData["humidity"]) + " %\n"
            msgToSend += "\tPressure: " + str(lastData["pressure"]) + " hPa\n"
            msgToSend += "\tAltitude: " + str(lastData["altitude"]) + " m\n"
            msgToSend += "\tGas resistance: " + str(lastData["gas_resistance"]) + " Ohm\n"
            self.reply_to(message, msgToSend)

        """
        Stop the bot when the command /stop is issued.
        """
        @bot.message_handler(commands=['stop'])
        def send_stop(message):
            self.reply_to(message, "Bot stopped")
            self.stop()

        print("Bot initialized")

    def send_message(self, message):
        self.bot.send_message(self.chat_id, message)

    def reply_to(self, message, text):
        self.bot.reply_to(message, text)

    def is_running(self):
        return not self.is_stopped

    def run(self):
        self.is_stopped = False
        if self.running == False:
            self.running = True
            bot.infinity_polling(none_stop=True, interval=0)
            print("Bot running")

    def stop(self, *args, **kwargs):
        self.is_stopped = True
        self.running = False
        print("Bot not running")

if __name__ == '__main__':
    db = Database()
    myBot = Bot(db)

    # Register a signal handler to stop the bot gracefully
    signal(SIGINT, myBot.stop)

    try:
        myBot.run()
    except Exception as e:
        print(f"An error occurred: {e}")
