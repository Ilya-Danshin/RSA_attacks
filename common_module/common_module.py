import random
import sys
from Crypto.Util.number import getPrime, getRandomNBitInteger, inverse
from math import gcd


class CommonModuleAlg:
    def __init__(self, n, e_b, d_b, e_a):
        self.n = n
        self.e_b = e_b
        self.d_b = d_b
        self.e_a = e_a

    @staticmethod
    def common_module_alg_get_params():
        if len(sys.argv) == 1:
            n = int(input("n:"))
            e_b = int(input("e_b:"))
            d_b = int(input("d_b:"))
            e_a = int(input("e_a:"))
        else:
            n, e_b, d_b, e_a = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

        return n, e_b, d_b, e_a

    @staticmethod
    def get_f_s(number):
        f = 0
        while number % 2 != 1:
            f += 1
            number //= 2

        return f, number

    def calculate_t(self, s):
        while True:
            a = random.randint(1, self.n)
            b = pow(a, s, self.n)

            if b == 1:
                continue

            b_hash_table = {0: b}

            counter = 1
            while b % self.n != 1:
                b = pow(b, 2, self.n)
                b_hash_table[counter] = b
                counter += 1

            if b_hash_table[counter-1] != (self.n - 1):
                return b_hash_table[counter-2]

    def gcd_extended(self, num1, num2):
        if num1 == 0:
            return int(num2), 0, 1
        else:
            div, x, y = self.gcd_extended(int(int(num2) % int(num1)), int(num1))

        return int(div), int(y - (int(int(num2) // int(num1))) * x), int(x)

    def start_alg(self):
        # 1. calc f, s: e_b*d_b - 1 = (2**d)*s
        f, s = self.get_f_s(self.e_b*self.d_b - 1)
        # 3.
        t = self.calculate_t(s)
        # 4. p = GCD(t + 1, n) q = GCD(t - 1, n)
        p = gcd(t + 1, self.n)
        q = gcd(t - 1, self.n)

        euler_func = (p - 1)*(q - 1)
        d_a = inverse(self.e_a, euler_func)

        if d_a < 0:
            d_a += euler_func

        return (p, q), d_a

    @staticmethod
    def gen_params(length):
        p = getPrime(length)
        q = getPrime(length)
        while p == q:
            q = getPrime(length)

        n = p * q
        euler_func = (p - 1)*(q - 1)
        e_b = getRandomNBitInteger(length // 2)
        while gcd(e_b, euler_func) != 1:
            e_b = getRandomNBitInteger(length // 2)

        d_b = inverse(e_b, euler_func)

        e_a = getRandomNBitInteger(length // 2)
        while e_a == e_b:
            e_a = getRandomNBitInteger(length // 2)

        d_a = inverse(e_a, euler_func)

        return p, q, n, e_b, d_b, e_a, d_a
