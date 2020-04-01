from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class Permission:
    # 用户身份类
    ROLE_USER = 10 # 普通用户
    ROLE_FORUMADMIN = 20 # 监管员
    ROLE_ADMIN = 30 # 超级管理员

class User:
    # 该类用于创建用户账号
    def __init__(self, name, email, password, role=Permission.ROLE_USER):
        self.name = name
        self.email = email
        self.password_hash = self.save_password(password)
        self.role = role

    def save_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 定义is_admin方法判断用户是否是管理员，要求方法可以像属性一样调用
    @property
    def is_admin(self):
        return self.role == Permission.ROLE_ADMIN

    # 定义修改用户权限的方法
    def change_role(self, role):
        self.role = role

def main():
    newUser1 = User('tom', '123@qq.com', '123456')
    newUser2 = User('roper', '444@163.com', '111111', Permission.ROLE_ADMIN)

    # 判断用户是否是管理员，不是的话修改为管理员
    for user in (newUser1, newUser2):
        if user.is_admin:
            print('{} is Admin'.format(user.name))
        else:
            print('{} is not Admin'.format(user.name))
            user.change_role(Permission.ROLE_ADMIN)
            print('{} is change to Admin'.format(user.name))

if __name__ == '__main__':
    main()