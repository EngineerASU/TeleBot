# Импортируем необходимые компоненты
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

# функция sms() будет вызвана пользователем при отправке команды /start,
# внутри функции будет описана логика при её вызове
def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?') # вывод сообщения в консоль при отправке команды /start
    bot.message.reply_text('Здравствуйте, {}! \n'
                           'Поговорите со мной!'.format(bot.message.chat.first_name)) # отправляем ответ
    # print(bot.message)

# функция parrot() отвечает тем же сообщением, которое ему прислали
def parrot(bot, update):
    print(bot.message.text) # печатаем на экран сообщение пользователя
    bot.message.reply_text(bot.message.text) # отправляем обратно текст пользователя

# Создаём (объявляем) функцию main, которая соединяется с платформой Telegram
def main():
    # описываем функцию (тело функции)
    # создадим переменную my_bot, с помощью которой будем взаимодействовать с нашим ботом
    my_bot = Updater(TG_TOKEN)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms)) # обработчик команды /start

    my_bot.dispatcher.add_handler((MessageHandler(Filters.text, parrot))) # обработчик текстового сообщения

    my_bot.start_polling() # проверяет наличие сообщений с платформы Telegram
    my_bot.idle() # бот будет работать, пока его не остановят

# Вызываем (запускаем) функцию main
main()