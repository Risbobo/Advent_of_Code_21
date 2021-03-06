def navigate(input):
    myFile = open(input, 'r')
    lines = myFile.readlines()
    instructions = [(x.split()[0], int(x.split()[1])) for x in lines]

    coord = [0,0]
    aim = 0
    for instr, dist in instructions :
        #print(instr, dist)
        if instr == 'forward':
            coord[0] += dist
            coord[1] += aim * dist
        elif instr == 'down' :
            aim += dist
        elif instr == 'up' :
            aim -= dist
        else :
            print("Error : {} is not an instruction".format(instr))
    return coord

#res = navigate('ex_02.txt')
res = navigate('input_02.txt')
print(res)
print(res[0]*res[1])