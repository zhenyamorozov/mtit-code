# def is_palindrome1(word):
#     '''Returns True if the provided word is a valid palindrome'''
#     # 0 1 2 3 4 5 6
#     # R O T A T O R

#     i = 0
#     while i < len(word)//2:

#         if word[i] != word[len(word)-i-1]:
#             return False

#         i = i + 1

#     return True

def dummy_function():
    pass

def is_palindrome(word):
    return word == word[::-1]

number = 0
fp = open('words.txt', 'r')
for i in fp:
    i = i.strip()
    if is_palindrome(i):
        number += 1
        print(number, i)
fp.close()