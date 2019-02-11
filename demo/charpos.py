def char_occurence_pos(word):
    original_word = set(word)
    result_dict={}
    for ch in word:
	inner_dict={}
	ch_positions = [ pos for pos, c in enumerate(word) if c == ch ]
	count = word.count(ch)
	inner_dict['occurrence']=count
	inner_dict['pos'] = ch_positions
	result_dict[ch] = inner_dict
    return result_dict
word="Hellohello"
print char_occurence_pos(word)
