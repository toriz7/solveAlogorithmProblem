'''
패스트 캠퍼스 카카오 강의
바이너리 서치 관련 코드 적기

'''
#파이썬 리진 탐색 라이브러리 : 특정 범위의 데이터 개수 구하기
from bisect import bisect_left,bisect_right

a=[1,2,3,3,3,3,4,4,8,9]

def count_by_range(a, left_value,right_value):
    right_index=bisect_right(a, right_value)
    left_index=bisect_left(a,left_value)
    return right_index-left_index

print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))


#정확히 값이 x 인 데이터의 인덱스 반환
def index_of_x(a,x):
    i=bisect_left(a,x)
    if i!=len(a) and a[i]==x:
        return i
    return None

# x보다 작은 데이터 중에서, 가장 큰 값의 인덱스를 반환
def index_of_less_than_x(a,x):
    i=bisect_left(a,x)
    if i:
        return i-1
    return None
#x 보다 작거나 같은 데이터 중에서, 가장 큰 값의 인덱스를 반환
def index_of_less_or_equal_than_x(a,x):
    i=bisect_right(a,x)
    if i:
        return i-1
    return None
#x 보다 큰 데이터 중에서 가장 큰 값의 인텍스를 반환
def index_of_greater_than_x(a,x):
    i=bisect_right(a,x)
    if i!=len(a):
        return i
    return None

#x보다 크거나 같은 데이터 중에서, 가장 큰 값의 인덱스를 반환
def index_of_greater_equal_than_x(a,x):
    i=bisect_left(a,x)
    if i!=len(a):
        return i
    return None

#순열 라이브러리
from itertools import permutations
data=[1,2,3]
result=list(permutations(data,3))
print(result)

#조합 라이브러리
from itertools import combinations


def solution(new_id):
    new_id = todown(new_id)
    answer = ''
    return new_id


def todown(id):
    A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'j', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    id = list(id)
    for i in range(len(id)):
        if id[i] in A:
            index = A.index(id[i])
            id[i] = a[index]
    return id


def trim(id):
    id = list(id)
    checklist = ['-', '_', '.']
    for i in range(len(id)):
        if id[i] is
    return str(id)

========================



from itertools import combinations


def solution(orders, course):
    answer = []

    count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
             'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, }
    A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']

    order_count(orders, count, A)
    candi = {}
    # for 문 이용으로 딕션어리 입력 2 이상만
    for i in range(26):
        if count[A[i]] >= 2:
            candi[A[i]] = count[A[i]]

    for i in course:
        makecom(i, count, answer, A)
    print(answer)
    return answer


def makecom(c, count, answer, A):  # c 는 각 코스 개수. 코스 개수 조건에 부합하면 answer 에 추가
    max_dict = max(count.values())
    temp_can = []
    for i in range(max_dict, 1, -1):


def order_count(orders, count, A):
    for i in range(len(orders)):
        for j in range(len(orders[i])):
            for k in range(26):
                if orders[i][j] == A[k]:
                    count[A[k]] += 1
