from Crypto.Util.number import getPrime, getRandomNBitInteger, isPrime
from math import gcd


class GenerateParameters:
    def __init__(self, length):
        self.length = length

    @staticmethod
    def extended_gcd(a, b):
        prev_x, x = 1, 0
        prev_y, y = 0, 1

        while b:
            q = int(a // b)
            x, prev_x = int(prev_x - int(q * x)), x
            y, prev_y = int(prev_y - int(q * y)), y
            a, b = b, int(a % b)

        return int(a), int(prev_x), int(prev_y)

    def generate_parameters(self):
        #while True:
        #    # Generate large prime p and q.
        #    p = getPrime(self.length // 2)
        #    q = getPrime(self.length // 2)
        #    while q == p:
        #        q = getPrime(self.length // 2)
#
        #    # Calculate n and phi(n)
        #    n = p * q
#
        #    if n.bit_length() == self.length:
        #        break

        while True:
            k = getPrime(self.length // 2)
            g = getPrime(self.length // 2)
            if k == g:
                continue

            p = 2*k + 1
            q = 2*g + 1

            if isPrime(p) and isPrime(q):
                n = p * q

                #if n.bit_length() == self.length:
                break

        euler_func = (p - 1) * (q - 1)

        while True:
            # Generate public key.
            # Public key must be coprime with phi(n)
            # Let public key be small, b'coz we need strong private key
            e = getPrime(self.length // 8)
            while gcd(e, euler_func) != 1:
                e = getPrime(self.length // 4)

            for i in range(1, 16):
                if pow(e, i, euler_func) == 1:
                    break
            else:
                break
            continue

        # Let's calculate d with extended gcd:
        # extended gcd give us gcd, x and y:
        # gcd(e, phi(n)) => e * x + phi(n) * y = 1
        # e * x + phi(n) * y = 1 => e * x = 1 (mod phi(n)) => x = d
        check, d, y = self.extended_gcd(e, euler_func)
        if check != 1:
            print("ERROR: gcd(e, phi(n)) != 1")

        if d < 0:
            d += euler_func

        return n, int(e), int(d)
