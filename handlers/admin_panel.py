from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from database import Database

db = Database('insta_save.db')


async def handle_admin_state(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    state = context.user_data.get('state')

    if state == 'ADMIN_HOME':
        if message == "➕ Kanal qo'shish":
            context.user_data['state'] = 'ADMIN_CHANNEL'
            await update.message.reply_text("Kanal qo'shish uchun namuna\n\nPython Sources++@python_sources1")
        elif message == "✔️ Reklama qo'shish":
            context.user_data['state'] = 'ADMIN_ADS'
            await update.message.reply_text("Reklama matnini kiriting")
        elif message == "❌ Chiqish":
            del context.user_data['state']
            await update.message.reply_text("Siz admin paneldan chiqdingiz", reply_markup=ReplyKeyboardRemove())
        return True

    elif state == "ADMIN_CHANNEL":
        data = message.split('++')
        if len(data) == 2:
            try:
                status = await context.bot.get_chat_member(chat_id=data[-1], user_id=context.bot.id)
                if "Administrator" in status.status.title():
                    db.create_channel(name=data[0], link=data[1])
                    context.user_data['state'] = 'ADMIN_HOME'
                    await update.message.reply_text(
                        text=f"{data[0]} qo'shildi",
                        reply_markup=ReplyKeyboardMarkup([
                            [KeyboardButton("➕ Kanal qo'shish"), KeyboardButton("✔️ Reklama qo'shish")],
                            [KeyboardButton("❌ Chiqish")]
                        ], resize_keyboard=True)
                    )
            except:
                await update.message.reply_html("❌ Botni admin qiling!")
        return True

    elif state == "ADMIN_ADS":
        users = db.get_users()
        k = 0
        for user in users:
            try:
                await context.bot.send_message(chat_id=user.get('chat_id'), text=message, parse_mode='HTML')
                k += 1
            except:
                print('Error')
        context.user_data['state'] = "ADMIN_HOME"
        await update.message.reply_text(f"Reklama {k} ta foydalanuvchiga jo'natildi")
        return True

    return False
