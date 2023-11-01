import telebot
from env import TOKEN, CHAT_ID
from time import sleep

bot = telebot.TeleBot(TOKEN)
class Bot:
	def __init__(self):
		self.token 		= TOKEN
		self.chat_id 	= CHAT_ID
		self.bot 	    = bot

		@bot.message_handler(commands=['help', 'start'])
		def send_welcome(message):
			msg = self.reply_to(message, "Welcome !")
			
		print("Bot initialized")

	def send_message(self, message):
		self.bot.send_message(self.chat_id, message)

	def reply_to(self, message, text):
		self.bot.reply_to(message, text)
	
	def get_updates(self):
		return self.bot.get_updates()

	def get_last_update(self):
		return self.bot.get_updates()[-1]

	def get_last_message(self):
		return self.get_last_update().message

	def get_last_message_text(self):
		return self.get_last_message().text

	def get_last_message_date(self):
		return self.get_last_message().date

	def run(self):
		print("Bot running")
		self.bot.infinity_polling()


if __name__ == '__main__':
	myBot = Bot()
	myBot.run()
		