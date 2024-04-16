
import telebot

bot = telebot.TeleBot('7160501552:AAFmjrBE3XhbyucKrWDJLEKLaHR0RNuUfT0')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

bot.polling(True)