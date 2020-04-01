from math import pi
from functools import reduce

def str_count(str_):
    # ## set方法获取字符串中所有字符的集合
    # char_list = set(str_)
    # for char in char_list:
    #     ## 遍历每一个字符，并算出字符出现的个数
    #     print(char, str_.count(char))

    # for char in set(str_):
    #     print(char, str_.count(char))

    ## 用字典存储遍历的字符
    countdict = {}
    for char in str_:
        # 查询字符是否存在字典里
        c = countdict.get(char)
        if c is None:
            countdict[char] = 1
        else:
            countdict[char] += 1
    print(countdict)

# s = input('Enter a string: ')
# str_count(s)

def isInstance_int(i):
    if isinstance(i, int):
        return True
    else:
        return False

# 挑选tuple元组里数值>=96的元组
def choose_pp(tuple):
    if tuple[1] >= 96:
        return True
    else:
        return False

def square(x):
    return x ** 2

def add(x, y):
    return x + y

def letters_lower(tuple):
    return tuple[0].lower()

def main():
    numList = [1,3,-5,11,-10,7]

    print(sorted(numList))
    print(sorted(numList, key=abs))

    pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95),('Anthony Davis', 94)]

    print(sorted(pp))

    # filter的用法，filter(a, b)，a是函数，b是数据列表
    list1 = [1, 3, 10, 1.1, 'tomy', abs]
    print(list(filter(isInstance_int, list1)))

    print(list(filter(choose_pp, pp)))

    # map的用法，map(a, b)，a是函数，用来处理b数据，b是可迭代对象
    print(list(map(square, numList)))

    # reduce的用法，reduce(a, b)，用函数a来处理b的数据，add函数类似sum()
    print(reduce(add, numList))
    print(sum(numList))

    # 用map方法把PP里的大写字母转换为小写，并输出
    print(list(map(letters_lower, pp)))

    # 使用lambda函数（lambda后面跟的i是参数，i*2是返回值）
    print(list(map(lambda i:'{:.2f}'.format(i*2*pi), numList)))
    print(list(map(lambda i:i[0].lower(), pp)))

if __name__ == '__main__':
    main()