#4 또는 선택정렬로. 선택정렬은 최소값부터 나오는 정렬방식
N=int(input())
l=[0]*N
for i in range(N):
    temp=int(input())
    l[i]=temp
l.sort()
for i in l:
    print(i)