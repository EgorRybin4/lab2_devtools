def quicksort(num):
   if len(num) <= 1:
       return num
   else:
       q = num[0]
       l_num = []
       r_num = []
       m_num = []
       for i in num:
           if i < q:
               l_num.append(i)
           elif i > q:
               r_num.append(i)
           else:
               m_num.append(i)
       return quicksort(l_num) + m_num + quicksort(r_num)
    
p = list(map(int,input().split()))
raft = [ ]
for i in range(p[0]):
    stroka = list(map(int,input().split()))
    raft += stroka
kolvo = int(input())
chel = list(map(int,input().split()))

i = j = k = 0
while i < len (raft) and j < len (chel):
        if raft [i] < chel [j]:
            i += 1
        else:
            k += 1
            j += 1
print(k)
    

























    
