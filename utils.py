from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculate(start_date, periods, start_amount, rate):
    data = {}
    current_amount = start_amount * (1 + rate / 12 / 100)
    for i in range(1, periods + 1):
        current_date = (start_date + relativedelta(months=i)).strftime("%d.%m.%Y")
        current_date = str(current_date)
        data[current_date] = round(current_amount, 2)
        current_amount *= (1 + rate / 12 / 100)
    return data


def convert_date(date_str):
    year, month, day = date_str.split("-")
    formatted_date = f"{day}.{month}.{year}"
    date = datetime.strptime(formatted_date, "%d.%m.%Y")
    return date


def validate_data(periods, amount, rate):
    if periods < 1 or periods > 60:
        return "Invalid period"
    if amount < 10000 or amount > 3000000:
        return "Invalid amount"
    if rate < 1 or rate > 8:
        return "Invalid rate"
    return "ok"
