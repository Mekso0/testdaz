import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("7272558954:AAH77qVl2XkjmUOEFTF6vq9VPBw2bu0dOEA")  # Используйте os.getenv() для получения токена из переменных окружения
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    gif_path = "seal.gif"  # Путь к вашей гифке. Поместите файл seal.gif в ту же папку, где находится скрипт
    
    if not os.path.exists(gif_path):
       bot.send_message(message.chat.id, "Ошибка: гифка не найдена. Пожалуйста, убедитесь, что файл seal.gif находится в той же папке, что и скрипт.")
       return
    
    with open(gif_path, 'rb') as gif:
      bot.send_animation(message.chat.id, gif, caption="🦭 Привет! Это тест бот здесь ничего интересного)")

if __name__ == '__main__':
    bot.polling(none_stop=True)