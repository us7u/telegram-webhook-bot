import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = "8948727654:AAGgAsVBYmU70kvNnhnJkx0XZTOyW0KyvOE"

app = Flask(__name__)
bot_app = Application.builder().token(TOKEN).build()

async def start(update: Update, context):
    await update.message.reply_text('تم تفعيل التحكم. أرسل الأوامر الآن.')

async def handle_command(update: Update, context):
    command = update.message.text
    await update.message.reply_text(f"تم تنفيذ الأمر: {command}")

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("help", handle_command))

@app.route('/webhook', methods=['POST'])
async def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot_app.bot)
        await bot_app.process_update(update)
        return 'ok', 200

@app.route('/')
def index():
    return "Server is running!"

if __name__ == '__main__':
    bot_app.initialize()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
