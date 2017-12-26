# coding=UTF-8

"""
class 클래스이름[(상속 클래스명)]:
    <클래스 변수 1>
    <클래스 변수 2>
    ...
    def 클래스함수1(self[, 인수1, 인수2,,,]):
        <수행할 문장 1>
        <수행할 문장 2>
        ...
    def 클래스함수2(self[, 인수1, 인수2,,,]):
        <수행할 문장1>
        <수행할 문장2>
        ...
    ...
"""
# 클래스
class DuckHunting:
    ducks = 3 # 클래스 변수
    def __init__(self, power):
        self.power = power
        print ("Dog's power is %d" % self.power)

    def hunting(self):
        print ("Catch!")
        self.ducks -= 1
        if self.ducks < 0:
            self.ducks = 0

    def checkDucks(self):
         if self.ducks <= 0:
             print ("Good Dog!")
         else:
             print (str(self.ducks) + " Ducks left")

dog1 = DuckHunting(1)
dog1.hunting()
dog1.checkDucks()
print (DuckHunting.ducks)

dog2 = DuckHunting(15)
dog2.checkDucks()

import sys
print (sys.version)

# 상속(Inheritance)
print ('')
print ('='*5 + '상속(Inheritance)')
class Parent():
    def print_last_name(self):
        print ("KingKong")

class Child(Parent):
    def print_first_name(self):
        print ("Amy")

    # overriding
    def print_last_name(self):
        print ("Monkey")

amy = Child()
amy.print_first_name()
amy.print_last_name()

# 다중상속(Multiple Inheritance)
print ('')
print ('='*5 + '다중상속(Multiple Inheritance)')
class Amy():
    def print_last_name(self):
        print ("Monkey")

class Lex():
    def print_first_name(self):
        print ("Lex")

class AmyLex(Amy, Lex):
    pass

amyLex = AmyLex()
amyLex.print_first_name()
amyLex.print_last_name()

# __add__, __sub__(+,- 연산자)
print ('')
print ('='*5 + '+,- 연산자')
class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 헤어졌네" % (self.fullname, other.fullname))


class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where):
        print("%s은 %s로 여행합니다." % (self.fullname, where))

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey + juliet    # + 연산자를 객체에 사용하게 되면 HousePark 클래스의 __add__ 라는 메서드가 자동으로 호출
pey - juliet    # - 연산자를 객체에 사용하게 되면 HousePark 클래스의 __sub__ 라는 메서드가 자동으로 호출
