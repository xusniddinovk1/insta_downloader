from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.error import BadRequest
from database import Database

db = Database('insta_save.db')

async def check_channel_membership(update: Update, context: ContextTypes.DEFAULT_TYPE, user) -> bool:
    channels = db.get_channels()
    channel_status = []
    channel_buttons = []

    for i in channels:
        try:
            i = dict(i)
            link = i.get('link')
            if not link.startswith("@"):
                link = f"@{link}"

            channel_buttons.append([
                InlineKeyboardButton(
                    text=f"📌 Kanalimizga obuna bo'ling {i.get('name')}",
                    url=f"https://t.me/{link[1:]}"
                )
            ])

            member = await context.bot.get_chat_member(link, user.id)
            channel_status.append(member.status.lower())

        except BadRequest as e:
            print(f'BadRequest: {e}')
        except Exception as e:
            print(f'Error: {e}')

    if any(status == 'left' for status in channel_status):
        await update.message.reply_html(
            "Kanalimizga obuna bo'ling",
            reply_markup=InlineKeyboardMarkup(channel_buttons)
        )
        return False

    return True
