list1 = []
num = int(input())
for x in range(0,num):
	nums = int(input())
	list1.append(nums)
list1.sort(reverse=True)

for i in range(int(num/2)):
	print(list1[i])
	print(list1[num-i-1])
	
if (num%2 != 0):
	print(list1[num-i-2])



