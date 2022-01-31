from utils import generate_random_prime_num, is_coprime
from Crypto.Util.number import inverse


class ElGamalSubscription:
    def __init__(self, p: int, g: int, x: int) -> None:
        """
        El Gamal Subscription Algorithm.

        :param p: random prime value, open key
        :param g: one of primitive root p, open key
        :param x: random integer value in range from 1 to p-1 (1 < x < p -1), close key
        """
        self.p = p
        self.g = g
        self.x = x
        self.y = pow(self.g, self.x, self.p) # open key
        self.k = None
        self.r = None

    def __generate_k(self):
        prime_numbers = generate_random_prime_num(1, self.p-1)
        for num in prime_numbers:
            if is_coprime(num, self.p-1):
                self.k = num
                break

    def __generate_r(self):
        self.r = pow(self.g, self.k, self.p)

    def __generate_sign(self, m: int):
        l = inverse(self.k, self.p-1)
        return l*(m - self.x * self.r) % (self.p - 1)
        

    def subscribe(self, msg: int) -> tuple:
        """
        Subscribe message.
        :param msg: ShaSum message.
        :return: the signature of the message msg is the pair (r,s)
        """
        self.__generate_k()
        self.__generate_r()
        return (self.r, self.__generate_sign(msg))


el_gamal = ElGamalSubscription(23, 5, 7)
print(el_gamal.subscribe(3))
