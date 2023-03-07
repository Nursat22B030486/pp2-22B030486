word = input()
word_reversed = ''.join(reversed(word))

if word == word_reversed:
    print('Yes, it\'s palindrome!')
print(word_reversed)
