import numpy as np


def process(my_input):
    my_file = open(my_input, 'r')
    lines = my_file.readlines()
    sig = []
    val = []
    for line in lines :
        separate = line.strip().split(' | ')
        sig.append(separate[0].split())
        val.append(separate[1].split())
    return sig, val


def decrypto(signal):
    # upper = ''
    # middle = ''
    # downer = ''
    # u_left = ''
    # u_right = ''
    # d_left = ''
    # d_right = ''

    zero = ''
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''
    n_235 = []
    n_069 = []
    for sig in signal:
        if len(sig) == 2:
            one = sig
        elif len(sig) == 3:
            seven = sig
        elif len(sig) == 4:
            four = sig
        elif len(sig) == 7:
            eight = sig
        elif len(sig) == 5:
            n_235.append(sig)
        elif len(sig) == 6:
            n_069.append(sig)

    for numero in n_069:
        if len(minus(numero, four)) == 2:
            nine = numero
            n_069.remove(nine)
    zero = n_069[0] if len(minus(seven, n_069[0])) == 0 else n_069[1]
    n_069.remove(zero)
    six = n_069[0]

    for numero in n_235:
        if len(minus(numero, seven)) == 2:
            three = numero
            n_235.remove(three)
    five = n_235[0] if len(minus(six, n_235[0])) == 1 else n_235[1]
    n_235.remove(five)
    two = n_235[0]
    return [zero, one, two, three, four, five, six, seven, eight, nine]


def decode(cypher, val):
    real_val = ''
    for numero in val:
        for real_numero, code in enumerate(cypher):
            # print(real_numero, code, numero)
            if sortString(numero) == sortString(code):
                real_val += str(real_numero)
    return int(real_val)


# Return letters in n1 but not in n2
def minus(n1, n2):
    res = ''
    for letter in n1:
        if letter not in n2:
            res += letter
    return res

def sortString(str):
    return ''.join(sorted(str))


signals, values = process('input_08.txt')
# signals, values = process('input_08.txt')

# Part 1
somme = 0
for line in values:
    for numero in line:
        if len(numero) in [2, 3, 4, 7]:
            somme += 1
print(somme)

# Part 2

real_values = []
for i in range(len(signals)):
    chiffre = decrypto(signals[i])
    real_values.append(decode(chiffre, values[i]))
print(real_values)
print(sum(real_values))
