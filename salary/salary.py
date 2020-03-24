import sys

# income = int(input('请输入您的薪资：'))

def calculate(num):
    shouldPay = num - 5000

    if shouldPay <= 0:
        tax = 0
    elif 0 < shouldPay <= 3000:
        tax = shouldPay * 0.03
    elif 3000 < shouldPay <= 12000:
        tax = shouldPay * 0.1 - 210
    elif 12000 < shouldPay <= 25000:
        tax = shouldPay * 0.2 - 1410
    elif 25000 < shouldPay <= 35000:
        tax = shouldPay * 0.25 - 2660
    elif 35000 < shouldPay <= 55000:
        tax = shouldPay * 0.3 - 4410
    elif 55000 < shouldPay <= 80000:
        tax = shouldPay * 0.35 - 7160
    else:
        tax = shouldPay * 0.45 - 15160
    salary = num - tax
    return '{.2f}'.format(salary)

def main():
    # 循环处理每一个用户
    sys.argv[:] = input(print('请输入员工号及薪资，用"："隔开：'))
    # for item in sys.argv[1:]:
    #     id, income = item.split(':')
    #     try:
    #         income = int(income)
    #     except ValueError:
    #         print('请在薪资的位置输入数字')
    #         continue
    #     print('员工ID{}，薪资{}'.format(id,calculate(income)))

if __name__ == '__main__':
    main()


# tax = calculate(income)
# salary = income - tax

# print('你的税费是：{:.2f}'.format(tax))
# print('税后所得：{:.2f}'.format(salary))


## 定义变量
# income = int(input('请输入你的薪资：'))     # 原始收入
# salary = 0                          # 税后收入
# shouldPay = 0                       # 应纳税所得额
# tax = 0                             # 纳税金额
#
# def calculator(num):
#     """计算税后薪资的函数，参数为原始收入"""
#
#     # 应纳税所得额为收入减5000
#     shouldPay = num - 5000
#
#     # 用条件判断语句，根据扣税表写出不同薪资的扣税公式
#     if shouldPay <= 0:
#         tax = 0
#     elif 0 < shouldPay <= 3000:
#         tax = shouldPay * 0.03
#     elif 3000 < shouldPay <= 12000:
#         tax = shouldPay * 0.1 - 210
#     elif 12000 < shouldPay <= 25000:
#         tax = shouldPay * 0.2 - 1410
#     elif 25000 < shouldPay <= 35000:
#         tax = shouldPay * 0.25 - 1410
#     elif 35000 < shouldPay <= 55000:
#         tax = shouldPay * 0.3 - 4410
#     elif 55000 < shouldPay <= 80000:
#         tax = shouldPay * 0.35 - 7160
#     else:
#         tax = shouldPay * 0.45 -15160
#
#     salary = income - tax
#     return '{:.2f}'.format(salary)
#
# print('你的税后收入是：{}'.format(calculator(income)))