import telebot #импорт библиотеки.

bot = telebot.TeleBot("7169016636:AAFdKBabPxu0g3t2vAB20hGol3ttOquorJY") #Инициализация бота с телеграммом.
todo_list = [] #массив с задачами.

@bot.message_handler(commands=['start']) #Получение команды start для начала работы.
def start_message(message): #создание функции для этой команды.
    bot.send_message(message.chat.id, "Привет! Этот бот поможет вам управлять вашим todo list. Используйте /add чтобы добавить задачу.") #Бот отправляет текст после команды старт.

@bot.message_handler(commands=['add']) #Получение команды add для добавления заметки.
def add_task(message): #Создание функции для этой команды 
    task = ' '.join(message.text.split()[1:]) #Обьявление переменной после команды /add
    todo_list.append(task) #Добавления task в массив задач.
    bot.send_message(message.chat.id, f"Задача '{task}' добавлена в ваш todo list.") #Отправка ботом сообщения о том что текст добавлен в заметки.

@bot.message_handler(commands=['delete']) #Получение команды delete для удаления заметки.
def delete_task(message): #Создание функции этой команды.
    if len(todo_list) == 0: #Если длина массива задач равна нулю бот отправляет сообщение о том что лист пуст.
        bot.send_message(message.chat.id, "Ваш todo list пуст.")
    else: #Если длина массива задач больше 1 
        task_index = int(message.text.split()[1]) - 1 #Индекс заметки
        if task_index < 0 or task_index >= len(todo_list): #Если он меньше 0 или индекс больше длины массива.
            bot.send_message(message.chat.id, "Неверный номер задачи.")
        else: #Если номер существует то выведет о том что функция удалена.
            deleted_task = todo_list.pop(task_index)
            bot.send_message(message.chat.id, f"Задача '{deleted_task}' удалена из вашего todo list.")

@bot.message_handler(commands=['list']) #Получение команды list 
def show_list(message): # Создание функции этой команды.
    if not todo_list: #Если тудулист пуст то выведет уведомление о том что он пуст - логично
        bot.send_message(message.chat.id, "Ваш todo list пуст.")
    else: #Если он не пустой то выведет лист.
        tasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(todo_list)])
        bot.send_message(message.chat.id, f"Ваш todo list:\n{tasks}")

bot.polling() #