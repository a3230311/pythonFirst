class User:
    name = 'tomy'

    @classmethod
    def get_name(cls):
        return cls.name

    def __init__(self, name):
        self.name = name

def main():
    print(User.get_name())
    # 不需要对User进行实例化，直接可以修改类属性name的值
    User.name = 'roper'
    print(User.get_name())

    newUser = User('newUserName')
    print(newUser.name)

    print(newUser.get_name())

if __name__ == '__main__':
    main()