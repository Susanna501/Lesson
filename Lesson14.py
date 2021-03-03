# x = [1,2]
# y = (1,2)

# import sys

# print(sys.getsizeof(x))
# print(sys.getsizeof(y))

# print(x is y)

# names = [12, 6.8, 21]

# print(len(names))
# print(max(names))
# print(min(names))
# print(sum(names))
# print(sum(names)/len(names))

# print(names[0])
# print(names[-1])
# print(names[::-1])
# print(names[::])
# print(names[-3:-1])
# print(names[1:3])


# cars = ['Bmw', 'Jack', 'Mers','Audi']
# people = ['Ani','Anna']
# print(cars.index('Bmw'))

# cars.extend(people)
# print(cars)

# cars.sort()
# print(sorted(cars))


# x = tuple(cars)
# print(type(x))

# cars[-1]='Niva'

# cars.append('Lada')
# cars.insert(3,'Lexus')
# cars.remove('Audi') 

# car = cars.pop()
# print(cars)
# print(car)


# del cars[1]
# del cars
# print(cars)


# x = [1,2,3,52,1,2,312,1]
# print(sorted(x)[-1])

# x.reverse()
# print(x)


# my_list = [43,123,-12,3]

# first = my_list[0]

# for i in my_list:
# 	if first < i:
# 		first = i

# print(first)
# my_list = [43,123,-12,3]

# first = my_list[0]

# for i in my_list:
# 	if first > i:
# 		first = i

# print(first)

# my_list = [43,123,-12,3]

# num = -12

# if num in my_list:
# 	print(my_list.index(num))
# else:
# 	print('no')	
# c = 0
# for i in my_list:

# 	if  i == num:
# 		break
# 	c+=1
# print(c)


# for i in range(len(my_list)):
# 	if my_list[i] == num:
# 		print(i)
# 		break


# cars = ['audi','bmw','audi','audi','bmw']

# n = [] # datark list
# for i in cars:
# 	if i not in n:  # ete chka darak listum
# 		n.append(i) # avelacnumenq

# print(n)






# fruits = ['banana', 'apple', 'cherry']
# print(fruits)

# '''        0    1    2     3     4   '''
# numbers = [34, 56, -456, 7.56, -2.34]
# '''        -5  -4   -3    -2    -1   '''
# print(numbers)
# print(numbers[2])
# print(numbers[-4])
# print(numbers[-1])


# fruits = ['banana', 'apple', 'cherry']
# print(fruits[1:3])
# print(fruits[:3])
# print(fruits[1:])
# print(fruits[-3:-1])

'''Change item Value'''
# fruits = ['banana', 'apple', 'cherry']
# fruits[1] = 'orange'
# fruits[0] = 'kiwi'
# print(fruits)
# print(len(fruits))     # tpum e 3, qani vor listi mej ka 3 anun-arjeq
# print(len(fruits[1]))  # tpum e 6, qani vor 1-in indexy orangen e- 6 tar,vory poxel enq , apple-ic orange


# fruits = ['banana', 'apple', 'cherry']
# fruits.append('kiwi')   	# avelacnum e listi verjum 
# print(fruits)

# fruits = ['banana', 'apple', 'cherry']
# fruits.insert(0,'orange') # avelacnum e mer nshvac arjeqic heto, ete 0 index , apa 1 indexum kavelacni  
# print(fruits)

# fruits = ['banana', 'apple', 'cherry']
# fruits.remove('cherry') 
# print(fruits)


# fruits = ['banana', 'apple', 'kiwi', 'cherry']
# mirg = fruits.pop()   # mirg popoxakani mej pahum e listi verjin arjeqy
# print(fruits)
# print(mirg)

# fruits = ['banana', 'apple', 'kiwi', 'cherry']
# del fruits[0]
# print(fruits)


# fruits = ['banana', 'apple', 'kiwi', 'cherry']
# number = [34, 56, -456, 7.56, -2.34]
# fruits.extend(number)  # extendov miacnum eqn listery irar, ete fruit in miacnenq tvery verjum en 
# number.extend(fruits)  # isk ete numberin miacnenq fruit apa tvery skzbum klinen, tarery verjum en 
# print(fruits)
# print(number)


# number = [34, 56, -456, 7.56, -2.34]
# number.sort()  # sortavorum e poqric mec
# print(number)

# fruits = ['banana', 'apple', 'kiwi', 'cherry']
# print(sorted(fruits[-1]))  # tpum e -1 indexy u arandznacrac bolor tarer ['c', 'e', 'h', 'r', 'r', 'y']

# fruits = ['banana', 'apple', 'kiwi', 'cherry']
# fruits.sort()
# print(fruits)

# fruits = ['banana', 'apple', 'kiwi', 'cherry']
# print(sorted(fruits)[-1])


# number = [34, 56, -456, 7.56, -2.34]
# number.reverse()
# print(number)


# number = [34, 56, -456, 7.56, -2.34]
# number.clear()
# print(number)


# number = [34, 56, -456, 7.56, -2.34]
# tiv = number.copy()
# print(tiv)

# cars = ['Bmw', 'Jack', 'Mers','Audi']
# print(cars.index('Bmw'))
# print(cars.index('Audi'))






