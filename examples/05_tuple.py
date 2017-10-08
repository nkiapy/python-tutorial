# coding=UTF-8

# tuple 은 요소 값을 바꿀 수 없다 (immutable한 자료형)
p = (1, 3, 5, 7, 9)
print p
len = len(p)
max = max(p)
min = min(p)
print len
print max
print min

# 인덱싱
print '='*5 + '인덱싱'
print p[1]
print p[-2]

# 슬라이싱
print '='*5 + '슬라이싱'
print p[1:3]
print p[2:]
print p[:4]

# 연산
print '='*5 + '연산'
print p + p
print p * 3

# list <-> tuple 변환
print '='*5 + 'list <-> tuple 변환'
p_list = list(p)
print p_list
p_tuple = tuple(p_list)
print p_tuple