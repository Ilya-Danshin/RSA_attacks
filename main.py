from common_module.common_module import CommonModuleAlg
from Wieners_attack.wieners_attack import WienersAttack
from special_public_params.special_public_params_attack import SpecialPublicParamsAttack
from generate_parameters.generate_parameters import GenerateParameters


def alg():
    while True:
        n = int(input("Alg:\n\
            1. P-1: common module attack\n\
            2. P-2: Wiener's attack\n\
            3. P-3: Special public parameters attack\n\
            4. P-4: Generate RSA parameters\n\
              \n\
            0. Exit\n"))

        if (n >= 0) and (n <= 4):
            break

    return n


def main():

    while True:
        alg_number = alg()

        if alg_number == 1:
            p, q, n, e_b, d_b, e_a, d_a = CommonModuleAlg.gen_params(256)
            print("Generated params:")
            print(f"p: {p}")
            print(f"q: {q}")
            print(f"n: {n}")
            print(f"e_b: {e_b}")
            print(f"d_b: {d_b}")
            print(f"e_a: {e_a}")
            print(f"d_a: {d_a}")

            n, e_b, d_b, e_a = CommonModuleAlg.common_module_alg_get_params()
            P_1 = CommonModuleAlg(n, e_b, d_b, e_a)
            (p, q), d_a = P_1.start_alg()

            print(f"p: {p}")
            print(f"q: {q}")
            print(f"d_a: {d_a}")
        elif alg_number == 2:
            n, e, d = WienersAttack.gen_params(256)
            print("Generated params:")
            print(f"n: {n}")
            print(f"e: {e}")
            print(f"d: {d}")

            n, e = WienersAttack.wieners_attack_get_params()
            P_2 = WienersAttack(n, e)
            d = P_2.start_alg()

            print(f"d: {d}")
        elif alg_number == 3:
            n, e, m, c = SpecialPublicParamsAttack.gen_params(16)
            print("Generated params:")
            print(f"n: {n}")
            print(f"e: {e}")
            print(f"m: {m}")
            print(f"c: {c}")

            n, e, c = SpecialPublicParamsAttack.special_public_params_get_params()
            P_3 = SpecialPublicParamsAttack(n, e, c)
            m, order = P_3.start_alg()

            print(f"encrypted m: {m}")
            print(f"ord: {order}")

        elif alg_number == 4:
            P_4 = GenerateParameters(int(input("length:")))
            n, e, d = P_4.generate_parameters()
            print(f"n: {n}")
            print(f"length: {n.bit_length()}")
            print(f"e: {e}")
            print(f"d: {d}")

        elif alg_number == 0:
            break


if __name__ == "__main__":
    main()
