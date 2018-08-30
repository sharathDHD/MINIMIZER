#!/bin/python
# def countBits(value):
#     count = 0
#     while value:
#         count += value & 1
#         value >>= 1
# 	return count if count==1 else  0

# def changebit(m,n):
# 	return m[(m^n).bit_length()-1]='x'

def countBits(i,j):
	return sum([1 for x in range(0,len(i)) if i[x] != j[x]])

def changebit(i,j):
	index = sum([x for x in range(0,len(i)) if i[x] != j[x]])
	l = list(i)
	l[index] = 'x'
	return ''.join(map(str, l))

def compare_dict(a,b):
	output = []
	for x in a:
		for y in b:
			if countBits(x,y) == 1:
				# if countBits(i^j) == 1
					output.append(changebit(x,y))
	return output				

min_list =[0,1,2,3,5,7,8,10,12,13,15]
max_ele = len(bin(max(min_list))[2:])
bin_minList = [bin(x)[2:].zfill(max_ele) for x in min_list]
v = [x.replace("0","") for x in bin_minList]
s={}
my_dict = {}   
for i in range(len(v)):
    s[bin_minList[i]]=v[i];


for i,j in s.items():  
	my_dict[len(j)]=[]
	
for i,j in s.items():
    my_dict[len(j)].append(i);

mynewlist = []
min_list = [i for i in my_dict]
count = 0
for i,j in my_dict.items():
	if i == list(my_dict.keys())[-1]:
		break
	for y in min_list:
		mynewlist.append(compare_dict(my_dict[i],my_dict[y]))	
		print(mynewlist)
	min_list.remove(y)
mynewlist = filter(None, mynewlist)
print(mynewlist)

# # #######################################################
# #min_list = [i for i,j in s.items()]
# #print(min_list)
# # for i,j in my_dict.items():
# #     for y in min_list:
# #         mynewlist.append(compare_dict(my_dict[y],my_dict[i]))
# #         min_list.remove(min_list[0])
             

       
# #    print(x,y)
# # mydict ={}