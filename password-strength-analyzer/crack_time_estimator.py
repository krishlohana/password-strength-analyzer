import math

def estimate_crack_time(entropy):
    
    guesses = 2 ** entropy
    
    guesses_per_second = 1_000_000_000  # 1 billion guesses/sec
    
    seconds = guesses / guesses_per_second

    if seconds < 60:
        return f"{round(seconds,2)} seconds"
    
    minutes = seconds / 60
    if minutes < 60:
        return f"{round(minutes,2)} minutes"
    
    hours = minutes / 60
    if hours < 24:
        return f"{round(hours,2)} hours"
    
    days = hours / 24
    if days < 365:
        return f"{round(days,2)} days"
    
    years = days / 365
    
    return f"{round(years,2)} years"