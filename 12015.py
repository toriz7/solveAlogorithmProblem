from bisect import bisect_left,bisect_right
N=int(input())
arr=list(map(int,input().split()))
L=[0]*N
L[0]=arr[0]
index=0

for i in range(1,N):
    #print(L)
    if L[index]<arr[i]:
        index+=1
        L[index]=arr[i]
    else:
        targetindex=bisect_right(L,arr[i],0,index)
        #print(targetindex)
        L[targetindex]=arr[i]
print(N-L.count(0))



