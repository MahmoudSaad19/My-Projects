w=input("enter a word ")
vowels=['a','i','o','u','e']
word=''
for letter in w :
    if letter in vowels :
        letter='*'
    word=word+letter
print(w)
print(word)
