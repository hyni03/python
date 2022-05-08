###########################################################
# 파이썬 기초교육 1주차 과제
# 제출방법: 파일명을 자신의 이름.py로 바꾸고 슬랙을 통해 각 팀 채널에 제출하시면 됩니다.
###########################################################



# Q1
# 세 개의 시험 점수의 평균을 출력하세요.

korean = 80
english = 75
math = 55

avg_=(korean+english+math)/3

print(f"평균 점수: {avg_}" )


###########################################################
# Q2
# 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

pin = "881120-1068234"
# Code here
print(f"{pin[:6]} {pin[7:]}")


###########################################################
# Q3
# [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.

ls = [1, 3, 5, 4, 2]
ls.sort()
# Code here
print(f"{ls}")

###########################################################
# Q4
# ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.

ls2 = ['Life', 'is', 'too', 'short']

# Code here
for i in ls2:
    print(i,end=" ")

print()

###########################################################
# Q5
# 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.

a = b = [1, 2, 3]
a[1] = 4
print(b)
# 여기에 정답 작성

print(id(a),id(b))
#id(a) = id(b)
#같은 주소를 가리키고 있음
