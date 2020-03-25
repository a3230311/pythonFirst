class Dog():
    # age = 1
    # name = 'tom'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Dog-name:{}\nDog-age:{}'.format(self.name,self.age)

def main():
    # myDog = Dog()
    myDog = Dog('tom',3)
    # print(myDog.name)
    # print(myDog.age)
    # print(dir(myDog))

    # myDog.age = 3
    # print(myDog.age)

    print(myDog)

if __name__ == '__main__':
    main()