import logging
# import pandas as pd
import telegram
import numpy as np
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
bot = telegram.Bot(token='5571349214:AAHCWNDBusMF7MYjhJ-QXjpSBNRqcyDzyX8')
try:
    chat_id = bot.get_updates()[-1].message.chat_id
except IndexError:
    chat_id = 0
####################################################################################################################

async def blockchain_stats():
    # Info Blockchain Stats
    url_pool = "https://api.blockchain.info/stats"
    r = await requests.get(url_pool)
    return r.json()

def pool_stat():
    # Info Pool Stats
    url_pool = "https: // api.blockchain.info/pools?timespan = 7 days"
        
    r = requests.get(url_pool)
    return r.json()

class data:
    pool = pool_stat()
    stat = blockchain_stats()

def ThConstProfit():
    # For now is only Statit Calc but should be more efficient
    binance_calc = 0.00012648 / 37.14
    return binance_calc


async def currency_international_price(update):
    # Get diferent BTC prices diferent currency.
    url_pool = "https: // blockchain.info/ticker"
    r = await requests.get(url_pool)
    json_prices = r.json()
    prices = [str(i["symbol"] + i["15m"]) for i in json_prices]
    update.message.reply_text('International prices:'
                              +str( [(i+"\n")  for i in prices]))
    
    

def soporte(update, context):

    update.message.reply_text('''Hola!, Soy un Bot Beta que calcula el Profit Diario y Mensual basado en el consumo KW/h y El poder de Computo en (TH). Por ahora me crearon con ese fin quizas con el tiempo de uso podre desarrollar mas herramientas y mas facil para ti. Esto es un desarrollo de Doctorminer & Leviatan CryptoLab.
    Los Creadores de este Proyecto: Juan Vicente Ventrone y Theo Toukoumidis.\n Nota!: Es un desarrollo Beta puede tener Fallas.
    https://t.me/JVentrone''')


def start(update, context: CallbackContext):
    update.message.reply_text(
        'Hola! ' + str(update.message.chat.username) +
        ', Presentamos diferentes Estadisticas Para Mineros la Idea  ofrecer Herramientas a nuestra Comunidad.\n' +
        'Mayor Informacion de este Bot /info\n' +
        '¿Quienes somos? /soporte'
    )

def total_stat(update):
    stat = blockchain_stats()
    thProfit = ThConstProfit()
    volumen_perBlock = stat['trade_volume_usd'] / \
        stat['n_blocks_mined']
        
    update.message.reply_text(
        'Precio Hash-USD: '+ str(thProfit)+'\n'
        'Precio BTC-USD: ' + str(stat['market_price_usd'])+'\n'
        'Hashrate: ' + str(stat['hash_rate'])+'\n'
        'Dificultad: ' + str(stat['difficulty'])+'\n'
        'Siguiente Bloque: ' + str(stat['nextretarget'])+'\n'
        'Minutos entre Bloques: ' + str(stat['minutes_between_blocks'])+'\n'
        'Estimado Volumen de Transacción en USD: ' +
        str(stat['estimated_transaction_volume_usd'])+'\n'
        'Minutos entre Bloques: ' + str(stat['minutes_between_blocks'])+'\n'
        'Volumen USD por Bloque: ' +
        str(volumen_perBlock)+'\n'
        )
    

def info(update, context):
    update.message.reply_text(
        'Precio BTC: Precio Actual BTC-USD \n\n' +
        'Precio Internacional: Precio Actual BTC respecto diferentes Monedas \n'
        'MinerStat: Estadistica total, Hashrate, Bloques Minados, Siguiente Bloque, Ultimo bloque, Dificultad, etc...\n'
        'PoolStat: Numero de Bloques minado en 7 dias \n'
        )
def calc(update):
    
    keyboard = [[InlineKeyboardButton(text='⚒🖥 VS ⚡🔌',
                                      url='https://t.me/LatamStatBot')],]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        'Calcula EL rendimiento de tus TH  "VS""  el consumo electrico', reply_markup=reply_markup
    )
def usd_price(update):
    stat = blockchain_stats()
    update.message.reply_text( '$'+  str(stat['market_price_usd']) )

def main():

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        '5571349214:AAHCWNDBusMF7MYjhJ-QXjpSBNRqcyDzyX8', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # p.add_handler(CommandHandler("menu", menu))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("estadisticas General", total_stat))
    dp.add_handler(CommandHandler("soporte", soporte))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("precio int.", currency_international_price))
    dp.add_handler(CommandHandler("precio", usd_price))
    p.add_handler(CommandHandler("calc", calc))
    # dp.add_handler(MessageHandler(Filters.sticker, sticker))
    # dp.add_handler(MessageHandler(Filters.text, echo))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

