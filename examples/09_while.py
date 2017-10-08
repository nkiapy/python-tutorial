# coding=UTF-8

# 기본
print '='*5 + '기본'
i = 0
while i <= 10:
    print(i),
    i += 1
print ''

# break
print '='*5 + 'break'
j = 0
while j <= 10:
    if j == 9:
        break
    print(j)
    j += 1
print ''

# continue
print '='*5 + 'continue'
k = 0
while k <= 10:
    k += 1
    if k % 2 == 1:
        continue
    print(k),