import heapq
N=int(input())
hq=[]
for i in range(N):
    data=int(input())
    heapq.heappush(hq,data)

a=0
b=0
result=[]
while hq:
    if len(hq)==1:
        print(sum(result))
        break
    else:
        a=heapq.heappop(hq)
        b=heapq.heappop(hq)
        a=a+b
        result.append(a)
        heapq.heappush(hq,a)

