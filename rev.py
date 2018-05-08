def name(strs):
    for i in range(len(strs)-1, -1, -1):
        yield strs[i]

print ''.join(name('hello'))
