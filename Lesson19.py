
# import sys

# names = {'Ani', 'Anna','Davit',"Ani" }
# print(sys.getsizeof(names))

# for i in names:
# 	print(i)


# c = set('ANi')
# print(c)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# c = tuple(set1)
# print(c)
# set3 = set1.union(set2)
# print(set3)

# set1 = {12,23,11,'hello'} 
# set2 = {14,3,141,11,'world'}
# print(set1.isdisjoint(set2))





#x = 5
#
#while True:
#	print(x)
#	x+=1
#	if x == 10:
#		break
  
#while True:
#
#    number = input('number ')
#    if number.isdigit():
#        print('thanks')
#        break
#    print('please input only numbers')

#while True:
#
#    letter = input('letter ')
#    if letter.isdigit():
#        print('only letters')
#        continue
#    print('good')
#    break


#while True:
#
#    quest = input('please write (y/n)').lower()
#    c = ('y','n')
#    if quest in c:
#        print('ok')
#        break
#    print('omly y or n' )


# my_tuple = (1,2,3)
# names=('Ani',"Susik","Jhon")
# c = {}
# for i,j in zip(my_tuple,names):
#     c[i] = j
# print(c)


# while True:
# 	num = input('enter number: ')
# 	if num.isdigit():
# 		if int(num) % 2 == 1:
# 			print('enter only even numbers')
# 			break
# 		else:
# 			print('odd number')

# 	else:
# 		print('input only numbers')



# num  = [1,3,2,1,3,1]
# print(list(set(num)))

# x = {'a':1,'b':3}
# y = {'j':6,'k':43}
# c = {**x,**y}
# print(c)



'''my working '''
# set1 = {12,23,'11','hello', True}
# print(set1)

# set_1 = {'apple','banana','kiwi','cherry'}

# for i in set_1:
# 	print(i)

# set_1 = {'apple','banana','kiwi','cherry'}
# print('kiwi' in set_1)     #True, as there are kiwi
# print('orange' in set_1)   #False, as there are not orange


# set_1 = {'apple','banana','kiwi','cherry'}
# set_1.add('melon')
# print(set_1)

# set_1 = {'apple','banana','kiwi','cherry'}
# set_2 = {'pineapple','mango','papaya'}
# set_1.update(set_2)
# print(set_1)

# set_1 = {'apple','banana','kiwi','cherry'}
# set_list = ['orange','melon']     #List can be add in set 
# set_1.update(set_list)
# print(set_1)


# set_1 = {'apple','banana','kiwi','cherry'}
# set_tuple = ('orange','melon')     #Tuple can be add in set 
# set_1.update(set_tuple)
# print(set_1)


# set_1 = {'apple','banana','kiwi','cherry'}
# set_dic = {'orange':3,'melon':5}     # Dictionary can be add in set 
# set_1.update(set_dic)
# print(set_1)


# set_1 = {'apple','banana','kiwi','cherry'}
# set_1.remove('kiwi')
# # set_1.remove('orange')

# print(set_1)


# set_1 = {'apple','banana','kiwi','cherry'}
# set_1.discard('cherry')
# set_1.discard('orange')
# print(set_1)



# set_1 = {'apple','banana','kiwi','cherry'}
# set_3 = {3,11,-5,'a'}
# set_4 = set_1.union(set_3)
# print(set_4)


# set_1 = {'apple','banana','kiwi','cherry'}
# x = set_1.pop()
# print(x)
# print(set_1)

# set_1 = {'apple','banana','kiwi','cherry'}
# set_1.clear()
# print(set_1)

# set_1 = {'apple','banana','kiwi','cherry'}
# del set_1
# print(set_1)


# x = {'apple','banana','kiwi','cherry'}
# y = {'google','microsoft','apple'}
# x.intersection_update(y)          # print e anum hamynknumy 2 set um
# print(x)

# x = {'apple','banana','kiwi','cherry'}
# y = {'google','microsoft','apple'}
# z = x.intersection(y)           #aranc updatei nor popoxakanov veradardznum e hamynknumy 2 set um
# print(z)

set1 = {'apple','banana','kiwi','cherry'}
set2 = {'google','microsoft','apple'}
set3 = set1 & set2      #intersection bari poxaren karox enq & symbvoly grel 
print(set3)

# x = {'apple','banana','kiwi','cherry'}
# y = {'google','microsoft','apple'}
# x.symmetric_difference_update(y)      # veradardznum e 2 set i arjeqnery bacarutyan krknvoxneri
# print(x)

# x = {'apple','banana','kiwi','cherry'}
# y = {'google','microsoft','apple'}
# z = x.symmetric_difference(y)      # aranc update nor popoxakani mijocov veradardznum e 2 seti arjeqnery bacarutyan krknvoxneri
# print(z)


# fruit = {'apple','banana','kiwi','cherry'}
# y = fruit.copy()
# print(y)

# x = {'apple','banana','kiwi','cherry'}
# y = {'google','microsoft','apple'}
# z = x.difference(y)            #  x seti arjeqy kveradardzni bacarutyan y set i het krknvoxneri
# print(z)

# x = {'apple','banana','kiwi','cherry'}
# y = {'google','microsoft','apple'}
# x.difference_update(y)            #  updatei jamanak x seti arjeqy kveradardzni bacarutyan y set i het krknvoxneri
# print(x)

# x = {'apple','banana','kiwi','cherry',3}
# y = {'google',14,3,False,-30,'aa6'}

# print(x.isdisjoint(y))


x = {'a','b','c'}
y = {'e','f','j','a','k','b','l','c'}
z = x.issubset(y)  # print e anum True , ete x Set i bolor arjeqnery kan y Set i mej, ete meky bacakayi, False klini 
print(z)


x = {'e','f','j','a','k','b','l','c'}
y = {'a','b','c'}
z = x.issuperset(y)   
print(z)