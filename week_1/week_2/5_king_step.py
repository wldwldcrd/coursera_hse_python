start_cell = [int(input()), int(input())]
stop_cell = [int(input()), int(input())]

if (abs(start_cell[0] - stop_cell[0]) < 2 and
        abs(start_cell[1] - stop_cell[1]) < 2):
    print('YES')
else:
    print('NO')
