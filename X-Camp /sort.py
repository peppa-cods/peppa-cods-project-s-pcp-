num = int(input())
num_list = [int(x) for x in input().split()]
steps = 0

while finished == False:
	a1 = ['1', '5-10', '12', '18', '23', '100-110', '16-17', '20','2']
a_dict = {int(v.split('-')[0]): v for v in a1}
final_a = [a_dict[k] for k in sorted(a_dict)]
print (final_a)
finished  = True
