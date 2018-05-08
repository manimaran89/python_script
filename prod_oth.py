def product_other_elements(nos):
    prod = reduce(lambda x,y: x*y, nos)
    return map(lambda  n: prod/n, nos)

print product_other_elements([1, 2, 3, 4])
