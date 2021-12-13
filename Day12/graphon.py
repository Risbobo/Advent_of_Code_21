def generate_graph(my_input):
    my_file = open(my_input, 'r')
    lines = my_file.readlines()
    caves = {}
    for line in lines:
        first, second = line.strip().split('-')
        if first not in caves:
            caves[first] = [second]
        else:
            caves[first] = caves[first] + [second]
        if second not in caves:
            caves[second] = [first]
        else:
            caves[second] = caves[second] + [first]
    return caves


def explore(cave, path=[], part2=False):
    if cave == 'end':
        return 1
    elif cave == 'start' and cave in path:
        return 0
    elif cave.lower() == cave and cave in path and not part2:
        return 0
    else:
        if cave.lower() == cave and cave in path:
            part2 = False
        new_path = path + [cave]
        count = 0
        for neighbour in subterrean[cave]:
            count += explore(neighbour, new_path, part2)
        return count


subterrean = generate_graph('ex_12.txt')
print(explore('start'))
print(explore('start', part2=True))
subterrean = generate_graph('ex_12_2.txt')
print(explore('start'))
print(explore('start', part2=True))
subterrean = generate_graph('ex_12_3.txt')
print(explore('start'))
print(explore('start', part2=True))
subterrean = generate_graph('input_12.txt')
print(explore('start'))
print(explore('start', part2=True))
