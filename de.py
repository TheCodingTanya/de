# decorator 裝飾器
def print_func(func):
    def inner():
        print('running', func.__name__)  # 拿__name__的屬性
        func()
    return inner   # 把function return出來 -> 成為最後一行的test


def test():
    print('hi')

test = print_func(test)
test()