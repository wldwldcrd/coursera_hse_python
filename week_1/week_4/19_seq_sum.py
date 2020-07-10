def seq_sum():
    act = int(input())
    if act != 0:
        return (act + seq_sum())
    return 0


print(seq_sum())
