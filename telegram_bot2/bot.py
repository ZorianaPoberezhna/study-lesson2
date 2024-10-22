import json
import os
import logging
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

TOKEN_BOT = "7434668199:AAEPBarrs467SYWSO5U4EhH-gzyAfFkLzv0"
DATA_FILE = "data.json"
categories = ["Food", "Transport", "Entertainment", "Health", "Utilities", "Gifts", "Clothes", "Education"]

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_data():
        with open(DATA_FILE, "w") as file:
            json.dump(user_data, file , indent=4)

user_data = load_data()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: CallbackContext) -> None:
    logging.info('Command "start" was triggered!')
    await update.message.reply_text(
        "Hello! I will help you track expenses and income. Use commands:\n" 
        "Commands:\n"
        "Adding expense: /add_expense <amount> <category>\n"
        "Adding income: /add_income <amount> <category>\n"
        "List transactions: /list_transactions \n"
        "Filter transactions: /filter_transactions \n"
        "View statistics: /statistics <day|week|month|year> [category]\n"
        "Remove transaction: /remove_transaction <number>\n"
        "Clear records:/clear\n"
        "\n"
        "List categories: " + ', '.join(categories)
    )

async def add_expense(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    try:
        amount = float(context.args[0])
        category = context.args[1]
        if category not in categories:
            await update.message.reply_text(f"Wrong category! Available categories: {', '.join(categories)}")
            return
        transaction = {
            "type": "expense",
            "amount": amount,
            "category": category,
            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        if user_id not in user_data:
            user_data[user_id] = []
        user_data[user_id].append(transaction)
        save_data()
        await update.message.reply_text(f"Cost added: {amount}  to {category}")
    except (IndexError, ValueError):
        await update.message.reply_text(f"Invalid format. Using: /add_expense <amount> <category>")

async def add_income(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    try:
        amount = float(context.args[0])
        category = context.args[1]
        transaction = {
            "type": "income",
            "amount": amount,
            "category": category,
            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        if user_id not in user_data:
            user_data[user_id] = []
        user_data[user_id].append(transaction)
        save_data()
        await update.message.reply_text(f"Income added: {amount} to {category}")
    except (IndexError, ValueError):
        await update.message.reply_text(f"Invalid format. Using: /add_income <amount> <category>")

async def list_transactions(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_data or not user_data[user_id]:
        await update.message.reply_text(f"You have no transactions yet.")
        return

    result = '\n'.join([f"{i + 1}. {t['type'].upper()} | {t['amount']}  | {t['category']} | {t['date']}"
                        for i, t in enumerate(user_data[user_id])])
    await update.message.reply_text(result)

async def remove_transaction(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_data or not user_data[user_id]:
        await update.message.reply_text(f"You have no transactions to delete.")
        return
    try:
        idx = int(context.args[0]) - 1
        removed_transaction = user_data[user_id].pop(idx)
        save_data()
        await update.message.reply_text(
            f"The transaction has been deleted: {removed_transaction['type']} {removed_transaction['amount']}")
    except (IndexError, ValueError):
        await update.message.reply_text(f"Invalid index. Using: /remove_transaction <number>")

async def clear(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_data[user_id] = []
    save_data()
    await update.message.reply_text(f"Cleared successfully.")

def filter_transactions(transactions, period, category=None):
    now = datetime.now()
    if period == "day":
        time_filter = now - timedelta(days=1)
    elif period == "week":
        time_filter = now - timedelta(weeks=1)
    elif period == "month":
        time_filter = now - timedelta(days=30)
    elif period == "year":
        time_filter = now - timedelta(days=365)
    else:
        return []

    filtered = [t for t in transactions if datetime.strptime(t['date'], '%Y-%m-%d %H:%M:%S') > time_filter]
    if category:
        filtered = [t for t in filtered if t['category'].lower() == category.lower()]
        return filtered

async def filter_transactions_cmd(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_data or not user_data[user_id]:
        await update.message.reply_text(f"You have no transactions yet.")
        return
    try:
        period = context.args[0]
        category = context.args[1] if len(context.args) > 1 else None
        filtered = filter_transactions(user_data[user_id], period, category)
        if not filtered:
            await update.message.reply_text(f"No transactions were found for the specified parameters.")
            return
        result = '\n'.join([f"{i + 1}. {t['type'].upper()} | {t['amount']} | {t['category']} | {t['date']}"
                            for i, t in enumerate(filtered)])
        await update.message.reply_text(result)
    except (IndexError, ValueError):
        await update.message.reply_text(
            f"Invalid index. Using: /filter_transactions <day|week|month|year> [category]")

def calculate_statistics(transactions):
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    return total_income, total_expense

async def statistics(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_data or not user_data[user_id]:
        await update.message.reply_text(f"You have no transactions yet.")
        return
    try:
        period = context.args[0]
        category = context.args[1] if len(context.args) > 1 else None
        filtered = filter_transactions(user_data[user_id], period, category)
        if not filtered:
            await update.message.reply_text(f"No transactions were found for the specified parameters.")
            return
        total_income, total_expense = calculate_statistics(filtered)
        await update.message.reply_text(f"Statistics for {period}:\n"
                                        f"Income: {total_income} \n"
                                        f"Expense: {total_expense}\n"
                                        f"Balance: {total_income - total_expense}")
    except (IndexError, ValueError):
        await update.message.reply_text(f"Invalid index. Using: /statistics <day|week|month|year> [category]")

def run():
    app = ApplicationBuilder().token(TOKEN_BOT).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add_expense", add_expense))
    app.add_handler(CommandHandler("add_income", add_income))
    app.add_handler(CommandHandler("list_transactions", list_transactions))
    app.add_handler(CommandHandler("remove_transaction", remove_transaction))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(CommandHandler("filter_transactions", filter_transactions_cmd))
    app.add_handler(CommandHandler("statistics", statistics))

    app.run_polling()

if __name__ == '__main__': run()







