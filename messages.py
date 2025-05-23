from database import Database
from telegram import Update
from telegram.ext import ContextTypes
from validators import url
from checking import check_user, check_channel
from downloader import insta_downloader

db = Database('insta_save.db')

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    user = update.effective_user

    # check user
    check_user(user)

    # check channels
    channels = db.get_channels()
    print(channels)
    channel_status = []

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
