def seq_reverse():
    act = int(input())
    if act != 0:
        seq_reverse()
    print(act)
    return 0


seq_reverse()
