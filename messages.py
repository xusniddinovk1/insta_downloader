from csv import excel

from telegram import Update
from telegram.ext import ContextTypes
from validators import url
from downloader import insta_downloader


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text

    # check message
    if url(message):
        try:
            data = insta_downloader(message)

            # return video
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
        except:
            await update.message.reply_html(
                text="❌ Video yiklashda xatolik",
            )
    else:
        await update.message.reply_html(
            text="❌ Manzil xato yuborildi"
        )
