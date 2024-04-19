
import telebot #Импортируем библиотеку.

bot = telebot.TeleBot('7160501552:AAFmjrBE3XhbyucKrWDJLEKLaHR0RNuUfT0') #Подключаемся к боту.

@bot.message_handler(content_types=["text"])  #Считывание сообщения.
def repeat_all_messages(message): #Функция для этого сообщения.
    bot.send_message(message.chat.id, message.text) #Функция отправки сообщения

bot.polling(True) #Команда для того чтобы Бот Работал.
