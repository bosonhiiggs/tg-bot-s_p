import telebot
import random
from telebot import types

# загружаем список интересных файлов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

# загружаем список поговорок
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()

# создание бота
bot = telebot.TeleBot('5751773698:AAG5Dp-fUXwnppWqxbI867H2tmUtS3V-cK4')

# команда "start"
@bot.message_handler(commands = ['start'])
def start(m, res = False):
    #Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Факт')
    item2 = types.KeyboardButton('Поговорка')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Нажми: \nФакт для факта \nПоговорка для поговорки', reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    # проверка сообщений от пользователя
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    elif message.text.strip() == 'Поговорка':
        answer = random.choice(thinks)
    # ответ пользователю на его запрос
    bot.send_message(message.chat.id, answer)

# запуск бота
bot.polling(none_stop = True, interval = 0)