from datetime import datetime
from functools import wraps

def print_time(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print(datetime.now())
        func(*args, **kw)
    return wrapper

# 在调用hello()函数的时候，会优先执行print_time里的wrapper函数
@print_time
def hello(name):
    print('my name is: {}'.format(name))

def main():
    hello('tomy')

if __name__ == '__main__':
    main()