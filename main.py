from admin import admin_handler
from config import BOT_TOKEN
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from messages import message_handler
from database import Database
from checking import check_user

# Logging
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

db = Database('insta_save.db')


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    if check_user(user):
        await update.message.reply_photo(
            photo=open("./media/logo.jpg", "rb"),
            caption=f"Assalomu aleykum {check_user(user).get('full_name')}\nBotimizga Xush kelibsiz!"
        )
    else:
        await update.message.reply_photo(
            photo=open("./media/logo.jpg", "rb"),
            caption=f"Assalomu aleykum !\nBotimizga Xush kelibsiz!Bu bot orqali siz Instagram, Facebook, TIkTok dan video yulab olishingiz mumkin"
        )


def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("admin", admin_handler))

    app.add_handler(MessageHandler(filters.TEXT, message_handler))
    app.run_polling()


if __name__ == "__main__":
    main()
