def process(my_input):
    my_file = open(my_input, 'r')
    lines = my_file.readlines()
    return [line.strip() for line in lines]


def is_opening(c):
    return c == '(' or c == '{' or c == '[' or c == '<'


def is_closing(c):
    return c == ')' or c == '}' or c == ']' or c == '>'


def is_balanced(c1, c2):
    return (c1 == '(' and c2 == ')') or (c1 == '{' and c2 == '}') or (c1 == '[' and c2 == ']') or (
            c1 == '<' and c2 == '>')


def check_balance(string, part='part_1'):
    stack = []
    for c in string:
        if is_opening(c):
            stack.append(c)
        if is_closing(c):
            if not stack or not is_balanced(stack.pop(), c):
                if part == 'part_1':
                    return c
                else:
                    return ''
    if part == 'part_1':
        return ''
    else:
        if stack:
            return stack
        else:
            return ''


def score_1(string):
    s = 0
    for c in string:
        if c == ')':
            s += 3
        if c == '}':
            s += 1197
        if c == ']':
            s += 57
        if c == '>':
            s += 25137
    return s


def score_2(string):
    s = 0
    for c in string[::-1]:
        if c == '(':
            s = 5 * s + 1
        if c == '{':
            s = 5 * s + 3
        if c == '[':
            s = 5 * s + 2
        if c == '<':
            s = 5 * s + 4
    return s


brackets = process('input_10.txt')
incorrect = []
incomplete = []
for bracket in brackets:
    incorrect.append(check_balance(bracket))
    score = score_2(check_balance(bracket, part='part_2'))
    if score > 0:
        incomplete.append(score)
print(score_1(incorrect))
print(incomplete)
print(sorted(incomplete)[int((len(incomplete) - 1) / 2)])

