import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("🗣 History Taking", callback_data="history"),
        ],
        [
            InlineKeyboardButton("🏥 Clinical Cases", callback_data="cases"),
        ],
        [
            InlineKeyboardButton("📝 MCQs Practice", callback_data="mcq"),
        ],
        [
            InlineKeyboardButton("📊 My Progress", callback_data="progress"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🩺 Welcome to MedMRCP AI\n\n"
        "Choose your training mode:",
        reply_markup=reply_markup
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "history":
        text = "🗣 History Taking Training\n\nComing soon..."

    elif query.data == "cases":
        text = "🏥 Clinical Cases\n\nComing soon..."

    elif query.data == "mcq":
        text = "📝 MCQs Practice\n\nComing soon..."

    elif query.data == "progress":
        text = "📊 Your Progress\n\nComing soon..."

    await query.edit_message_text(text)


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
