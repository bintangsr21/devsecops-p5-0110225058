from .models import Task
from .validators import validate_title, validate_priority


class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = storage.load()

    def _next_id(self):
        return max((t.id for t in self.tasks), default=0) + 1

    def add(self, title, priority="medium"):
        task = Task(
            id=self._next_id(),
            title=validate_title(title),
            priority=validate_priority(priority),
        )
        self.tasks.append(task)
        self.storage.save(self.tasks)
        return task

    def complete(self, task_id):
        task = self._find(task_id)
        task.done = True
        self.storage.save(self.tasks)
        return task

    def remove(self, task_id):
        task = self._find(task_id)
        self.tasks.remove(task)
        self.storage.save(self.tasks)

    def list(self, only_pending=False):
        if only_pending:
            return [t for t in self.tasks if not t.done]
        return list(self.tasks)

    def _find(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                return t
        raise KeyError(f"Tugas dengan id {task_id} tidak ditemukan")