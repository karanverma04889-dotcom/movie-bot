from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7863126978:AAEhaPHGKCfWu1zFsOw5aEH7_LyEb1O3PFI"

CHANNEL_LINK = "https://t.me/moviewish_710"
WEBSITE_LINK = "https://movieswish.netlify.app/"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Yes", callback_data="yes"),
            InlineKeyboardButton("No", callback_data="no")
        ]
    ]
    await update.message.reply_text(
        "You join Telegram channel?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# button handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "yes":
        keyboard = [[InlineKeyboardButton("Open Website", url=WEBSITE_LINK)]]
        await query.edit_message_text(
            "Here is your access link:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "no":
        keyboard = [[InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)]]
        await query.edit_message_text(
            "Join first Telegram channel.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
