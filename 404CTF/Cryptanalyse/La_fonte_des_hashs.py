import os
import subprocess

init = "18f2048f7d4de5caabd2d0a3d23f4015af8033d46736a2e2d747b777a4d4d205"


Code = list([])#"404CTF{0000000000000000000000}")

for i in range(30):
    min_dist = 10**100
    best_char = ""
    Code.append(0)
    # [92, 92] pour eviter ` et \
    for char in [chr(m) if not m in [96, 92] else "0" for m in range(35, 126)]:
        Code[i] = char

        Input = "python hash.py \""+"".join(Code)+"\""
        print("Input: ", Input)
        var = subprocess.check_output(Input, shell=True)
        print(var)
        # distance au hash init
        dist = abs(int(init, 16) - int(var, 16))
        if min_dist > dist:
            min_dist = dist
            best_char = char
    Code[i] = best_char

    print(Code)
print("".join(Code), min_dist)



