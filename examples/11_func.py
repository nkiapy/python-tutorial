# coding=UTF-8

"""
def 함수명(인자1, 인자2, ...):
    <수행할 문장1>
    <수행할 문장2>
"""

def add(x, y):
    sum2 = x + y
    return sum2

print(add(2, 3))
print(add(26, 15))

# 입력 인수에 초값 미리 설정
# 초기화시키고 싶은 입력 변수들을 항상 뒤쪽에 위치
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응선", 27, False)