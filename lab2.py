n=int(input())
arr=input().split()
for e in range(len(arr)):
    arr[e]=int(arr[e])
k=0
for i in range(1,n):
    k=arr[i]
    j=i-1
    while j>=0 and arr[j]>k:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=k
    print(*arr)
    
