import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для старта
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я твой личный помощник.")

# Функция для обработки команд
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Я могу помочь тебе следить за проектами.")

# Основная функция для запуска бота
def main():
    updater = Updater("ВАШ_ТОКЕН", use_context=True)
    dispatcher = updater.dispatcher

    # Обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
