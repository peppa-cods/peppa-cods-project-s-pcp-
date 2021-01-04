def main():
    num = int(input())
    lists = [int(x) for x in input().split()]
    encounted = 0
    count = 0
    for x in range(num-1):
        if lists[x] > lists[x+1]:
            encounted += 1
            count = num - x -1
        if encounted > 1:
            return -1
         
    if encounted == 0:
        return 0
    elif encounted == 1 and lists[0] >= lists[num-1]:
        return count
    else:
        return -1
print(main())