import random

cardTuple = (1,2,3,4,5,6,7,8,9)

package = []

while 1:

    print('-------------------------')
    print('    充值让你更强大：')
    print('    请输入指令：')
    print('    1. 抽卡')
    print('    2. 查看背包')
    print('    3. 整理背包')
    print('    4. 离开')
    choose = int(input())

    ## 抽随机卡片，并放到背包
    if choose == 1:
        num = int(input('请输入抽卡次数：'))
        for i in range(num):
            n = random.randint(0,8)
            print('你抽到了卡牌{}'.format(cardTuple[n]))
            ## 放到背包
            package.append(cardTuple[n])

    ## 查看背包
    if choose == 2:
        if len(package) == 0:
            print('背包为空')
        else:
            for i in package:
                print('卡牌{}'.format(i))

    ## 整理背包
    if choose == 3:
        if len(package) == 0:
            print('背包为空')
        else:
            ## 背包排序
            package.sort()
            for i in package:
                print('卡牌{}'.format(i))

    ## 退出
    if choose == 4:
        break
