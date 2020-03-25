import json
import csv
import sys

## 计算税后收入
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
    return '{:.2f}'.format(salary)

## 将字典存入文件
def dataOutput(data):
    # 将字典转化为json格式
    json_str = json.dumps(data)

    # 将计算后的json代码写入sys.argv[2]
    with open(sys.argv[2], 'w') as f:
        f.write(json_str)

def main():

    # 定义字典，存放输出的数据
    salary_list = {}

    # 获取脚本后面跟随的第一个代码
    data_file = sys.argv[1]
    usr_csv = csv.reader(open(data_file))
    data_list = list(usr_csv)

    # # 打印测试
    # print(usr_csv)
    # print(type(usr_csv))
    # print(data_list)
    # print(type(data_list))

    for item in data_list:
        id, income = item[0], float(item[1])
        salary = calculate(income)
        salary_list[id] = salary

    dataOutput(salary_list)

if __name__ == '__main__':
    main()