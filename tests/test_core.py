from src.my_app.core import TodoList


def test_add_task():
    todo = TodoList()
    todo.add("Купити молоко")
    assert todo.count() == 1
    assert "Купити молоко" in todo.tasks[0]["task"]


def test_add_task_with_mock_id(mocker):

    todo = TodoList()

    mocker.patch(
        "src.my_app.core.generate_id",
        return_value="mock_id_123"
    )

    todo.add("Зробити тест")

    assert todo.tasks[0]["id"] == "mock_id_123"
    assert "Зробити тест" in todo.tasks[0]["task"]


def test_clear_all_tasks():
    todo = TodoList()
    todo.add("Завдання 1")
    todo.add("Завдання 2")
    assert todo.count() == 2

    todo.clear_all()
    assert todo.count() == 0
    assert todo.tasks == []
