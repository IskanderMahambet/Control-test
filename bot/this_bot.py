import telebot


token = '485606860:AAFC1eSP_LksyJSRHsDK0Z9b49Rt4u_YzEI'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def check_message(message):

    t = message.text
    t=t[::-1]
    bot.send_message(message.chat.id, t)

bot.polling(none_stop=True)
