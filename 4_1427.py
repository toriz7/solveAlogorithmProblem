#4
N=str(input())
deciN=int(N)
divider=int(10**(len(N)-1))
result=[]
for i in range(len(N)):

    result.append(int(deciN/divider))
    deciN=deciN-divider*int(deciN/divider)
    divider=divider/10

result.sort(reverse=True)
for i in range(len(result)):
    print(result[i],end='')



''' 패스트 캠퍼스 답
N=input()
for i in range(9,-1,-1):
    for j in N:
        if int(j)==i:
            print(i,end='')    
'''