# shop = ('dell', 'hp', 'hp','Aser','ViewSoinc','dell')
# user = input('preferable comp: ')

# if user in shop:
# 	print('yes count -', shop.count(user))
# 	print(len(shop))
# else:
# 	print('sorry')


# name = ('aram', 'Sona', 'Lusine')
# c = 0

# for i in name:
# 	if i == 'Sona':
# 		print(c)
# 		break
# 	c += 1


# a = ()
# print(type(a))

# b = tuple()
# print(type(b))



# import sys
# tup1 = ('physics', 'chemistry',1998,2023)
# tup2 = ('math', 'history','languages',1908,2003)
# print(sys.getsizeof(tup1))
# print(sys.getsizeof(tup2))


# tupthis = ('apple','banana','cheryy',1998,2023)
# print(len(tupthis))


# tupthis = ('apple','banana','cherry',1998,2023, 'cherry')
# print(tupthis.count(1998))
# print(tupthis.count('cherry'))



# tupthis = ('apple','banana','cherry',1998,2023, 'cherry')

# if 'cherry' in tupthis:
# 	print('yes, cherry is in the fruits tuple')
# else:
# 	print('sorry, please try again')



# tupthis = ('apple','banana','cherry',1998,2023, 'cherry')
# for x in tupthis:
# 	print(x)
# 	# print(x, end ="-")



# tupthis = ('apple','banana','cherry',1998,2023,'cherry')
# print(tupthis[1])
# print(tupthis[0:3])
# print(tupthis[2:])
# print(tupthis[2:4])



# x = (5,10,15,20,25)
# y = reversed(x)
# print(tuple(y))



# tupthis=('apple','banana','cherry','cherries','orange','kiwi','melon','mango')
# print(tupthis[-4:-1])
# print(tupthis[-1])
# print(tupthis[-2])


# tuple1 = ('a','b','c','d')
# tuple2 = (1,2,3,4)
# tuple3 =tuple1 + tuple2
# print(tuple3)



# #      0  1  2     3    4  5     6
# num = [10,20,30,(10,20),40,50,(60,60)]
# c = 0
# for i in num:
# 	if isinstance(i, tuple):
# 		break
# 	c += 1
# print(c)



tup1 = ('e','x','e','r','c','i','s','e','s')
mystr = ''.join(tup1)
tup2 = ('s','u','s','a','n','n','a','m','a','r','t','r','o','s','y','a','n')
myname = '-'.join(tup2)
print(mystr)
print(myname)


