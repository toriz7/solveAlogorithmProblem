#5  계수 정렬 counting sort : 데이터 범위가 정해져 있고, 개수가 많을 때
import sys
N=int(input())
arr=[0]*10001

for i in range(N):
    input_data=int(sys.stdin.readline())
    #input_data=int(input())  데이터 개수가 많을 때에는 input 보다 sys.stdin.readline() 을 사용하자.
    # 계수 정렬 방법 : if 문 쓰지 말고 바로 인덱싱을 하자.
    arr[input_data]+=1

for j in range(1,10001):
    if arr[j]!=0:
        for k in range(arr[j]):
            print(j)