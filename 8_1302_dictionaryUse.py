#8  딕션어리 정렬을 마음대로 하는 과정. 중요 가능성
N=int(input())
datas={}
for i in range(N):
    input_data=input()
    if input_data in datas:
        datas[input_data]+=1
    else:
        datas[input_data]=1
# dictionary 함수 : .items(), .values()

target=max(datas.values())
array=[]
for title, number in datas.items():
    if number == target:
        array.append(title)
array.sort()
print(array[0])


'''
print(datas)
bestseller=sorted(datas.items(),key=lambda x:(x[1],x[0]),reverse=True)
print(bestseller)
res=bestseller[0][0]
print(res)
'''