from utils import input_reader, bin_to_int
import numpy as np


# Well this is pretty much useless for part 2
def in_the_bin(input, n):
    bin_mat = np.array(input_reader(input, [str]*n, lambda x : list(str.split(x)[0])))
    bs = [bin_to_int(''.join(col)) for col in bin_mat.T]
    γ = bin_to_int(''.join(['1' if bk_algo(b) > len(bin_mat)/2 else '0' for b in bs]))
    # 11111 - γ for the example
    ε = 2**n-1-γ
    return γ, ε


# Count the number of 1 in the binary representation
# Not for Burger King
# But Brian Kernighan’s Algorithm
def bk_algo(b):
    count = 0
    n = b
    while n > 0:
        n = n & (n-1)
        count += 1
    return count


print(in_the_bin('ex_03.txt', 5))
res = in_the_bin('input_03.txt', 12)
print(res)
print(res[0]*res[1])
