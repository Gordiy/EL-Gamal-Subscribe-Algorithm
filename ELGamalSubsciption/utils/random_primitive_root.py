from random import randint


def _gcd(a: int,b: int) -> int:
    """Compute the greatest common divisor of a and b"""
    while b != 0:
        a, b = b, a % b
    return a


def random_primitive_root(modulo: int) -> int:
    """
    Get random primitive root.

    :param modulo:
    :return:
    """
    p_root = []
    required_set = set(num for num in range (1, modulo) if _gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            p_root.append(g)

    return p_root[randint(0, len(p_root)-1)]
