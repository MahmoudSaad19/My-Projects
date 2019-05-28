print("welcome to my guessing game ")
Secret_Word= "Valkyrie"
guess=''

while guess != Secret_Word:
    try:
        guess = input("enter your guess ")
        count = 0
        for s in range(len(guess)):
            for i in guess:
                if i == Secret_Word[s]:
                    count += 1

        if guess != Secret_Word:
            print('your guess is wrong but you have ', count, 'correct letters ')

    except IndexError:
        print("too long the word is shorter than that ")
    except:
        print("inalid input")
print('\n your guess is right \n you won the game \n congratulations ')
