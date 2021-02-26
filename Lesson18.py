'''Task1-Create new dictionary where you have 10 students and each of them have rating(1-10).'''

# students ={'Kevin': 3,'Alis': 9,'Ani': 6, 
# 			'Sona': 10,'Jas': 8,'Lus': 5,
# 			'Anna': 1,'Susik': 7,'Armine': 6,'Satik': 4}

# print(students)

'''Task2 Create python program which will calculate the arithmetic average of rating students.'''

# students ={'Kevin': 3,'Alis': 9,'Ani': 6, 
# 			'Sona': 10,'Jas': 8,'Lus': 5,
# 			'Anna': 1,'Susik': 7,'Armine': 6,'Satik': 4}

# count = 0
# count_len = 0

# for i in students.values():
# 	count +=i
# 	count_len +=1

# res = count/count_len
# print(res)


'''Task3-Create a python program which will say you who they are good and bad students.'''
# students ={'Kevin': 3,'Alis': 9,'Ani': 6, 
# 			'Sona': 10,'Jas': 8,'Lus': 5,
# 			'Anna': 1,'Susik': 7,'Armine': 6,'Satik': 4}
# maximum = 0

# for i in students.values():
# 	if i > maximum:
# 		maximum = i

# minimum = maximum

# for i in students.values():
# 	if i < minimum:
# 		minimum = i 

# for i in students:
# 	if students[i] == maximum:
# 		print('Max',i)
# 	elif students[i] == minimum:
# 		print('Min',i)

# print('min',minimum)
# print('max',maximum)



'''Task4 Create a python program which will say who have 5 or great rating in your Students.'''
# students ={'Kevin': 3,'Alis': 9,'Ani': 6, 
# 			'Sona': 10,'Jas': 8,'Lus': 5,
# 			'Anna': 1,'Susik': 7,'Armine': 6,'Satik': 4}

# count = 5
# for i in students:
# 	if students[i] >= count:
# 		print(i, students[i],)

'''Task5-Create a python program which will say if your dictionary have this name print name and rating.'''

# students ={'Kevin': 3,'Alis': 9,'Ani': 6, 
# 			'Sona': 10,'Jas': 8,'Lus': 5,
# 			'Anna': 1,'Susik': 7,'Armine': 6,'Satik': 4}

# name = input('enter your name: ')

# if name in students:
# 	print(name,students[name])
# else:
# 	print('please try again')


'''Task7 -Create a new dictionary: For example…
s = 'a,2,b,5,c,8,a,4,e,11' 
{“a”:6,”b”:5,”c”:8,”e”:11}'''

# s = 'a,2,b,5,c,8,a,4,e,11'.split(",")
# # print(s) 

# dic = dict()
# for i in range(0,len(s),2):
# 	if s[i] in dic:
# 		dic[s[i]] = int(s[i + 1]) + int(dic[s[i]])
# 	else:
# 		dic[s[i]] = int(s[i + 1])
# print(dic)




