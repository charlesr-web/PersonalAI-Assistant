import pytest
from src.services.notion_service import fetch_tasks


@pytest.fixture
def mock_notion_response():
    return {
        "results": [
            {
                "properties": {
                    "Name": {"title": [{"plain_text": "Test Task"}]},
                    "Next Due Date": {"date": {"start": "2024-11-30"}},
                    "Frequency": {"select": {"name": "Daily"}},
                }
            }
        ]
    }


def test_fetch_tasks_success(mocker, mock_notion_response):
    mocker.patch(
        "src.services.notion_service.notion.databases.query",
        return_value=mock_notion_response,
    )
    tasks = fetch_tasks(
        "dummy_database_id",
        {"name": "Name", "due_date": "Next Due Date", "frequency": "Frequency"},
    )
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Test Task"
    assert tasks[0]["due_date"] == "2024-11-30"
    assert tasks[0]["frequency"] == "Daily"
