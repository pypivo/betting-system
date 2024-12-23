from enum import Enum


class EventStatus(str, Enum):
    UNCOMPLETED = "uncompleted"
    FIRST_WIN = "first_win"
    SECOND_WIN = "second_win"
