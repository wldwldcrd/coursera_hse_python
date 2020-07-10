max_of_streak = 1
num_of_streak = 1
prev = 0
act = int(input())
while act != 0:
    if act == prev:
        num_of_streak += 1
    else:
        num_of_streak = 1
    if num_of_streak > max_of_streak:
        max_of_streak = num_of_streak
    prev = act
    act = int(input())
print(max_of_streak)
