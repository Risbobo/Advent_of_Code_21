def process(my_input):
    my_file = open(my_input, 'r')
    lines = my_file.readlines()
    base = lines[0].strip()
    insertions = {}
    for line in lines[2:]:
        pattern, elem = line.strip().split(' -> ')
        insertions[pattern] = elem
    return base, insertions


def add_one(dic, letter):
    if letter in dic:
        dic[letter] += 1
    else:
        dic[letter] = 1


# def remove_one(dic, letter):
#     assert letter in dic
#     dic[letter] -= 1


def polymerization(base, insertions, num_step=0):
    letters = {}
    pairs = {}
    add_one(letters, base[0])
    for i in range(1, len(base)):
        add_one(letters, base[i])
        add_one(pairs, base[i-1] + base[i])
    for _ in range(num_step):
        next_pairs = {}
        # Missing multiple occurences in pairs
        for pair in pairs:
            new_letter = insertions[pair]
            add_one(letters, new_letter)
            add_one(next_pairs, pair[0] + new_letter)
            add_one(next_pairs, new_letter + pair[1])
        pairs = next_pairs
    return letters, pairs


template, rules = process('ex_14.txt')
print(template)
print(rules)
print(polymerization(template, rules, 3))
