from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Bu yerda real indikatorlar o‘rniga misol yozilgan
    message_uz = (
        "📊 Trend: Yuqoriga (Bullish)\n"
        "📈 RSI: 58\n"
        "🧭 Qo‘llab-quvvatlash: 3220\n"
        "🔺 Qarshilik: 3245\n"
        "🇺🇿 Bozor yuqoriga harakatlanmoqda."
    )

    message_en = (
        "📊 Trend: Upward (Bullish)\n"
        "📈 RSI: 58\n"
        "🧭 Support: 3220\n"
        "🔺 Resistance: 3245\n"
        "🇬🇧 The market is trending upward."
    )

    await update.message.reply_text(message_uz + "\n\n" + message_en)

if __name__ == '__main__':
    import os
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("signal", signal))
    app.run_polling()
  
