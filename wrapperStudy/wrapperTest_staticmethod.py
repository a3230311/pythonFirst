class Cat:
    owner = 'Miss House'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def get_cat_food():
        print(__class__.owner, 'go to pet shop...')
        print('Buy cat food and back.')

def main():
    Cat.get_cat_food()

if __name__ == '__main__':
    main()