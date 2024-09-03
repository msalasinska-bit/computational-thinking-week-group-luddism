from datetime import datetime

def solution_station_2(date_str):
    # Convert the input string to a datetime object
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Get the day of the week as an integer (Monday is 0 and Sunday is 6)
    day_of_week = date.weekday()

    # Map the weekday to the Japanese name
    japanese_days = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    
    # Return the Japanese day of the week, adjusting for Sunday which is 6
    return japanese_days[day_of_week] if day_of_week < 6 else "日曜日"
