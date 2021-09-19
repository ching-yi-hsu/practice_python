str_word = str(input("enter a string : "))
str_word_rev = str_word[::-1]

if str_word == str_word_rev :
    print(str_word , " is a palindrome word")
else :
    print(str_word, " isn't a palindrome word")

