from telegram import Update
from telegram.ext import ContextTypes
from validators import url
from downloader import insta_downloader


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text

    if url(message):
        data = insta_downloader(message)

        if data:
            await update.message.reply_video(
                video=data,
                caption='📌 <b>@instagraam_savve_bot</b>',
                parse_mode='HTML'
            )
        else:
            await update.message.reply_html(
                text="❌ Video yiklashda xatolik",
            )
    else:
        await update.message.reply_html(
            text="❌ Manzil xato yuborildi"
        )
