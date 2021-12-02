myFile = open("input_1.txt", 'r')
lines = myFile.readlines()
depths = [int(x.strip()) for x in lines]

count_inc = 0
count_dec = 0
count_stag = 0

old_sum = depths[0] + depths[1] + depths[2]
for i in range(2, len(lines)-1):
    prev = depths[i-1]
    current = depths[i]
    next = depths[i+1]
    sum = prev + current + next
    if old_sum < sum:
        count_inc += 1
    elif old_sum > sum :
        count_dec += 1
    else :
        count_stag += 1
    old_sum = sum

print(count_inc)
#print(count_dec)
#print(count_stag)
#print(count_dec+count_inc+count_stag)