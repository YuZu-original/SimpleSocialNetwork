import datetime


def calculate_age(born: datetime.date):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
