
def list_vowels_before(char):
	for vowel in ('a', 'e', 'i', 'o', 'u'):
		if vowel == char:
			break
		yield vowel


if __name__ == "__main__":
	d = list_vowels_before('i')
	print(list(d))
