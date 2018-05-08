def pos_occ_of_letters(word):
    result = {}
    letters = set(word)
    for i in letters:
        result[i] = word.count(i)
    return result

print pos_occ_of_letters('manimaran')
