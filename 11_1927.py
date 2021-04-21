import heapq
import sys
N=int(input())
arr=[]
hq=[]
for i in range(N):
    data=int(sys.stdin.readline())
    arr.append(data)

for i in arr:
    if i == 0 and hq:
        print(heapq.heappop(hq))
    elif i==0 and len(hq) == 0:
        print(0)
    else:
        heapq.heappush(hq,i)




