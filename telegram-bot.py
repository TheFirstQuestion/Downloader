from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from downloader import isValid, manageMessage


# Get token from token.txt
with open("token.txt") as f:
    # Read file
    content = f.readlines()
    # Get rid of whitespace
    MY_TOKEN = content[0].strip()


# Create updater and dispatcher
updater = Updater(token=MY_TOKEN)
dispatcher = updater.dispatcher


# Define what to do
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="If it's not in your archive, you don't know it.")
# Specify when to do it
start_handler = CommandHandler('start', start)
# Watch for it
dispatcher.add_handler(start_handler)


# Define what to do
def parseMessage(bot, update):
    # Check that text was a valid command for the downloader
    if isValid(update.message.text):
        bot.send_message(chat_id=update.message.chat_id, text="Added to list! Will be downloaded when possible.")
        # Pass to downloader.py
        manageMessage(update.message.text)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that.")
# Specify when to do it
handler = MessageHandler(Filters.text, parseMessage)
# Watch for it
dispatcher.add_handler(handler)



# And, go!
updater.start_polling()
