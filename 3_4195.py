#3
T=int(input())
N=int(input())
arr=[]*N
result=0
count=0
for i in range(N):
    temp=input().split()
    name1=temp[0]
    name2=temp[1]
    if name1 in arr or name2 in arr[count]:
        arr[count].add(name1)
        arr[count].add(name2)
    else:
        count+=1 #
        arr[count].add(name1)
        arr[count].add(name2)

for i in arr:
    result+=(len(i)-1)

print(result)