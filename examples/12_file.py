# coding=UTF-8

# 문자열 인덱싱/슬라이싱
print '='*5 + '문자열 인덱싱/슬라이싱'
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print alphabet[0:3]
print alphabet[-3:]
print alphabet[:-3]
print alphabet[:3] + " Hello"

# 문자열 함수
print '='*5 + '문자열 함수'
print alphabet.capitalize()
print len(alphabet)
print alphabet.replace("A", "B")
a = "Life is too short"
print a.split()
a = "a:b:c:d"
print a.split(':')

# 문자열 포매팅 / 튜플
print '='*5 + '문자열 포매팅'
print "나는 %d 살 이구요, 몸무게는 %.1f kg 이구요, 취미는 %s 입니다." % (20, 68, "영화보기")

# 파일 입출력
print '='*5 + '파일쓰기'
t_file = open("t.txt", "wb")
print t_file.name
print t_file.mode
t_file.write(bytes("안녕하세요.\n"))
t_file.close()

print '='*5 + '파일읽기'
t_file = open("t.txt", "r")
r = t_file.read()
print r
t_file.close()

# 파일쓰기(쓰기모드 range 값을 바꾸면서 획인)
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# readline 으로 읽기
print '='*5 + 'readline 으로 읽기'
f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# readlines 로 읽기(readlines() 함수는 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴)
print '='*5 + 'readlines 으로 읽기'
f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# read 로 읽기(파일의 내용 전체를 문자열로 리턴)
print '='*5 + 'read 으로 읽기'
f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()