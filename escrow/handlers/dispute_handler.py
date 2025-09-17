from telegram import Update
from telegram.ext import ContextTypes
from utils.formatter import bold, code

async def dispute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    deal = active_deals.get(chat_id)
    
    if not deal:
        await update.message.reply_text(
            "❌ No active deal to dispute. Start with /deal first.",
            parse_mode='HTML'
        )
        return
    
    await update.message.reply_text(
        f"""
⚠️ {bold('Dispute Raised')}

A dispute has been raised for this deal between @{deal.buyer} and @{deal.seller}.

Moderation team has been notified and will contact both parties shortly.

Please provide any evidence or details about the dispute to the moderators.
""",
        parse_mode='HTML'
    )
