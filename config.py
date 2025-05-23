import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_LIST = str(os.getenv('ADMIN_LIST')).split(',')
print(ADMIN_LIST)
