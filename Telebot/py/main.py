from Bot import Bot
from Database import Database
from env import TOKEN, CHAT_ID
from signal import signal, SIGINT
import sys

def main():

    db = Database()
    bot = Bot(db)

    # Register a signal handler to stop the bot gracefully
    signal(SIGINT, bot.stop)

    while bot.is_running():
        try:
            bot.run()
        except KeyboardInterrupt:
            # Handle Ctrl+C (SIGINT)
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break


if __name__ == '__main__':
    main()
