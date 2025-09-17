from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.formatter import format_deal_preview, bold, code, italic

async def handle_deal_form(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    deal = active_deals.get(chat_id)
    
    if not deal or not deal.buyer or not deal.seller:
        await update.message.reply_text(
            "❌ Please set both roles first with /deal",
            parse_mode='HTML'
        )
        return
    
    try:
        parts = update.message.text.split(':', 2)
        quantity = float(parts[0].strip())
        rate = float(parts[1].strip())
        condition = parts[2].strip()
        
        deal.quantity = quantity
        deal.rate = rate
        deal.condition = condition
        
        keyboard = [
            [InlineKeyboardButton("💳 I will pay the fees (Buyer)", callback_data="fee_buyer")],
            [InlineKeyboardButton("➗ Split Fees 50/50", callback_data="fee_split")]
        ]
        
        preview = format_deal_preview(quantity, rate, condition)
        message = f"""
{preview}

🏷️ {bold('Escrow Fee Selection')}
A 1% escrow fee will be applied. Who will pay the fee?
"""
        
        await update.message.reply_text(
            message,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='HTML'
        )
        
    except (ValueError, IndexError):
        await update.message.reply_text(
            f"""
❌ {bold('Invalid Format')}

Please use the format: {code('quantity : rate : condition')}

{italic('Example:')} {code('100 : 0.85 : Brand new, sealed')}
""",
            parse_mode='HTML'
        )
