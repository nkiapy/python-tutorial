# coding=UTF-8

'''

1. try, except만 쓰는 방법

try:
    ...
except:
    ...
이 경우는 오류 종류에 상관없이 오류가 발생하기만 하면 except 블록을 수행한다.


2. 발생 오류만 포함한 except문

try:
    ...
except 발생 오류:
    ...
이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행한다.


3. 발생 오류와 오류 메시지 변수까지 포함한 except문

try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...
이 경우는 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법

'''

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)


# 여러개의 오류처리하기
print ''
print '='*5 + '여러개의 오류처리하기'

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")


try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)


# try .. else
# else절은 예외가 발생하지 않은 경우에 실행되며 반드시 except절 바로 다음에 위치
print ''
print '='*5 + 'try .. else'

try:
    f = open('foo.txt', 'r')
except IOError as e:
    print(str(e))
else:
    data = f.read()
    f.close()


# try .. finally
# finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
print ''
print '='*5 + 'try .. finally'

try:
    a = 1
    _f = open('foo1.txt', 'r')
except IOError as e:
    print e
finally:
    #_f.close()
    print 'finally'


# 오류 회피하기 (pass)
'''
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass
'''


# 오류 일부러 발생시키기 (raise)
'''
class Bird:
    def fly(self):
        raise NotImplementedError
'''


# 오류 만들기
print ''
print '='*5 + '오류 만들기'
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def say_nick(nick):
    if nick == '바보':
        raise MyError("허용되지 않는 별명입니다.")
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)