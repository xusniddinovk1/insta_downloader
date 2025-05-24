from telegram import Update
from telegram.ext import ContextTypes
from services.checking import check_user
from handlers.admin_panel import handle_admin_state
from handlers.check_channel import check_channel_membership
from handlers.downloader_handler import handle_instagram_download

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = update.message.text

    if not user:
        await update.message.reply_text("Foydalanuvchi aniqlanmadi.")
        return

    if await handle_admin_state(update, context):
        return

    delete_message = await update.message.reply_text("⌛")
    check_user(user)

    if not await check_channel_membership(update, context, user):
        if delete_message:
            await delete_message.delete()
        return

    await handle_instagram_download(update, context, message, delete_message)
