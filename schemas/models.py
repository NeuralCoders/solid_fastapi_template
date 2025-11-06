from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=3, max_length=100)
    priority: str = TaskPriority

    @field_validator("priority")
    def validate_priority(cls, priority):
        if priority not in [
            TaskPriority.LOW,
            TaskPriority.MEDIUM,
            TaskPriority.HIGH
        ]:
            raise ValueError("Priority must be one of low, medium, high")
        return priority
