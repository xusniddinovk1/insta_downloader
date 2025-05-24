from telegram import Update
from telegram.ext import ContextTypes
from services.checking import check_user


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
            caption="Assalomu aleykum!\nBotimizga xush kelibsiz! Bu bot orqali siz Instagram, Facebook, TikTok dan video yuklab olishingiz mumkin."
        )
