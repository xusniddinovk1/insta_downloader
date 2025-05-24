from telegram import Update
from telegram.ext import ContextTypes
from validators import url
from downloader import insta_downloader

async def handle_instagram_download(update: Update, context: ContextTypes.DEFAULT_TYPE, message: str, delete_message):
    if url(message):
        try:
            data = insta_downloader(message)
            if data:
                await delete_message.delete()
                await update.message.reply_video(
                    video=data,
                    caption='📌 <b>@instagraam_savve_bot</b>',
                    parse_mode='HTML'
                )
            else:
                await delete_message.delete()
                await update.message.reply_html("❌ Video yuklashda xatolik")
        except:
            await delete_message.delete()
            await update.message.reply_html("❌ Video yuklashda xatolik")
    else:
        await delete_message.delete()
        await update.message.reply_html("❌ Manzil xato yuborildi")
