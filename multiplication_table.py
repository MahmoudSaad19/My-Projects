import time

def multiplication_table():
	for i in range(13):
		print('\n')
		for j in range(13):
			print(f'{i} x {j} = {i*j}')

multiplication_table()

def mul_table_with_user_click():
	for i in range(14):
		print(f'\nDo you want {i} table ? \nPress Enter to continue.... \n')
		input()
		for j in range(13):
			time.sleep(.3)
			print(f'{i} x {j} = {i * j}')

mul_table_with_user_click()
