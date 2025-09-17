from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.calculator import calculate_fees
from utils.formatter import format_fee_summary, format_confirmation_message

async def handle_fee_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    deal = active_deals.get(chat_id)
    
    if not deal or not deal.is_ready():
        await query.answer("❌ Deal not fully configured")
        return
    
    if "fee_buyer" in query.data:
        deal.fee_policy = "buyer_pays"
        await query.answer("✅ Buyer will pay fees")
    else:
        deal.fee_policy = "split"
        await query.answer("✅ Fees will be split 50/50")
    
    # Calculate fees
    fee_details = calculate_fees(deal.quantity, deal.rate, deal.fee_policy)
    
    # Show fee summary
    fee_summary = format_fee_summary(deal.quantity, deal.rate, deal.fee_policy, fee_details)
    
    keyboard = [
        [InlineKeyboardButton("✅ Buyer Confirm", callback_data="confirm_buyer")],
        [InlineKeyboardButton("✅ Seller Confirm", callback_data="confirm_seller")]
    ]
    
    confirmation_message = format_confirmation_message(deal, fee_details)
    
    await query.edit_message_text(
        fee_summary + confirmation_message,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='HTML'
    )
