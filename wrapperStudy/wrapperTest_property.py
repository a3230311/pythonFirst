class User:
    def __init__(self, name, email, *password):
        self.name = name
        self.email = email
        self._password = list(password)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        # self._password = password
        self._password.append(password)

    @password.deleter
    def password(self):
        # del self._password
        self._password.pop(-1)

def main():
    newUser = User('Tomy', 'tomy@163.com', '123')
    print(newUser.name)
    print(newUser.email)
    print(newUser.password)

    newUser.password = '456'
    print(newUser.password)

    newUser.password.pop()
    print(newUser.password)

if __name__ == '__main__':
    main()