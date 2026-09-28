import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8948727654:AAGgAsVBYmU70kvNnhnJkx0XZTOyW0KyvOE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('تم تفعيل التحكم. أرسل الأوامر أو أي رسالة الآن.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = f"تم استلام رسالتك: {user_text}"
    await update.message.reply_text(response)

def main():
    application = Application.builder().token(TOKEN).build()
    
    # معالج أمر /start
    application.add_handler(CommandHandler("start", start))
    
    # معالج لجميع النصوص العادية (مثل مرحبا وغيرها)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
