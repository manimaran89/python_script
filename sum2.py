def sum_of_biggest(nos, n):
    sum = 0
    for i in range(n):
        if nos:
            big = max(nos)
            sum = sum + big
            nos.remove(big)
    return sum

print sum_of_biggest([2, 5, 3, 4], 5)
