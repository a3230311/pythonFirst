# from collections import Iterable

# 用迭代器实现斐波那契数列
class Iter:
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration('超过了n')
        return self.a

# 用生成器yield实现斐波那契数列
def fib(n):
    current = 0
    a = b = 1
    while current < n:
        yield a
        a, b = b, a + b
        current += 1

def main():
    print(list(Iter(100)))
    print(list(fib(10)))

if __name__ == '__main__':
    main()