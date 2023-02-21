from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from telegram import Bot
from value import get_id_user, get_input_data, get_result, save_val
from controllers import parseable_data, calculate

token1 = "6184639222:AAFbX666ZsmNLdKJqdsL1Z8bI_IGFAsSLrs"
bot = Bot(token=token1)
updater = Updater(token=token1)
dispatcher = updater.dispatcher

def start(update: Updater, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, "Привет! Я бот-калькулятор! Введите выражение без пробелов!")
    
    get_id_user(update.effective_chat.id)

def initial_data(update: Updater, context: CallbackContext):
    data = update.message.text
    get_input_data(data)
    list_data = parseable_data(data)
    result = calculate(list_data)
    get_result(result)
    save_val()
    context.bot.send_message(update.effective_chat.id, f'Результат вычислений: {result}')
    
start_handler = CommandHandler('start', start)
initial_data_handler = MessageHandler(Filters.text, initial_data)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(initial_data_handler)

updater.start_polling()
updater.idle()