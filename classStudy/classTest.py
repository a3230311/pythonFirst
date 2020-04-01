# 定义父类Animal
class Animal:
    def __init__(self, name):
        self._name = name

    # 定义格式化打印
    def __repr__(self):
        return 'Animal name: {}'.format(self._name)

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value


# 定义Dog为Animal的子类
class Dog(Animal):
    # 扩展Dog的age属性
    def __init__(self, name, age):
        # super的使用方法，Dog初始化中加入age属性
        # 等同于Animal.__init__(name)
        super().__init__(name)
        self.age = age

# 定义Cat为Animal的子类
class Cat(Animal):
    # 扩展Cat子类的color属性
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

def main():
    myDog = Dog('Tom',10)
    print(myDog)
    print(myDog.get_name())
    print(myDog.age)

    myCat = Cat('cat1', 'red')
    print(myCat)
    print(myCat.get_name())
    print(myCat.color)

if __name__ == '__main__':
    main()