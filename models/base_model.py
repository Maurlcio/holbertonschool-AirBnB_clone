#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now
        self.update_at = datetime.now

    def __str__(self):
        return (f"{self.__class__.__name__}, {self.id}, {self.__dict__}")

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "update_at": self.update_at.isoformat()
        }