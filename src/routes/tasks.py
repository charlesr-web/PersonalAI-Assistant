from fastapi import APIRouter
from src.config import NOTION_RECURRING_TASKS_DB_ID, NOTION_MISC_TASKS_DB_ID
from src.services.notion_service import fetch_tasks

router = APIRouter()


@router.get("/tasks/recurring")
def get_recurring_tasks():
    """
    Fetch and prioritize tasks from the Recurring Tasks database.
    """
    property_map = {
        "name": "Task Name",
        "due_date": "Next Due Date",
        "frequency": "Frequency",
    }
    tasks = sorted(
        fetch_tasks(NOTION_RECURRING_TASKS_DB_ID, property_map),
        key=lambda x: x["due_date"],
    )
    return {"recurring_tasks": tasks}


@router.get("/tasks/misc")
def get_misc_tasks():
    """
    Fetch and return miscellaneous tasks from the Misc Tasks database.
    """
    property_map = {"name": "Task Name", "category": "Category"}
    tasks = fetch_tasks(NOTION_MISC_TASKS_DB_ID, property_map)
    return {"misc_tasks": tasks}
