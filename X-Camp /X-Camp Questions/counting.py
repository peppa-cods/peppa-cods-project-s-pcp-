import sys
word = ''
for line in sys.stdin:
	word += line
Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]
hits = [
    (Alphabet[i], word.count(Alphabet[i]))
    for i in range(len(Alphabet))
    if word.count(Alphabet[i])
]
for letter, frequency in hits:
	print("{}:{}".format(letter,frequency))	