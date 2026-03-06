import math


def character_pool_size(password):
    pool = 0

    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(not c.isalnum() for c in password):
        pool += 32

    return pool


def calculate_entropy(password):
    pool = character_pool_size(password)
    length = len(password)

    if pool == 0:
        return 0

    entropy = length * math.log2(pool)
    return entropy