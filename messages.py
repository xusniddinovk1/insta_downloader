from telegram import Update
from telegram.ext import ContextTypes
from validators import url
from downloader import insta_downloader


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    if url(text):
        data = insta_downloader(text)

        delete_message = await update.message.reply_text(text="⏳")

        if data:
            await delete_message.delete()

            await update.message.reply_video(
                video=data,
                caption="<b> @instagram_downnloadeer_bot </b>",
                parse_mode = "HTML"
            )

        else:
            await delete_message.delete()
            await update.message.reply_html(
                text="❌ Video yuklashda xatolik"
            )
    else:
        await update.message.reply_html(
            text="❌ Manzil xato yuborildi"
        )
