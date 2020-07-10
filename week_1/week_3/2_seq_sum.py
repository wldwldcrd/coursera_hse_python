n = int(input())

i = 1
seq_sum = 0
while i <= n:
    seq_sum += i ** (-2)
    i += 1
print('{0:.10f}'.format(seq_sum))
