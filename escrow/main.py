import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import BOT_TOKEN

# Import handlers
from handlers.start_handler import deal_command
from handlers.role_handler import handle_role_selection
from handlers.deal_handler import handle_deal_form
from handlers.fee_handler import handle_fee_selection
from handlers.confirm_handler import handle_confirmation
from handlers.dispute_handler import dispute_command

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("deal", deal_command))
    application.add_handler(CommandHandler("dispute", dispute_command))
    application.add_handler(CallbackQueryHandler(handle_role_selection, pattern="^role_"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_deal_form))
    application.add_handler(CallbackQueryHandler(handle_fee_selection, pattern="^fee_"))
    application.add_handler(CallbackQueryHandler(handle_confirmation, pattern="^confirm_"))
    
    # Start the bot
    logger.info("escrow bot v1 starting... started successfully! @eternalaura")
    application.run_polling()

if __name__ == "__main__":
    main()
