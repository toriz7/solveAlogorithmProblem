
N=int(input())
arr=[0]*(1000000+1)
arr[1]=1 #1
arr[2]=2 # 00, 11  arr[1]+1
arr[3]=3 # 100 001,,111 짝 arr[2]*1+arr[1]*2
arr[4]= 5 # 1100, 1001, 0011,        0000, 1111
for i in range(5,1000000+1):
    arr[i]=(arr[i-1]+arr[i-2])%15746

print(arr[N])