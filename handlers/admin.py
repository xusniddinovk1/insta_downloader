from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes

from config import ADMIN_LIST


async def admin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    if str(user.id) in ADMIN_LIST:
        # change state
        context.user_data['state'] = 'ADMIN_HOME'

        await update.message.reply_html(
            text='Admin panelga xush kelibsiz',
            reply_markup=ReplyKeyboardMarkup([
                [KeyboardButton("➕ Kanal qo'shish"), KeyboardButton("✔️ Reklama qo'shish")],
                [KeyboardButton("❌ Chiqish")]
            ], resize_keyboard=True)
        )
    else:
        pass
