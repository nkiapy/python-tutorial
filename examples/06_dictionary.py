# coding=UTF-8

# 튜플은 Key로 쓸 수 있다.
# 딕셔너리의 Key로 쓸 수 있느냐 없느냐는 Key가 변하는 값인지 변하지 않는 값인지에 달려 있다.

dic = {'Monday': '월요일', 'Tuesday': '화요일', 'Wednesday': '수요일',
       'Thursday': '목요일', 'Friday': '금요일', 'Saturday': '토요일',
       'Sunday': '일요일'}
print (dic)
print (dic['Friday'])

# get
print ('='*5 + 'get(key)')
print (dic.get('Friday'))

# len
print ('='*5 + 'len')
print (len(dic))

# 딕셔너리 요소 삭제
del dic['Friday']

# 파이썬 2.7 버전까지는 a.keys() 호출 시 리턴값으로 리스트를 리턴
# 리스트를 리턴하기 위해서는 메모리의 낭비가 발생하는데 파이썬 3.0 이후 버전에서는 이러한 메모리 낭비를 줄이기 위해 dict_keys 라는 객체를 리턴
# keys()
print ('='*5 + 'keys()')
print (dic.keys())

# 파이썬 2.7 버전까지는 a.values() 호출 시 리턴값으로 리스트를 리턴
# 파이썬 3.0 이후 버전에서는 이러한 메모리 낭비를 줄이기 위해 dict_values 라는 객체를 리턴
# values()
print ('='*5 + 'values()')
print (dic.values())

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print ('='*5 + 'in')
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print ('name' in a)
print ('email' in a)

# Key: Value 쌍 모두 지우기(clear)
print ('='*5 + 'clear')
a.clear()
print (a)