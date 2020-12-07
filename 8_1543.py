#8
string=input()
target=input()
destination=len(string)-len(target)
count=0
loc=0
while(loc <= destination): #마지막 끝을 카운트하기 위해 =
    temp_string=string[loc:loc+len(target)]

    if temp_string == target:
        loc+=len(target)
        count+=1
    else:
        loc+=1
print(count)
