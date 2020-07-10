answer_list = list(
    set(map(int, input().split())) & set(map(int, input().split())))
answer_list.sort()
print(*answer_list)
