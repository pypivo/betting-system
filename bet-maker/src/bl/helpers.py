from src.common.enums import EventStatus, BetStatus

def map_event_status_to_bet_status(event_status: EventStatus) -> BetStatus:
    if event_status == EventStatus.UNCOMPLETED:
        return BetStatus.UNCOMPLETED
    elif event_status == EventStatus.FIRST_WIN:
        return BetStatus.WIN
    else:
        return BetStatus.LOSE
