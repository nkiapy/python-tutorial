# coding=UTF-8

list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print (list)

print (list[1:3])

week = ['a', 'b', 'c']
list2 = [week, list]
print (list2[1][1])

# 연산
print ('='*5 + '연산')
week2 = week + list
print (week2)

# list 함수
print ('='*5 + 'list 함수')
print (len(week2))
print (max(week2))
print (min(week2))