def process(my_input):
    my_file = open(my_input, 'r')
    lines = my_file.readlines()
    base = lines[0].strip()
    insertions = {}
    for line in lines[2:]:
        pattern, elem = line.strip().split(' -> ')
        insertions[pattern] = elem
    return base, insertions


def add_in_dic(dic, letter, value=1):
    if letter in dic:
        dic[letter] += value
    else:
        dic[letter] = value


def polymerization(base, insertions, num_step=0):
    letters = {}
    pairs = {}
    # Initialisation
    add_in_dic(letters, base[0])
    for i in range(1, len(base)):
        add_in_dic(letters, base[i])
        add_in_dic(pairs, base[i - 1] + base[i])
    # Update of the number of letters for each step
    for _ in range(num_step):
        next_pairs = {}
        for pair in pairs:
            val = pairs[pair]
            new_letter = insertions[pair]
            add_in_dic(letters, new_letter, val)
            add_in_dic(next_pairs, pair[0] + new_letter, val)
            add_in_dic(next_pairs, new_letter + pair[1], val)
        pairs = next_pairs
    return letters


# template, rules = process('ex_14.txt')
template, rules = process('input_14.txt')

# First part
poly = polymerization(template, rules, 10)
print("Answer to part 1 : ", max(poly.values()) - min(poly.values()))
# Second part
poly = polymerization(template, rules, 40)
print("Answer to part 2 : ", max(poly.values()) - min(poly.values()))
