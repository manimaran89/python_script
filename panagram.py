import string
def all_alpha_present(word):
    s = set(word.lower())
    print s
    print len(s)
    lower = set(string.ascii_lowercase)
    print lower
    if s >= lower:
        return True
    return False

print all_alpha_present('ABCDefghijklmnopqrstuvwxyz')
print all_alpha_present('jaklsdfkasgKAJKLJLJJWKTJRKNTLSNGFKLSG')
