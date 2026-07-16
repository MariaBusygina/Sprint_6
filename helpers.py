from datetime import datetime, timedelta
 
 
def get_date(days_from_now: int = 1) -> str:
    """Возвращает дату в формате дд.мм.гггг через days_from_now дней от сегодня."""
    return (datetime.now() + timedelta(days=days_from_now)).strftime("%d.%m.%Y")