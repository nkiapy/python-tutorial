# coding=UTF-8

import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print (threading.currentThread().getName())

x = Messenger(name="메시지를 보냅니다.")
y = Messenger(name="메시지를 수신합니다.")

x.start()
y.start()

# lambda 변수: 표현식
mul = lambda x: x*7
print (mul(5))