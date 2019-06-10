from pyfiglet import *

print_figlet('hello WORLD !',colors='red'.upper())
for i in range(5):
    try:
        word = input('enter a word ? \n')
        color = input('what color ? \n')
        print_figlet(word, colors=color.upper())
    except:
        from termcolor import colored
        text =colored('*** you enterd invalid color ***'.upper(),color='red',on_color='on_yellow')
        print(text)
