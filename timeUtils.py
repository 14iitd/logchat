from datetime import datetime

def format_time_ago(timestamp):
    if not timestamp:
        return None

    # Get the current time
    import time
    current_millis = int(round(time.time() * 1000))

    # Calculate the time difference
    time_difference = current_millis - timestamp

    # Calculate seconds, minutes, hours, days, and months difference
    seconds = time_difference/1000
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    months = days / 30

    if months >= 1:
        return f"{int(months)} months ago"
    elif days >= 1:
        return f"{int(days)} days ago"
    elif hours >= 1:
        return f"{int(hours)} hours ago"
    elif minutes >= 1:
        return f"{int(minutes)} minutes ago"
    else:
        return f"{int(seconds)} seconds ago"

# Example usage
# timestamp = "2023-12-19 00:45:19.160307"
# formatted_time_ago = format_time_ago(timestamp)
# print(formatted_time_ago)
