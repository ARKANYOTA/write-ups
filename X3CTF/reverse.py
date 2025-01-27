from a import bytes_to_long
from sage.all import *

p = next_prime(2**24)
F = GF(p)
S = vector(F, map(ord, "Mvm"))
B = matrix(F, 9,9, [0]*9*9)
A = [[0]*9 for i in range(9)]
print(A)
gen = F(2)

for i in range(9):
    print("en ------------")
    A[i][0] = S[0]
    A[i][1] = S[1]
    A[i][2] = S[2]
    A[i][3] = S[0]
    A[i][4] = S[1]
    A[i][5] = S[2]
    A[i][6] = S[0]
    A[i][7] = S[1]
    A[i][8] = S[2]
    print(S)

    for j in range(len(S)):
        S[j] = gen**S[j]

    A[i][0] *= S[0]
    A[i][1] *= S[0]
    A[i][2] *= S[0]
    A[i][3] *= S[1]
    A[i][4] *= S[1]
    A[i][5] *= S[1]
    A[i][6] *= S[2]
    A[i][7] *= S[2]
    A[i][8] *= S[2]
    print(S)

    print("vm ------------")

print(A)
C = matrix(F, 9,9, A)

print(C)

print(C.det())
print("inversematrix")
print(C.inverse())

print("result")

print(C.inverse() * vector(F, [6192533, 82371, 86024, 4218430, 12259879, 16442850, 6736271, 7418630, 15483781]))

print("endinv")
print(C * vector(F, [11144394, 16776215, 1555054, 3471308, 1510282, 12133261, 829684, 7548780, 13046208]))

flag = b"MVM{???????????????????????????}"
seed = flag[4:-1]

flag = vector(F, [bytes_to_long(seed[i:i+3]) for i in range(0, len(seed), 3)])
print(flag)

print("rese: ", C * flag)


class RNG:

    def __init__(self, seed):
        self.p = next_prime(2**24)
        self.F = GF(self.p)
        # self.M = matrix(self.F, 3,3, [bytes_to_long(seed[i:i+3]) for i in range(0, len(seed), 3)])
        self.state = vector(self.F, map(ord, "Mvm"))
        self.gen = self.F(2)
        print(self.p)
        print("F: ", self.F)
        print("state: ", self.state)
        print(self.gen)

    def get_random_num(self):
        print("gen ---------")
        print(self.state)
        # out = self.M * self.state

        for i in range(len(self.state)):
            self.state[i] = self.gen**self.state[i]

        print("end gen gen ---------")
        # return out * self.state
        return self.state


# for i in range(255):
#     for j in range(255):
#         for k in range(255):
#             print(bytes([i,j,k]))
# 
#             rng = RNG(seed)
#             if 6192533 == rng.get_random_num():
#                 print(i,j,k)
            


rng = RNG(b"???")

print(rng.get_random_num())