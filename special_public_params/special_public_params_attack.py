from Crypto.Util.number import getPrime, getRandomNBitInteger, getRandomRange
from math import gcd


class SpecialPublicParamsAttack:
    def __init__(self, n, e, c):
        self.n = n
        self.e = e
        self.c = c

    @staticmethod
    def special_public_params_get_params():
        n = int(input("n:"))
        e = int(input("e:"))
        c = int(input("c:"))

        return n, e, c

    def start_alg(self):
        c_i = self.c
        counter = 1

        while True:
            c_prev = c_i
            c_i = pow(c_i, self.e, self.n)
            counter += 1
            if c_i == self.c:
                return c_prev, counter

        return

    @staticmethod
    def gen_params(length):
        p = getPrime(length)
        q = getPrime(length)
        while p == q:
            q = getPrime(length)

        n = p * q
        euler_func = (p - 1) * (q - 1)
        e = getPrime(length) % euler_func
        while gcd(e, euler_func) != 1:
            e = getPrime(length)

        # Get open text
        m = getRandomNBitInteger(length) % n
        # Get cipher text
        c = pow(m, e, n)

        return n, e, m, c




