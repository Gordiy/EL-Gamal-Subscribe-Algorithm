def is_prime(num: int) -> bool:
    """
    Check if number is prime

    :param num: number for checking
    :return: True if the number is prime else False.
    """
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
