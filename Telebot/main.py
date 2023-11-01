from Bot import Bot
from Database import Database
from env import TOKEN, CHAT_ID

def main():

    db = Database()
    bot = Bot(db)

    while True:
        try:
            bot.run()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
