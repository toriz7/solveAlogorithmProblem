#3
n=int(input())
array=set(map(int, input().split() )) # 중복되는 것은 필요 없으니까
m=int(input())
x=list(map(int, input().split()))
for i in x:
    if(i in array):
        print('1')
    else:
        print('0')

'''
A=int(input())
temp=input().split(' ')

arr1=[]
for i in range(A):
    arr1.append(int(temp[i]))

B=int(input())
temp=input().split(' ')
arr2=[]
for i in range(B):
    arr2.append(int(temp[i]))

result=[]

for i in range(B):
    if(arr2[i] in arr1):
        result.append(1)
    else:
        result.append(0)

for i in range(len(result)):
    print(result[i])
'''