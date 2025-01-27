# from Crypto.Util.number import bytes_to_long
from a import bytes_to_long
from sage.all import *

class RNG:

    def __init__(self, seed):
        self.p = next_prime(2**24)
        self.F = GF(self.p)
        print([bytes_to_long(seed[i:i+3]) for i in range(0, len(seed), 3)])
        self.M = matrix(self.F, 3,3, [bytes_to_long(seed[i:i+3]) for i in range(0, len(seed), 3)])
        self.state = vector(self.F, map(ord, "Mvm"))
        self.gen = self.F(2)
        print(self.p)
        print("F: ", self.F)
        print(self.M)
        print("state: ", self.state)
        print(self.gen)

    def get_random_num(self):
        print("gen ---------")
        print(self.M)
        print(self.state)
        out = self.M * self.state
        print(out)
        print("en -----")
        print(self.state)
        for i in range(len(self.state)):
            self.state[i] = self.gen**self.state[i]

        print(self.state)
        print("ve -----")

        print(out * self.state)
        print("end gen gen ---------")
        print(out * self.state)
        return out * self.state


flag = b"MVM{???????????????????????????}"

flag = b"MVM{l1n34r_fuNcT10n5_4r3_my_f4v}"
l1n34r_fuNcT10n5_4r3_my_f4v



seed = flag[4:-1]

rng = RNG(seed)
samples = []

# for i in range(255):
#     for j in range(255):
#         for k in range(255):
#             print(bytes([i,j,k]))

for i in range(9):
    samples.append(rng.get_random_num())

print(f"{samples = }")
# samples = [6192533, 82371, 86024, 4218430, 12259879, 16442850, 6736271, 7418630, 15483781]
