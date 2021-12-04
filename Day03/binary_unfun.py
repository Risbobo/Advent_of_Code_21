from Day03.binary_fun import bk_algo
from utils import input_reader, bin_to_int, int_to_bin
import numpy as np


def out_of_bin(input, n):
    bin_mat = np.array(input_reader(input, [str] * n, lambda x: list(str.split(x)[0])))
    return sieve_line(bin_mat, True), sieve_line(bin_mat, False)


def sieve_line(mat, oxy=True):
    # Very dirty end conditions
    if len(mat) == 0 or len(mat[0]) == 0 :
        return []
    if len(mat) == 1:
        return list(mat[0])

    γ = bk_algo(bin_to_int(''.join(mat.T[0])))
    if oxy:
        test = γ >= (len(mat.T[0]) / 2.0)
    else:
        test = γ < (len(mat.T[0]) / 2.0)
    byte = '1' if test else '0'
    return [byte] + sieve_line(np.array([line[1:] for line in mat if line[0] == byte]), oxy)


res1, res2 = out_of_bin('input_03.txt', 12)
res1 = bin_to_int(''.join(res1))
res2 = bin_to_int(''.join(res2))
print(res1, res2, res1 * res2)