

n,k = map(int, input().split())
Mat=[[0]*(k+1) for _ in range(n+1)]


for i in range(1,n+1):
    w, value= map(int, input().split())
    for j in range(1,k+1):
        if w>j:
            Mat[i][j]=Mat[i-1][j] # 그대로 옆에것 가져온다
        else:
            Mat[i][j]=max(Mat[i-1][j], Mat[i-1][j-w]+value)
print(Mat[n][k])







'''
n,k=map(int , input().split())
Mat=[[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    w, val = map(int, input().split())
    for j in range(1,k+1):
        if w>j:
            Mat[i][j]=Mat[i-1][j]
        else:
            Mat[i][j]=max(Mat[i-1][j],Mat[i-1][j-w]+val)
print(Mat[n][k])

'''

