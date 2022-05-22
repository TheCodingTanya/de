# decorator 裝飾器
import time

def print_func(func):
    def inner():
        print('running', func.__name__)  # 拿__name__的屬性
        func()
    return inner   # 把function return出來 -> 成為最後一行的test

def time_func(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('elapsed', end - start, 'seconds')
    return inner



def test():
    for i in range(10000000):
        i = i + 1

def test2():
    print('ni hao')

# test()
# print('加工中')
test = time_func(test)
test2 = time_func(test2)
test()
test2()

# import time

# start = time.time()
# test()
# end = time.time()
# print('elapsed', end - start, 'seconds')