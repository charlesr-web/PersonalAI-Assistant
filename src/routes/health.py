from fastapi import APIRouter
from src.services.notion_service import fetch_tasks
from src.config import NOTION_RECURRING_TASKS_DB_ID

router = APIRouter()


@router.get("/health")
def health_check():
    """
    Enhanced health check endpoint
    """
    health = {"status": "running", "notion_connected": False, "env_loaded": False}

    # Check environment variables
    if NOTION_RECURRING_TASKS_DB_ID:
        health["env_loaded"] = True

    # Test Notion connectivity
    try:
        test_data = fetch_tasks(NOTION_RECURRING_TASKS_DB_ID, {"name": "Name"})
        health["notion_connected"] = True if test_data else False
    except Exception as e:
        health["notion_connected"] = False

    return health
