from dotenv import load_dotenv
import os

load_dotenv()

# Notion API Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_RECURRING_TASKS_DB_ID = os.getenv("NOTION_RECURRING_TASKS_DB_ID")
NOTION_MISC_TASKS_DB_ID = os.getenv("NOTION_MISC_TASKS_DB_ID")
