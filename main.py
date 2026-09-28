import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8948727654:AAGgAsVBYmU70kvNnhnJkx0XZTOyW0KyvOE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('تم تفعيل التحكم. أرسل الأوامر الآن.')

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text
    response = f"تم تنفيذ الأمر: {command}"
    await update.message.reply_text(response)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", handle_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
