import math
import random
import sys
from Crypto.Util.number import getPrime, inverse, getRandomNBitInteger
from math import gcd


class WienersAttack:
    def __init__(self, n, e):
        self.n = n
        self.e = e

    @staticmethod
    def wieners_attack_get_params():
        if len(sys.argv) == 1:
            n = int(input("n:"))
            e = int(input("e:"))
        else:
            n = sys.argv[1]
            e = sys.argv[2]

        return n, e

    @staticmethod
    def get_continued_fraction(top, bottom):
        a_list = []

        while bottom != 0:
            a = top // bottom
            b = top % bottom
            a_list.append(a)
            top, bottom = bottom, b

        return a_list

    def calculate_d(self, list_a):
        P = {-1: 1,
             0: 0}

        Q = {-1: 0,
             0: 1}

        for i in range(1, len(list_a)):
            P[i] = list_a[i]*P[i - 1] + P[i - 2]
            Q[i] = list_a[i]*Q[i - 1] + Q[i - 2]

            m = random.randint(1, self.n)

            if pow(pow(m, self.e, self.n), Q[i], self.n) == m:
                return Q[i]

    def start_alg(self):
        list_a = self.get_continued_fraction(self.e, self.n)

        return self.calculate_d(list_a)

    @staticmethod
    def gen_params(length):
        q = getPrime(length)

        p = getPrime(length)
        while (not p > q) and (not p < 2*q):
            p = getPrime(length)

        n = p * q
        euler_func = (p - 1)*(q - 1)

        while True:
            while True:
                d = getRandomNBitInteger(length // 4)
                if gcd(d, euler_func) == 1 and pow(3 * d, 4) < n:
                    break

            e = inverse(d, euler_func)
            if gcd(e, euler_func) == 1:
                break

        return n, e, d
