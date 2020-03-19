import random
import time

cardTuple = ('豆豆','西渚','房子','邦平','凯尔文','弹弹','俊杰','东洋','韩兴')

# package = []

## 定义字典背包
package_dict = {}

## 定义抽卡权重
card_weight = (0,5,10,20,50,100,200,400,800)

while 1:

    print('-------------------------')
    print('    跟我一起翻牌子：')
    print('    请输入指令：')
    print('    1. 翻牌子')
    print('    2. 今晚睡几次')
    # print('    3. 整理背包')
    print('    4. 离开')
    choose = int(input())

    ## 当用户输入1的时候，翻牌子
    if choose == 1:
        num = int(input('请输入翻牌次数：'))

        for x in range(0,num):
        ## 生成0到card_weight[-1]之间的随机数
            random_int = random.randint(0,card_weight[-1])

            ## 定义起点i=0，当radom_int的值大于card_weight[i]，则i+1
            i = 0
            while random_int > card_weight[i]:
                i += 1

            if 0 <= random_int <= 5:
                print('你翻到里SSR后宫佳丽：{}'.format(cardTuple[i]))
            elif 5 < random_int <= 20:
                print(print('你翻到里SR后宫佳丽：{}'.format(cardTuple[i])))
            elif 20 < random_int <= 100:
                print('你翻到里R级后宫佳丽：{}'.format(cardTuple[i]))
            else:
                print('你翻到了男人：{}'.format(cardTuple[i]))

            ## 每0.3秒循环一次
            time.sleep(0.3)

            ## 把翻到的牌子放入字典
            if package_dict.__contains__(cardTuple[i]):
                package_dict[cardTuple[i]] += 1
            else:
                package_dict[cardTuple[i]] = 1
        print('---------------')
        print('美女们已进房间')
        print('---------------')

    if choose == 2:
        ## 当没有卡片的时候
        if len(package_dict) == 0:
            print('后宫佳丽都没在')
        else:
            for key,value in package_dict.items():
                print('{} 今晚跟你睡 {} 次'.format(key,value))
            print('--------------------')

    # ## 抽随机卡片，并放到背包
    # if choose == 1:
    #     num = int(input('请输入翻牌次数：'))
    #     for i in range(num):
    #         n = random.randint(0,8)
    #         print('你抽到了{}'.format(cardTuple[n]))
    #         ## 放到背包
    #         package.append(cardTuple[n])
    #
    # ## 查看背包
    # if choose == 2:
    #     if len(package) == 0:
    #         print('背包为空')
    #     else:
    #         for i in package:
    #             print('卡牌{}'.format(i))

    # ## 整理背包
    # if choose == 3:
    #     if len(package) == 0:
    #         print('背包为空')
    #     else:
    #         ## 背包排序
    #         package.sort()
    #         for i in package:
    #             print('卡牌{}'.format(i))

    ## 退出
    if choose == 4:
        break
