import math

def is_coprime(x: int or float, y: int or float) -> bool:
    "Check if numbers is corprime."
    return math.gcd(x, y) == 1
