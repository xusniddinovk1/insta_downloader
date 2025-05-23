from telegram.error import BadRequest
from database import Database
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from validators import url
from checking import check_user
from downloader import insta_downloader

db = Database('insta_save.db')


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    user = update.effective_user

    if context.user_data['state'] == 'ADMIN':
        if message == "➕ Kanal qo'shish":
            pass
        elif message == "✔️ Reklama qo'shish":
            pass
        elif message == "❌ Chiqish":
            pass
    else:
        if not user:
            await update.message.reply_text("Foydalanuvchi aniqlanmadi.")
            return

        delete_message = await update.message.reply_text("⌛")

        # check user
        check_user(user)

        # check channels
        channels = db.get_channels()
        channel_status = []
        channel_buttons = []
        for i in channels:
            try:
                i = dict(i)

                channel_link = i.get('link')
                if not channel_link.startswith("@"):
                    channel_link = f"@{channel_link}"

                # inline keyboard
                channel_buttons.append(
                    [InlineKeyboardButton(
                        text=f"📌 Kanalimizga obuna bo'ling {i.get('name')}",
                        url=f"https://t.me/{channel_link[1:]}"
                    )]
                )

                chat_member = await context.bot.get_chat_member(channel_link, user.id)

                status = chat_member.status
                channel_status.append(status.lower())
                print(f'Status: {status}')
            except BadRequest as e:
                print(f'Error: {str(e)}')
            except Exception as e:
                print(f'Error: {str(e)}')

        print(channel_status)
        if any(status == "left" for status in channel_status):
            if delete_message:
                await delete_message.delete()
            await update.message.reply_html(
                text="Kanalimizga obuna bo'ling",
                reply_markup=InlineKeyboardMarkup(channel_buttons)
            )
        else:
            # check message
            if url(message):
                try:
                    data = insta_downloader(message)

                    # return video
                    if data:
                        await delete_message.delete()
                        await update.message.reply_video(
                            video=data,
                            caption='📌 <b>@instagraam_savve_bot</b>',
                            parse_mode='HTML'
                        )
                    else:
                        await delete_message.delete()
                        await update.message.reply_html(
                            text="❌ Video yiklashda xatolik",
                        )
                except:
                    await delete_message.delete()
                    await update.message.reply_html(
                        text="❌ Video yiklashda xatolik",
                    )
            else:
                await delete_message.delete()
                await update.message.reply_html(
                    text="❌ Manzil xato yuborildi"
                )
