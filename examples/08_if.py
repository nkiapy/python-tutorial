# coding=UTF-8

# if else
print ('='*5 + 'if else')
age = 21
if age > 18:
    print ('운전 가능')
else:
    print ('운전 불가능')

# if elif
print ('='*5 + 'if elif')
age = 21
if age >= 21:
    print ('트럭도 운전 가능')
elif age >= 18:
    print ('운전 가능')
else: print ('운전 불가능')

# and or not
print ('='*5 + 'and or not')
age = 30
if age > 1 and age <= 18:
    print ('청소년 입니다.')
elif age ==21 or age >= 65:
    print ('21살이거나 65세 이상입니다.')
elif not age == 30:
    print ('하하하')
else:
    print ('생일 파티합시다.')

# x in s, x not in s
print ('='*5 + 'x in s, x not in s')
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print ('택시를 타고 가라')
elif 'j' not in 'python':
    print ('j가 없음')
else:
    print ('걸어가라')

# pass
# 조건문에서 아무 일도 하지 않게 설정
print ('='*5 + 'pass')
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")