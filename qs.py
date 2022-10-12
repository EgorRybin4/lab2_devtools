import random
n=int(input())
arr=list(map(int,input().split()))
def qs(array,s,b):
    if s >= b:
        return array
    i, j = s, b
    d = array[random.randint(s, b)]
    while i <= j:
        while array[i] < d:
            i += 1
        while array[j] > d:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    qs(array, s, j)
    qs(array, i, b)
qs(arr,0,n-1)
print(*arr)
