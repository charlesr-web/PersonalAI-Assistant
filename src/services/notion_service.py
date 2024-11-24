from notion_client import Client
from src.config import NOTION_API_KEY

notion = Client(auth=NOTION_API_KEY)


def fetch_tasks(database_id, property_map):
    """
    Fetch tasks from a specified Notion database.
    Args:
        database_id (str): The ID of the Notion database to query.
        property_map (dict): A mapping of task properties to database column names.
    Returns:
        list[dict]: A list of tasks with their properties.
    """
    try:
        response = notion.databases.query(database_id=database_id)
        tasks = []

        for result in response.get("results", []):
            task = {}
            for key, column in property_map.items():
                # Check if the column exists in the result properties
                value = result["properties"].get(column, {})

                # Handle different property types
                if value.get("title"):
                    task[key] = (
                        value["title"][0]["plain_text"]
                        if value["title"]
                        else "Untitled Task"
                    )
                elif value.get("date"):
                    task[key] = value["date"]["start"] if value["date"] else None
                elif value.get("select"):
                    task[key] = value["select"]["name"] if value["select"] else None
                elif value.get("multi_select"):
                    task[key] = [option["name"] for option in value["multi_select"]]
                elif value.get("rich_text"):
                    task[key] = (
                        value["rich_text"][0]["plain_text"]
                        if value["rich_text"]
                        else None
                    )
                else:
                    # Provide a default value if the property is missing or unsupported
                    task[key] = None
            tasks.append(task)

        return tasks
    except Exception as e:
        print(f"Error fetching tasks: {e}")
        return []
