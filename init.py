import configparser
import logging

import numpy as np
import prettytable as pt
import requests
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackContext, CommandHandler, Updater

# Enable logging
config = configparser.ConfigParser()
config.read('conf.ini')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
bot = telegram.Bot(token=config['KEY']['token'])
try:
    chat_id = bot.get_updates()[-1].message.chat_id
except IndexError:
    chat_id = 0
####################################################################################################################

def blockchain_stats():
    # Info Blockchain Stats
    url_pool = "https://api.blockchain.info/stats"
    r = requests.get(url_pool)
    return r.json()

def pool_stat():
    # Info Pool Stats
    url_pool = "https://api.blockchain.info/pools?timespan=7days"
        
    r = requests.get(url_pool)
    return r.json()

class data:
    pool = pool_stat()
    stat = blockchain_stats()

def ThConstProfit():
    # For now is only Statit Calc but should be more efficient
    binance_calc = 0.00012648 / 37.14
    return binance_calc


def inter_price(update, context):
    # Get diferent BTC prices diferent currency.
    url_pool = "https://blockchain.info/ticker"
    r = requests.get(url_pool)
    prices = r.json()
    tittles = ['-', 'Unidad', 'Simbolo']
    data = [('BTC-'+ i, prices[i]['last'], i) for i in prices]
    send_table(update, CallbackContext, tittles, data)
    
    

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
    calc(update, context)

def general_stat():
    stat = blockchain_stats()
    thProfit = ThConstProfit()
    tittles = ['', 'Unidad', 'Simbolo']
    volumen_perBlock = stat['trade_volume_usd'] / \
        stat['n_blocks_mined']
    TH = thProfit/0.00000001
    profit_THUSD = thProfit*stat['market_price_usd']
    data = [
        ('Precio BTC-USD', stat['market_price_usd'], '$'),
        ('ProfitDay TH-SAT', round(TH), 'SAT'),
        ('ProfitDay TH-USD', profit_THUSD, 'TH/$'),
        ('Hashrate', stat['hash_rate'], 'TH/s'),
        ('Dificultad', stat['difficulty'], ''),
        ('Sig. Bloque', stat['nextretarget'], 'BLock'),
        ('Tiempo entre Bloques', stat['minutes_between_blocks'], 'Min'),

        ('Vol-Trans USD',
         stat['estimated_transaction_volume_usd'], '$', ),

        ('Vol-USD por Bloque', volumen_perBlock, '$')

    ]
    return tittles, data

def total_stat(update, context):
    tittles, data = general_stat()
    send_table(update, CallbackContext, tittles, data)

def min_stat(update, context):
    tittles, data = general_stat()
    logs = [(i + ' - ' + f'{unit:,.2f}' + ' ' + symbol + ' \n\n')
            for i, unit, symbol in data]
    c = ''
    for i in logs:
        c = c + i
    update.message.reply_text( c )

def profit_pool(update, context):
    pool=pool_stat()
    data = [(i, pool[i], 'in 7 Days') for i in pool]
    tittles = ['Pools', 'Bloques Minados', 'Tiempo']
    send_table(update, CallbackContext, tittles, data)
    
def send_table(update: Updater, context: CallbackContext,tittles, data):
    table = pt.PrettyTable(tittles)
    table.align[tittles[0]] = 'l'
     
    for item, units, symbol in data:
        table.add_row([item, f'{units:,.2f}', symbol])

    update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)
    
    
def info(update, context):
    update.message.reply_text(
        'Estadistica General para Mineros, las tablas solo seran reflejadas en desktop'
        )

def calc(update, context):
    
    keyboard = [[InlineKeyboardButton(text='⚒🖥   VS   ⚡🔌',
                                      url='https://t.me/Hosting_calc_Bot')], ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        'Calcula EL rendimiento de tus TH  "VS""  el consumo electrico', reply_markup=reply_markup
    )


def usd_price(update, context):
    stat = blockchain_stats()
    price = stat['market_price_usd']
    update.message.reply_text('Precio BTC-USD - $' + f'{price:,.2f}')
    
def main():

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater( config['KEY']['token'], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("tablestat", total_stat))
    dp.add_handler(CommandHandler("textstat", min_stat))
    dp.add_handler(CommandHandler("tableinterprice", inter_price))
    dp.add_handler(CommandHandler("usdprice", usd_price))
    dp.add_handler(CommandHandler("tablepoolstat", profit_pool))
    dp.add_handler(CommandHandler("soporte", soporte))
    dp.add_handler(CommandHandler("info", info))
    
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

