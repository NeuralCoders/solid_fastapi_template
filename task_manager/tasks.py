from typing import List
from schemas.models import Task
from loggers.interfaces import LoggerInterface


class MemoryTaskManager:

    def __init__(self, logs: LoggerInterface):
        self._tasks: List[Task] = []
        self._current_id: int = 1
        self._logger = logs

    def save(self, task: Task) -> Task:
        task.id = self._current_id
        self._current_id += 1
        self._tasks.append(task)
        self._logger.info(f"Task saved: {task.title}")
        return task
