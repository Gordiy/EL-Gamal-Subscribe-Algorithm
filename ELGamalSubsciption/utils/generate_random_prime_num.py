import math
from random import randint


def generate_random_prime_num(x: int, y: int) -> int:
    """
    Generate random prime number
    
    :param x: starting range
    :param y: ending range
    :return: random prime number in range from x to y
    """
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)

    
    return prime_list[randint(0, len(prime_list)-1)]
