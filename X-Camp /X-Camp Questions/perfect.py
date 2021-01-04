num = int(input())

n = 1

while n <= num:

    sum = 0
    divisor = 1
    while divisor < n:
        if not n % divisor:
            sum += divisor
        divisor = divisor + 1
    if sum == n:
        print(n)
    n = n + 1
