
from random import randint as r
point = 0
question = input('Do you want play 1st? Y/N: ').upper() == 'Y'

if question:

	while True:

		if point > 4:
			user = 4 - point % 4
		else:
			user = 4- point

		if point > 18:
			end = 22- point
		else:
			end = 4

		while True:
			user = input('123: ')
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					break
				else:
					print('please input between 1-3')
			else:
				print('please input number ')
				
		print('User Sus',point, '+', user,'=', point + user )
		
		point += user
		res = point >= 21
		pc = r(1,3)

		if res:
			print('pc win')
			break
		print('Pc',point, '+', pc,'=', point + pc )
								
		point += pc
		res = point >= 21
		if res:
			print('user win')
			break
else:

	while True:

		if point % 4 == 0:
			pc = r(1,3)

		else:
			pc = 4 - point % 4
		print('Pc',point, '+', pc,'=', point + pc )		

		point += pc
		res = point >= 21
		
		if res:
			print('user win')
			break
		
		if point > 18:
			end = 22- point

		else:
			end = 4

		while True:
			user = input('123: ')
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					break
				else:
					print('please input correct')
			else:
				print('please input number ')

		print('User Sus',point, '+', user,'=', point + user )
		
		point += user
		res = point >= 21
		if res:
			print('pc win')
			break


