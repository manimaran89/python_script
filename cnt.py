vowels = 'aeiou'

# change this value for a different result
ip_str = 'Hello, have you tried our turorial section yet?'

# uncomment to take input from the user
#ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)
print count
