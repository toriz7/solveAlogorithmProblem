#5
N=int(input())
arr=[]
for i in range(N):
    temp=input().split()
    arr.append( (int(temp[0]) , int(temp[1]) ))

arr.sort()
# 기본 정렬 라이브러리 sort() 의 특징. 여기서는 둘다 증가하는순서대로 한다 : 사실 sort 함수의 특징이며, 아래처럼 key 값 지정 필요가 없는것
#arr.sort(key=lambda x:(x[0], x[1]), )
#arr=sorted(arr,key=lambda x:(x[0],x[1]))

for i in arr:
    print(i[0],i[1])