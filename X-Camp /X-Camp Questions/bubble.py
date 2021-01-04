num = int(input())
blist = [int(x) for x in input().split()]
def perform_bubble_sort():
    swapcount =  0
    for j in range(num):
        for i in range(1, num-j):
            if blist[i-1] > blist[i]:
                swapcount += 1
                blist[i-1], blist[i] = blist[i], blist[i-1]
    return swapcount
 
print(perform_bubble_sort())