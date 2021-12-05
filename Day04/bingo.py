myFile = open("input_04.txt", 'r')
lines = myFile.readlines()

bingo_numero = lines[0].strip().split(',')


# Create a list of board from the lines in the input
def boards_maker(lines):
    boards = []
    board = []
    for line in lines:
        line = line.split()
        if not line:
            boards.append(board)
            board = []
        else:
            board_line = [[numero, False] for numero in line]
            board.append(board_line)
    boards.append(board)
    return boards


# Mark the number in the board (swap the boolean for the number)
def mark(numero, board):
    for line in board:
        for case in line:
            if case[0] == numero:
                case[1] = True


# Check if there is a bingo on the LINES of a board
def check_lines(board):
    for line in board:
        inter = True
        for case in line:
            inter = inter and case[1]
        if inter:
            return True
    return False


# Check if there is a bingo on a board
def check(board):
    # This weird thing transpose a list of list
    board_T = list(map(list, zip(*board)))
    return check_lines(board) or check_lines(board_T)


# Sum all the unmarked number of a board
def unmarked_sum(board):
    somme = 0
    for line in board:
        for case in line:
            if not case[1]:
                somme += int(case[0])
    return somme


# Compute solution for first part
def run_bingo(numeros, boards):
    for n in numeros:
        for board in boards:
            mark(n, board)
            if check(board):
                return int(n) * unmarked_sum(board)
    return 0


# Compute solution for part 2
def run_anti_bingo(numeros, boards):
    # End condition
    if len(boards) == 1:
        return run_bingo(numeros, boards)

    # Eliminate winning board until only one
    for i, n in enumerate(numeros):
        for b, board in enumerate(boards):
            mark(n, board)
            if check(board):
                # Continuing with not winning boards
                new_board = boards[:b]
                # If the winning board is not the last one, append the boards after
                if b < len(boards)-1:
                    new_board += boards[b+1:]
                return run_anti_bingo(numeros[i:], boards[:b] + boards[b+1:])


boards1 = boards_maker(lines[2:])
boards2 = boards1
print(run_bingo(bingo_numero, boards1))
print(run_anti_bingo(bingo_numero, boards2))
