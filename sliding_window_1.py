# 1
# 10 3
# 1 2 3 1 5 2 7 8 9 1

def get_ints(): return map(int, input().split())

# input t
t = int(input())

while t != 0 :
    n, k = get_ints()
    a = [int(x) for x in input().split()]
    sum = 0
    for i in range(k): sum += a[i]
    res = sum; idx = 0
    for i in range(k, n):
        sum = sum - a[i - k] + a[i]
        if sum > res:
            res = sum
            idx = i - k + 1
    
    print(res)
    for x in a[idx:idx+k]:
        print(x, end=" ") 
    print("\n")

    t -= 1
 
