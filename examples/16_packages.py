'''

__init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
만약 game, sound, graphic등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.

(※ python3.3 버전부터는 __init__.py 파일 없이도 패키지로 인식이 된다(PEP 420).
하지만 하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전한 방법이다.)

'''


# __init__.py 에서 all 용
# import * 에서 echo, bar 모듈을 import할 것을 명시
# __all__ = ['echo', 'bar']

# relative한 접근자
# from ..sound.echo import echo_test
# ..    – 부모 디렉터리
# .     – 현재 디렉터리
# relative한 접근자는 모듈 안에서만 사용해야 한다.


# 패키지 안의 함수 실행하기
######################################
# import modules.mod1
# modules.mod1.hello()

# from modules import mod1
# mod1.hello()

# from modules.mod1 import hello
# hello()

# import a.b.c처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.
# import modules.mod1.hello (X)
######################################