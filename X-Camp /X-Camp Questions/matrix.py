list=[]
r = [int(x) for x in input().split()]
for i in range(r[0]):
    list.append(input().split())
for x in range(r[1]):
	colum_ones = 0
	for j in range(r[0]): 
		colum_ones += int(list[j][x])
	print(colum_ones)