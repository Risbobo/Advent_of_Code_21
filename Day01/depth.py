myFile = open("input_01.txt", 'r')
lines = myFile.readlines()
depths = [int(x.strip()) for x in lines]

count_inc = 0
count_dec = 0
old_depth = depths[0]

for depth in depths[1:]:
    if old_depth <= depth:
        count_inc += 1
    else:
        count_dec += 1
    old_depth = depth

print(count_inc)
#print(count_dec)
#print(count_dec+count_inc)