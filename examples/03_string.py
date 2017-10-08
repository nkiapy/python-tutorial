# coding=UTF-8

abc='12'
c = "%d 250" % 5
d = """
dfsadfdf
%s
dsfddf
""" % "우헤헤"
print (abc + c + d)

# format
print '='*5 + 'format'
f = "I eat {0} apples".format(3)
print f

number = 10
day = "three"
f1 = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print f1

f2 = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print f2