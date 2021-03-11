# try:
# 	print(x)
# except:
# 	print('an exception occurred')


# try:
# 	print(x)
# except NameError:
# 	print('x not defined')


# try:
# 	print('Hello')
# except:
# 	print('something went wrong')
# else:
# 	print('nothing went wrong')


# try:
# 	print('Hello')
# except:
# 	print('something went wrong')
# finally:
# 	print('The try except is finished')
	

# try:
# 	while True:
# 		pass
# except KeyboardInterrupt:
# 	print('\nGood Bye')


# x = -1
# if x < 0:
# 	raise Exception('Sorry no numbers below 0')


# x = 'Hello'
# if not isinstance(x,str):
# 	raise TypeError('only integers')

# try:
# 	print(5/0)
# 	print(x)
# except NameError:
# 	print('x chunenq')
# except ZeroDivisionError:
# 	print('number not division by 0')


# while True:
# 	try:
# 		numb = int(input('Enter your num: '))
# 		print('Good')
# 		break
# 	except ValueError:
# 		print('input only number')


# try:	
# 	print(5 + '5')
# except TypeError:
# 	print('only int or str')

# try:
# 	name = input('enter name: ')
# except KeyboardInterrupt:
# 	print('\nGood Bye')


# my_list = [1, 4, -3, 59, True]
# try:
# 	print(my_list[11])
# except IndexError:
# 	print('We dont have this index')



# name = dict(fname = 'Susi', age = 26, city = 'Yerevan')
# try:
# 	print(name['lname'])
# except KeyError:
# 	print('we dont have this key')

# while True:
# 	try:
# 		name = input('Enter name: ')
# 		if not name.isalpha():
# 			raise ValueError
# 		else:
# 			print('Thanks for your registration', name)
# 			break
# 	except ValueError:
# 		print('Only letters')


# while True:
# 	try:
# 		password = input('Enter you password')
# 		if not password.istitle():
# 			raise TypeError('Miayn mecatar')
# 		else:
# 			print('Tnaks for your registration')
# 			break
# 	except ValueError:
# 		print('No')
# 	except TypeError:
# 		print('Only Letters')

# num = int(input('num '))

# try:
# 	res = 2/num
# except:
# 	print('no')
# else:
# 	print(res)	 	

# age = int(input('age '))
# try:
# 	if age < 0:
# 		raise Exception('Please input positive number')
# except ValueError:
# 	print('0')


# x = input('x: ')

# if isinstance(x, str):

# if not x.isdigit():
# 	raise TypeError("Only integers are allowed")
# else:	
# 	print('good')

# try:
# 	import Susik
# except ModuleNotFoundError:
# 	print('No Susik')

while True:
    mydic = {"Anna" : 10, "Narek" : 9, "Mane" : 7}
    try:
        name = input("Name: ")
        if not name.isalpha():
            raise ValueError
        print(name,mydic[name],'years old')
        break
    except KeyError:
        print(name, "don't found")
    except ValueError:
        print("Invalid input")







