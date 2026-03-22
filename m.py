   
   from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7777560572:AAHp0ecPZ9mBsXCnIYetguZgSwIwd4sfUkU"

# Welcome message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Guild TCP Bot 🔥\n"
        "Use /help to see commands"
    )

# Guild info
async def guildinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Guild Name: TCP Warriors\n"
        "Leader: Admin\n"
        "Members: 50\n"
        "Status: Active 🔥"
    )

# Guild glory bot list
async def members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Guild Members:\n"
        "1. Classy1\n"
        "2. Classy2\n"
        "3. Classy3\n"
        "4. Classy4\n"
    )

# Active Classys
async def activeClassys(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Active Classys Today 🔥\n"
        "Classy1\n"
        "Classy3\n"
        "Classy4"
    )

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/guildinfo - Show guild info\n"
        "/members - Show members list\n"
        "/activeClassys - Active Classys\n"
        "/help - All commands"
    )

# Main function
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("guildinfo", guildinfo))
app.add_handler(CommandHandler("members", members))
app.add_handler(CommandHandler("activeClassys", activeClassys))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()
