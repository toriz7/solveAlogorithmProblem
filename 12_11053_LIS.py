N=int(input())
A=list(map(int,input().split()))

sums=[1]*(N)
for i in range(1,N):
    for j in range(0,i):
        if A[j] < A[i]:
            sums[i]=max(sums[i],sums[j]+1)
print(max(sums))