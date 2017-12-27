# coding=UTF-8

# range
print ('='*5 + 'range')
for i in range(10):
    print (i),
print ('')
for i in range(1, 8):
    print (i),
print ('')

# list
print ('='*5 + 'list')
list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for j in list:
    print (j),
print ('')

# tuple
print ('='*5 + 'tuple')
tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for t in tuple:
    print (t),
print ('')

# 리스트 안에 for문 포함하기
print ('='*5 + '리스트 안에 for문 포함하기')
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)