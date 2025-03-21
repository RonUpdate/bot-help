import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Dispatcher
from flask import Flask, request

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Функция для старта
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я твой личный помощник.")

# Функция для обработки команд
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Я могу помочь тебе следить за проектами.")

# Функция для настройки вебхука
def set_webhook(updater):
    webhook_url = "https://url-auto-delete-shortener-bot-o5y2.onrender.com/webhook"
    updater.bot.setWebhook(webhook_url)

# Обработчик запросов от Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = Update.de_json(json_str, updater.bot)
    dispatcher.process_update(update)
    return 'ok'

# Основная функция для запуска бота
def main():
    # Используем token из переменных окружения для безопасности
    updater = Updater("7953930520:AAHfK3RHiw5UNWxrBqkeqak1-9VuQ73O4tg", use_context=True)
    dispatcher = updater.dispatcher
    
    # Обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    
    # Настроим вебхук
    set_webhook(updater)
    
    # Запускаем Flask для обработки webhook
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
