import telebot
from web3 import Web3
# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
from dotenv import load_dotenv
import os


w3 = Web3()

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variable
TOKEN = os.getenv('BOT_TOKEN')


# You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot(token=TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, """
Welcome to AI Oraichain (V1)! Here is the list of commands : 

/audit CA or just paste the CA - AI Generated security report for a token  
/dapp URL - AI Generated security report for a dApp  
/chart CA - OnchainChart + AI Generated charting analysis  
/nft CA - NFT audit & AI authenticity detection  
/sentiment CA - Live social media sentiment analysis (available on V2) 
/assistant - PaladinAI personal & trained assistant (Available on V3) 

/settings - Configure the bot for your group/channel 
/advertise - Book an AD on PaladinAI 
/premium - Subscribe to Premium and use PaladinAI to it's full potential (Not yet available, available on V2) 

You can add this bot to any group or use the commands above in this chat. 

Developers: Want to use our data? Reach out to us.
""")


@bot.message_handler(commands=['audit'])
def audit_token(message):
    # Extract the argument from the command
    if len(message.text.split()) > 1:
        token_address = message.text.split()[1]
        is_valid_address = w3.is_address(token_address)

        # Print the result
        if is_valid_address:
            print(f"{token_address} is a valid Ethereum address.")
        else:
            print(f"{token_address} is not a valid Ethereum address.")

        bot.reply_to(message, f"Auditing token: {token_address}")
        # Implement your logic for auditing the token here
    else:
        bot.reply_to(
            message, "Please provide a token address with the /audit command.")


@bot.message_handler(commands=["ohlc"])
def ohlc(message):
    # Extract the argument from the command
    if len(message.text.split()) > 1:
        token_address = message.text.split()[1]
        bot.reply_to(message, f"Auditing token: {token_address}")
        # Implement your logic for auditing the token here
    else:
        bot.reply_to(
            message, "Please provide a token address with the /ohlc command.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.infinity_polling()
