import time
import math
from .utils import generate_id
from typing import Dict, Any


DatabaseType = Dict[str, Dict[str, Any]]


class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task_name: str):
        task = {
            "id": generate_id(),
            "task": task_name,
            "created_at": time.time()
        }
        self.tasks.append(task)

    def count(self) -> int:
        return len(self.tasks)

    def get_tasks(self, limit: int = 10):
        return self.tasks[:limit]

    def clear_all(self):
        self.tasks = []

    def __repr__(self) -> str:
        return f"<TodoList with {self.count()} tasks>"

