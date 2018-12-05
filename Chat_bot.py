from config import *

bot = telebot.TeleBot(token = bot_token)

@bot.message_handler(func=lambda message: message.chat.id==chat1_id, commands = ['start'])
def send_welcome(message):
    log_message(message)
    bot.reply_to(message, 'Greetings.')


@bot.message_handler(commands = ['help'])
def send_info(message):
    log_message(message)
    if message.chat.id==chat1_id:
        bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.from_user.id, "Чем могу быть полезен?\nЗадаш вопрос, вскоре получишь ответ.")


@bot.message_handler(func=lambda message: message.chat.id==chat1_id)
def universal_receiveing(message):
    log_message(message)
    if calculate(message) == 1:
        bot.delete_message(chat1_id, message.message_id)


while True:
    # if getDate().tm_yday != date.tm_yday:
    #     zeroTable()
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
