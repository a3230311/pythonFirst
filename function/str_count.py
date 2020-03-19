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

s = input('Enter a string: ')
str_count(s)