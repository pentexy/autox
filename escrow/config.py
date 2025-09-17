import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
LOG_GROUP_ID = os.getenv('LOG_GROUP_ID')  # Private group for logging

# Fee configuration
ESCROW_FEE_PERCENTAGE = 1.0
