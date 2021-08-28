# tert = [{'a':'145'}, {'b':'1584'}]
# for	i in range(len(tert)):
# 	print(tert[i]['a'])

# set1={12,23,'11', "hello"}
# print(set1)

# this_set = {"apple", "banana", "cherry"}
# for x in this_set:
# 	print(x)

# list1 = [1,5,6,8,5,1,9,15]
# count = 0
# for i in range(len(list1)):
# 	if list1.count(list1[count])>1:
# 		del list1[count]
# 		count -=1
# 	count+=1
# print(list1)
# set1 = {12,23,11}
# set2 = {14,3,141}
# print(set1.is2disjoint(set2))

name = ['ball', 'bat', 'glove', 'glove', 'glove']
price = [2,3,1,2,1]
weight = [2,5,1,1,1]
res =[]
count = 0
res = [[name[i], price[i],weight[i]] for i in range(len(name))]
# for i in range(len(name)):
# 	s = [name[i], price[i],weight[i]]
# 	res.append(s)
# for i in res:
# 	if res.count(i)>1:
# 		count +=1
# print(count)

print(len([i for i in res if res.count(i)>1]))