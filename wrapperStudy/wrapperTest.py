from datetime import datetime
# import datetime

def print_datetime(func):
    # 传入可变参数args和关键字参数kw
    def wrapper(*args, **kw):
        print(datetime.now())
        func(*args, **kw)
    return wrapper

def hello(name, age):
    print('my name is: {}\nmy age is: {}'.format(name,age))

def main():
    wrapper = print_datetime(hello)
    wrapper('tom', 2)
    # 能直接调用hello()函数，但是不会调用wrapper
    hello('roper', 3)
    print(hello.__name__)

if __name__ == '__main__':
    main()