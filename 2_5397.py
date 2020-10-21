#2
T=int(input())
for i in range(T):
    str=input()
    leftstack=[]
    rightstack=[]
    tempstack=[]
    for j in range(len(str)):
        if(str[j]=='<'):
            if leftstack:
                rightstack.append(leftstack.pop())
        elif (str[j]=='>'):
            if rightstack:
                leftstack.append(rightstack.pop())
        elif(str[j]=='-'):
            if leftstack:
                leftstack.pop()
        else:
            leftstack.append(str[j])
    print(leftstack)
    print(rightstack)
    leftstack.extend(reversed(rightstack))
    print(''.join(leftstack))
