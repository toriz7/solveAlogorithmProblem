#8
# 스스로 풀지 못한 문제.
N,M= map(int, input().split())
Mat=[['.']*M for i in range(N)]
rowcan=0
colcan=0
#입력
for row in range(N):
    input_data=input()
    if 'X' not in input_data:# 해당 행에 경비원 없으면 행을 후보로 넣는다.
        rowcan+=1
    for col in range(M):
        Mat[row][col] = input_data[col]

# 열 검사
for col in range(M):
    check = False
    for row in range(N):
        if Mat[row][col] == 'X':
            check=True
    #마지막까지 없으면
    if check==False:
        colcan+=1
#후보군 정리 완료

#print(max(rowcan,colcan))

if rowcan > colcan:
    print(rowcan)
else:
    print(colcan)


