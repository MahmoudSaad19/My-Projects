from csv import *

def create_user():
    with open('pc_users.csv','w')as file:
        pen=writer(file)
        pen.writerow(['user_name','job'])
        pen.writerow(['modi','python_dev'])
        pen.writerow(['mana','c_dev'])
        pen.writerow(['shady','acountant'])


def print_user():
    with open('pc_users.csv','r')as f:
        data=reader(f)
        for line in data:
            if line:
                print(line)

def search_for_a_user(user_name):
    with open('pc_users.csv','r') as s:
        data=reader(s)
        for line in data:
            if line:
                if line[0]==user_name:
                    return f'\nthe user name {user_name} is found and his job is {line[1]}'
        return f'\nthe user name {user_name} not found'

while True:
    word=input('\nenter the user name you want to search about ?  or e for exist')
    if word.lower()=='e':
        print('\ngood bye ^_^')
        break
    else:
        print(search_for_a_user(word))

#print_user()
