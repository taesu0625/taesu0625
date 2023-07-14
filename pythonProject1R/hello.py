# print('Hello world!')
#
#
# # 변수명 : 영문소문자로 시작(권고) 뜻을 알수 있는 단어(권장) 숫자로 시작 X 특수문자_로 시작 가능
# # 숫자, 문자, 참거짓( True / False )
# a = 'hello'
# b = False
# b = 10
#
# str1 = 'abc'
# str2 = "abc"
# # 따옴표, 쌍따옴표 둘다 가능하나 혼용금지(권고)
#
# # 문자열 : 변경 불가능
# name = 'kim ssafy'
# greeting = '안녕하세요 홍길동입니다.' # <<하드코딩
# # 문자열 안에 변수값을 넣고 싶을때 사용하는 > string interpolation
# # fString 활용
# greeting = f'안녕하세요 {name}입니다.'
# print(greeting)
# # #1 정답
# # print(f'#{number} {정답}')형태로 쓰시면 됩니다.


# ----------------------------------------------------------------------------------------
#
# # 데이터를 저장할 때는 변수에 저장한다
# # 데이터 여러개를 동시에 처리할 때는??
# # 변수 여러개 X -> 덩어리데이터(구조)에 저장
# score1 = 100
# score2 = 90
# score3 = 95
# # 배열 Array >>> 리스트 []
# scores = [100, 90, 95]
# print(scores[1])      # 0번부터 시작 (인덱스 Index)
# scores[1] = 110
# print(scores[1])      # 변경 가능 mutable   ex) 리스트
# print(a[1])
# # a[1] = a  --> 에러            # 변경 불가능 immutable   ex)문자열
# # 순서를 가지고 있는 것 (시퀀스)
#
# scores2 = (100, 90, 95)   # 튜플, immutable
# print(scores2[2])
# # scores2[2] = 100  --> 에러
# # print(scores2[2])

# -------------------------------------------------------------------------------------------

# # input
# # 100 90 95 리스트 or 튜플에 어떻게 입력하지?
# # 입력받기 input()  함수호출(사용)
# # input()  : 키보드에서 엔터 칠때 까지 내용을 입력받음
# #            표준 입력에서 문자열 한줄을 읽어오는 것
# # 표준입력을 파일입력(파일에서 읽어오기)으로 변경하기
# import sys
# sys.stdin = open('input.txt', 'r')
# # sys.stdout = open('output.txt', 'w')   # 'w' 생략 불가
# # data = input().split()
# # 덩어리 데이터의 각 욧에 똑같은 일을 하고 싶을때  사용하는 함수
# # map(할일, 덩어리 데이터)
# # 문자열 > 숫자로 바꾸는 함수 int
# # list(map(int, data))   # list(map(int, input().split()))
# print(list(map(int, input().split())))         # split(',') 콤마를 기준으로 가르기 (기본은 띄어쓰기)

# # 32532592
# # 각 자리 수를 리스트에 저장하고 싶다.
#
# data = list(map(int, input()))
# print(data)

# -------------------------------------------------------------------------------------------

# # 리스트 만들기
# arr = [100, 90, 95]
# # 데이터는 안들어가 있는데... 100개자리 리스트를 만들고 싶다.
# arr = [0] * 100
# print(arr)

# 1부터 100까지 정수가 들어있는 리스트 만들기
# List Comprehension 사용
# arr = [x for x in range(1, 101)]
# print(arr)

# # --------------- list 사용 (변수를 한꺼번에 만들어 내는)(반복문 사용하려고)------------------------------------
# arr = [0] * 10
# arr[2] = 500
# print(arr)

# # 반복문으로 모든 요소에 접근하기
arr = [100, 200, 300, 400, 500]
# # 파이썬 for문 문법은  for ~~(꺼내오는 애들) in ~~(덩어리 데이터) :
# # for 문은 어떤 문장을 반복
# for a in arr:
#     print(a)
# # 리스트의 모든 요로를 출력.. 인덱스 이용 (range)      in 뒤쪽은 이터러블 데이터
# for i in range(5):
#     print(arr[i])
# for i in range(len(arr)):
#     print(arr[i])
# # 이터러블 (하나하나 집어낼수 있다)

# ---------------------------------------------------------------------------------------

# # 짝수번째 인덱스를 어떻게 출력하는가
# # 인덱스가 짝수인애를 찾으면 됨
# # 어떻게 찾는가? 검사하면 됨
# # if i 가 짝수이면: -> 결과는 참 거짓
# #   문장
# #   문장
# for i in range(len(arr)):
#     if i % 2 == 1:
#         print(arr[i])
# # 위에서부터 내려오는 흐름을 바꾸는 것 -> 제어문 (반복문, 조건문, 실행문)

# -----------------------------------------------------------------------------------------
#
# # 딕셔너리
# # key - value 형태로 저장가능한 자료구조
# d = {
#     '국어' : 100,
#     '수학' : 80,
#     '영어' : 90
# }
# print(d['영어'])
# # 추가
# d['과학'] = 77
# print(d)

# 최빈수
# input =  5 4 3 7 5 1 3 2 4 5      # 1~10중 (많이 나온 수를 찾는) 몇번 나왔는지 저장
# 입력부터 받기 (리스트에 숫자로 저장하기)
# 숫자를 세기 위해 딕셔너리 만들기                                           set??
dic = dict()
# 1부터 10까지 키값에 0을 매핑 시켜주기
for num in range(1, 11):
    dic[num] = 0
print(dic)
numbers = list(map(int, input().split()))
print(numbers)
for number in numbers:
    dic[number] += 1

print(dic)

# 제일 많이 나온 애를 찾고 싶으면?
# 제일 많이 나온애만 몇번나왔는지 알면 됨
max_num = 0
max_count = 0
for el in dic:
    # print(el ,dic[el])
    # dic[el] : 각 숫자 (el)가 몇번 나왔는지를 가진 변수
    if dic[el] > max_count:
        max_count = dic[el]
        max_num = el
print(max_num, max_count)