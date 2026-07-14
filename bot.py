import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)

from handlers.chat import handle_message


TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("❤️ Cardiovascular", callback_data="cardio")],
        [InlineKeyboardButton("🫁 Respiratory", callback_data="respiratory")],
        [InlineKeyboardButton("🧠 Neurology", callback_data="neurology")],
        [InlineKeyboardButton("🍽 Gastrointestinal", callback_data="gi")],
        [InlineKeyboardButton("🫘 Renal", callback_data="renal")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome to MedMRCP AI 🩺\nChoose a system:",
        reply_markup=reply_markup
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "cardio":
        await query.edit_message_text(
            "❤️ Cardiovascular\n\nChoose training:",
        )

    elif query.data == "respiratory":
        await query.edit_message_text(
            "🫁 Respiratory selected"
        )

    elif query.data == "neurology":
        await query.edit_message_text(
            "🧠 Neurology selected"
        )

    elif query.data == "gi":
        await query.edit_message_text(
            "🍽 Gastrointestinal selected"
        )

    elif query.data == "renal":
        await query.edit_message_text(
            "🫘 Renal selected"
        )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    app.add_handler(
        MessageHandler(filters.TEXT, handle_message)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
