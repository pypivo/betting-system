from enum import Enum


class EventStatus(str, Enum):
    UNCOMPLETED = "uncompleted"
    FIRST_WIN = "first_win"
    SECOND_WIN = "second_win"


class BetStatus(str, Enum):
    UNCOMPLETED = "uncompleted"
    WIN = "win"
    LOSE = "lose"