#5

'''
N=int(input())
array=[]

for i in range(N):
    input_data=input().split()
    array.append((int(input_data[0]), input_data[1]))
array=sorted(array,key=lambda x:(x[0]))

for i in range(N):
    print(array[i][0], array[i][1])
'''
N=int(input())
array=[[0]*2 for row in range(N)]

for i in range(N):
    temp=input().split()
    array[i][0] = int(temp[0])
    array[i][1] = temp[1]

array=sorted(array,key=lambda x:(x[0]))

for i in range(N):
    print(array[i][0], array[i][1])
# matrix = [[0 for col in range(10)] for row in range(10)]
#
# 출처: https://andrew0409.tistory.com/53 [코인하는 프로그래머]
#arr.sort(key=lambda x:(x[0]))