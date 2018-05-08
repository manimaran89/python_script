def second_largest(numbers):
    count = 0
    n1 = n2 = float('-inf')
    for x in numbers:
        count += 1
        if x > n2:
            if x >= n1:
                n1, n2 = x, n1            
            else:
                n2 = x
    return n2 if count >= 2 else None

print(second_largest([1, 2, -8, -2, 0]))
