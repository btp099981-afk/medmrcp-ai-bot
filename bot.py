
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🩺 مرحباً بك في MedMRCP AI\n\n"
        "أنا مساعدك الطبي للتدريب على:\n"
        "• History Taking\n"
        "• Clinical Cases\n"
        "• MCQs\n\n"
        "سيتم تطويري تدريجياً 🚀"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
