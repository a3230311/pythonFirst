# 导入werkzeug创建的hash类
from werkzeug.security import generate_password_hash
# 比较hash值和字符串是否相等
from werkzeug.security import check_password_hash

import io
import json
import os

# password = 'helloworld'
# # 将password转换为hash值
# password_hash = generate_password_hash(password)
# print(password_hash)
#
# print(check_password_hash(password_hash, password))
#
# wrong_password = 'hello'
# print(check_password_hash(password_hash, wrong_password))

# 创建一个用户类
class User:
    def __init__(self, email, password):
        self.email = email
        # 将password转换为hash值赋值给password_hash
        self.password_hash = self.transfer_password(password)

    # 将password转换为hash字符串
    def transfer_password(self, password):
        return generate_password_hash(password)

    # 检查密码和hash值是否相等
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def check_email(self, email):
        return self.email == email

def save_user(email, password):

    password_hash = generate_password_hash(password)
    userInfo_json = {}

    # 读取文件数据，并判断是否存在相同email
    with open('userInformation.json', 'r') as f1:
        # 判断文件内容是否存在，os.path.getsiz返回false/true
        if not os.path.getsize('userInformation.json'):
            with open('userInformation.json', 'w') as f2:
                userInfo_json[email] = password_hash
                json_str = json.dumps(userInfo_json)
                f2.write(json_str)
                print('第一个用户注册成功！')
        else:
            userInfo_json = json.load(f1)
            userInfo_keys = userInfo_json.keys()

            isExist = 0

            for key in userInfo_keys:
                while key == email:
                    isExist = 1
                    print('邮件已存在，请重新注册！')
                    break

            if isExist == 0:
                with open('userInformation.json', 'w') as f2:
                    userInfo_json[email] = password_hash
                    json_str = json.dumps(userInfo_json)
                    f2.write(json_str)
                    print('注册成功！')
    return


def check_user(email, password):
    password_hash = generate_password_hash(password)
    userInfo_json = {}
    with open('userInformation.json', 'r') as f:
        # 判断文件内容是否存在，os.path.getsiz返回false/true
        if not os.path.getsize('userInformation.json'):
            print('没有用户信息，请先注册！')
        else:
            userInfo_json = json.load(f)
            userinfo_keys = userInfo_json.keys()

            isExist = 0

            for key in userinfo_keys:
                while key == email:
                    isExist = 1
                    break

            if isExist == 0:
                print('用户名输入错误，请重新输入！')
            elif isExist == 1:
                if check_password_hash(userInfo_json[email], password):
                    print('登录成功！')
                else:
                    print('密码输入错误，请重新输入！')
    return

def main():
    print('————————————欢迎———————————')
    while 1:
        choose = int(input('''
        1. 注册
        2. 登录
        3. 退出
        ————————————————————
        '''))


        if choose == 1:
            print('————————注册————————')
            email = input('邮箱：')
            password = input('密码：')
            print('————————————————————')
            save_user(email, password)

        if choose == 2:
            print('————————登录————————')
            email = input('邮箱：')
            password = input('密码：')
            print('————————————————————')
            # print(password)
            check_user(email, password)
            print('————————————————————')

        if choose == 3:
            break

if __name__ == '__main__':
    main()