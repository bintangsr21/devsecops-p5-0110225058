from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    priority: str = "medium"
    done: bool = False
    created_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat(timespec="seconds")

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return Task(**data)