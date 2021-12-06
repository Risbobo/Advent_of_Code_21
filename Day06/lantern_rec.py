import numpy as np


ex_06 = np.array([3, 4, 3, 1, 2])
input_06 = np.array([1, 2, 5, 1, 1, 4, 1, 5, 5, 5, 3, 4, 1, 2, 2, 5, 3, 5, 1, 3, 4, 1, 5, 2, 5, 1, 4, 1, 2, 2, 1, 5, 1, 1, 1, 2,
            4, 3, 4, 2, 2, 4, 5, 4, 1, 2, 3, 5, 3, 4, 1, 1, 2, 2, 1, 3, 3, 2, 3, 2, 1, 2, 2, 3, 1, 1, 2, 5, 1, 2, 1, 1,
            3, 1, 1, 5, 5, 4, 1, 1, 5, 1, 4, 3, 5, 1, 3, 3, 1, 1, 5, 2, 1, 2, 4, 4, 5, 5, 4, 4, 5, 4, 3, 5, 5, 1, 3, 5,
            2, 4, 1, 1, 2, 2, 2, 4, 1, 2, 1, 5, 1, 3, 1, 1, 1, 2, 1, 2, 2, 1, 3, 3, 5, 3, 4, 2, 1, 5, 2, 1, 4, 1, 1, 5,
            1, 1, 5, 4, 4, 1, 4, 2, 3, 5, 2, 5, 5, 2, 2, 4, 4, 1, 1, 1, 4, 4, 1, 3, 5, 4, 2, 5, 5, 4, 4, 2, 2, 3, 2, 1,
            3, 4, 1, 5, 1, 4, 5, 2, 4, 5, 1, 3, 4, 1, 4, 3, 3, 1, 1, 3, 2, 1, 5, 5, 3, 1, 1, 2, 4, 5, 3, 1, 1, 1, 2, 5,
            2, 4, 5, 1, 3, 2, 4, 5, 5, 1, 2, 3, 4, 4, 1, 4, 1, 1, 3, 3, 5, 1, 2, 5, 1, 2, 5, 4, 1, 1, 3, 2, 1, 1, 1, 3,
            5, 1, 3, 2, 4, 3, 5, 4, 1, 1, 5, 3, 4, 2, 3, 1, 1, 4, 2, 1, 2, 2, 1, 1, 4, 3, 1, 1, 3, 5, 2, 1, 3, 2, 1, 1,
            1, 2, 1, 1, 5, 1, 1, 2, 5, 1, 1, 4])


# The recursive methode is nice but don't hold for part 2
def lantern_fish(timer, day, final_day):
    if day == final_day:
        return 1
    if timer == 0:
        return lantern_fish(6, day + 1, final_day) + lantern_fish(8, day + 1, final_day)
    return lantern_fish(timer - 1, day + 1, final_day)


inpout = ex_06
#inpout = input_06
number_of_fish = 0
final_day = 80
for timer in np.unique(inpout):
    number_of_fish += np.count_nonzero(inpout == timer) * lantern_fish(timer, 0, final_day)
print(number_of_fish)
