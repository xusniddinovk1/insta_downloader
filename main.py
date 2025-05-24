from config import BOT_TOKEN
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers.start_handler import start_handler
from handlers.admin import admin_handler
from messages import message_handler
from database import Database

import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
db = Database('insta_save.db')


def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("admin", admin_handler))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    logger.info("Bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
