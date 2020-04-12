# 型と変数
a = 1
type(a)  # int
'''取り込む型
整数
浮動小数点
配列
文字列
真偽
辞書型 '''

# クラスは型である
'''class: name
    variable=value'''


class Person:
    pass


'''class: name
    variable=value'''


class Person:
    species = 'Homo sapiens'
    number = 1


print(Person.species)
print(Person.number)


# Personクラスは全て、speciesとnumberと言うクラス変数を所有（しょゆう）

# 演習問題
# クラス宣言

class Animal:
    number = 0


# print  Object_name.variables
print(Animal.number)

# How to create objects  object_name= class_name
# インスタンス変数を追加  add instance to the object Juan(Person +new instance)
Juan = Person()
Juan.name = 'Juan'
Juan.age = 22
print(Juan.name)
print(Juan.age)
print(Juan.number)

# オブジェクトcatを宣言する
cat = Animal()
cat.name = 'meow'
cat.type = type(cat)

print(cat.name)
print('cat is :', cat.type)


# クラスを使う関数
# クラスを引数にする use a class object as a variable
def nemu1(person):
    print(person.name)


nemu1(Juan)


# 関数の返り値(かえりち）にクラスを使う　Make a function that returns an object

def nemu2(name):
    p = Person()
    p.name = name

    return p


Bob = nemu2('Bob')
Elle = nemu2('Elle')
print(Bob.name, Elle.name)


# Animalクラスのオブジェクトを返す関数を作成する


# Doesnt need a variable to work (properties of the class )
def nemu3():
    A = Animal()
    return A


dog = nemu3()
print(type(dog))

# constructor
# after calling class object you will always get the constructor function
''' class 名：
　　　def_init_(self):　always self
      関数の中身'''


class Person:
    species = 'Homo sapiens'
    number = 1

    def __init__(self):  # two _
        print('This is a constructor')


Person()

# constructor
# after calling class object you will always get the constructor function
''' class 名：
　　　def_init_(self):　always self
      関数の中身'''


class Person:
    species = 'Homo sapiens'
    number = 1

    def __init__(self):  # two _
        print('This is a constructor')


Person()

# コンストラクタに引数を追加
''' def__init__(self,引数1,引数２)：
        self.インスタンス変数＝　引数1
        。。。
'''


class Person:
    species = 'Homo sapiens'
    number = 1

    # add variables after self
    def __init__(self, name_arg, age_arg):
        print('Im a constructor')
        self.name = name_arg
        self.age = age_arg


Bob = Person('Bob', 22)

print(Bob.name)
print(Bob.age)


# コンストラクタでクラス変数を操作
class Person:
    species = 'Homo sapines'
    number = 1

    def __init__(self, name_arg, age_arg):
        print('Im a constructor')
        self.name = name_arg
        self.age = age_arg
        # cool
        Person.number += 1
        # not cool  n　numberがインスタンス変数に変化してしまう get 3 (Person +Object)
        self.number += 1


Pablo = Person('Pablo', 22)
print('Pablo number', Pablo.number)
print('Person number', Person.number)


# デストラクタ
class Person:
    species = 'homosapines'
    number = 1

    def __init__(self, name, age):
        print('Im a constructor')
        self.name = name
        self.age = age
        Person.number += 1

    def __del__(self):
        print('This is a deconstructor')
        Person.number -= 1


Janela = Person('Janela', 54)
print(Janela.name, Person.number)
print("-----/----")
del Janela
print(Person.number)


# Animalクラスのコンストラクタにおいて、nameとｓp引数s、ageをひきすう
class Animal:
    def __init__(self, name_arg, species_arg, age_arg):
        print('Animal constructor')
        self.name = name_arg
        self.species = species_arg
        self.age = age_arg


Cat = Animal("meow", "cat", 5)
print(Cat.name, Cat.species, Cat.age)


# デストラクタにおいて、オブジェクトが消除されたことを示す適当な文言をだす　
class Animal:
    def __init__(self, name_arg, species_arg, age_arg):
        print('Animal constructor')
        self.name = name_arg
        self.species = species_arg
        self.age = age_arg

    def __del__(self):
        print('Destroying the Object ', self.name)


Cat = Animal("meow", "cat", 5)
del Cat

# Method メソッドひＫ Functions inside the class object
''' class クきすス名：
        def 関数名（self,引数、..）
        〜中身〜
referred as cf
'''


class Person:
    species = 'Homo Sapiens'
    number = 1

    def __init__(self, name_arg, age_arg):
        self.name = name_arg
        self.age = age_arg
        Person.number += 1

    def birthday(self):
        print('Today is ' + self.name + " birthday")
        self.age += 1

    @classmethod
    def get_species(cls):
        print("This guy is " + cls.species)
        print(cls)


Juan = Person('Juan', 22)
Juan.birthday()
print(Juan.age)

Person.get_species()






class Animal:
    number = 0

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def me(self):
        print('my name is ' + self.name)

    def older(self):
        self.age += 1
        print('I will be ' + str(self.age) + ' years old')

    '''def add_num(self):
            Animal.number += 1
    '''

    @classmethod
    def aDD(cls):
        cls.number += 1
        print('number : ' + str(cls.number))


Juan = Animal('Juan', 'Alien', 22)
Juan.me()
Juan.older()
Animal.aDD()
print('Animal number ' + str(Animal.number))
print('Juan number ' + str(Juan.number))
# Juan.add_num()
# print(Animal.number)
# 疑似プライベート  __変数名 pseudo private two downbars
'''
class ClassName():
    def __init__(self,arg):
        self.__arg = arg 
'''


class Person:
    species = 'Homo Sapiens'
    number = 0

    def __init__(self, name, age):
        print('Welcome to the class object')
        self.__name = name
        self.__age = age
        Person.number += 1

    def birth(self):
        print(self.__name + ' birthday')

    def __change_name(self, new_name):
        sel.__name = new_name

    @classmethod
    def spe(cls):
        print('This individual is (a/an)' + cls.species)
        print(cls)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 0:
            self.__name = name
            return

        raise ValueError('your name needs more than one character')


Kuro = Person('kuro', 22)
print(Kuro.name)
Kuro.name = 'shiro'
print(Kuro.name)
# Kuro.name = ''  # ValueErrorをこちらで設定できるようになった（通常との違い）
print(Kuro.name)


# 演習　6
class Animal:
    number = 0

    def __init__(self, name, species, age):
        print('Constructor')
        self.name = name
        self.__age = age  # 変更箇所（かしょ）
        self.species = species

    def get_name(self):
        print(self.name)

    @classmethod
    def add_num(cls):
        cls.number += 1
        print('specimen is number:' + str(cls.number))

    def over(self):
        print('I am Animal')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):

        if type(age) == int:
            if age > 0:
                self.__age = age
                return
            raise ValueError('Your age needs to be positive')
        raise ValueError('Your age needs to be an integer')


Bob = Animal('Bob', 'dog', '13')
print('Bob age is ' + str(Bob.age))
# Bob.age = 'age'
# Bob.age = 0
Bob.get_name()
Animal.add_num()
print(Bob.age)

# 継承


''' class 子クラス（親クラス）  子は親クラスのメンバー
　　　　　pass'''


class NewAnimal(Animal):
    pass

new_bob = NewAnimal('bob', 'dog', 6)
new_bob.add_num()
new_bob.get_name()


# Overwrite

class Parent:
    def say(self):
        print('IM YOUR FATHER CLASS')


class Child(Parent):
    def say(self):
        print('IM YOUR CHILD CLASS')


A = Parent()
B = Child()
A.say()
B.say()

# 子クラスで親クラスのメソッドを呼び出すsuper()
# Initialize constructor from Parents with super()

''' class child(Paraent):
        def __init__(self,arguments...);
            super().__init__(arguments)
                special agruments of child特有の処理'''


class NewAn(Animal):

    def __init__(self, name, species, age, ability):
        super().__init__(name, species, age)
        self.ability = ability


new_meow = NewAn('meow', 'cat', 10, '寝る')
print(new_meow.ability)
new_meow.get_name()


# 演習問題7
class Animal:
    number = 0

    def __init__(self, name, species, age):
        print('Constructor')
        self.name = name
        self.__age = age  # 変更箇所（かしょ）
        self.species = species

    def get_name(self):
        print(self.name)

    @classmethod
    def add_num(cls):
        cls.number += 1
        print('specimen is number:' + str(cls.number))

    # over_write
    def over(self):
        print('I am Animal The parent')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):

        if type(age) == int:
            if age > 0:
                self.__age = age
                return
            raise ValueError('Your age needs to be positive')
        raise ValueError('Your age needs to be an integer')


class NewA(Animal):
    def __init__(self, name, species, age, beard):
        super().__init__(name, species, age)
        # or condition ()|()
        if (beard is True) | (beard is False):
            self.beard = beard
            return
        raise ValueError('baerd should be boolean ')

    def over(self):
        print('I am NewA the child')


Cat = NewA('Garfield', 'cat', 5, False)
Bob = Animal('Bob', 'dog', 6)
print(Cat.beard)
Bob.over()
Cat.over()


# 関数オブジェクト
class Person:
    species = 'Homo Sapiens'
    number = 0

    def __init__(self, name, age):
        print('Welcome to the class object')
        self.__name = name
        self.__age = age
        Person.number += 1

    def birth(self):
        print(self.__name + ' birthday')

    def __change_name(self, new_name):
        self.__name = new_name

    @classmethod
    def spe(cls):
        print('This individual is (a/an)' + cls.species)
        print(cls)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 0:
            self.__name = name
            return

        raise ValueError('your name needs more than one character')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):

        if type(age) == int:
            if age > 0:
                self.__age = age
                return
            raise ValueError('Your age needs to be positive')
        raise ValueError('Your age needs to be an integer')


class NewPerson(Person):

    def __init__(self, name, age, ability):
        super().__init__(name, age)
        self.ability = ability

    def __call__(self):
        print('This is an function object')


New_Koyomi = NewPerson('Koyomi', 18, 'vampire')
print(New_Koyomi.ability)
New_Koyomi()


# 演習問題8

class Animal:
    number = 0

    def __init__(self, name, species, age):
        print('Constructor')
        self.name = name
        self.__age = age  # 変更箇所（かしょ）
        self.species = species

    def get_name(self):
        print(self.name)

    @classmethod
    def add_num(cls):
        cls.number += 1
        print('specimen is number:' + str(cls.number))

    # over_write
    def over(self):
        print('I am Animal The parent')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):

        if type(age) == int:
            if age > 0:
                self.__age = age
                return
            raise ValueError('Your age needs to be positive')
        raise ValueError('Your age needs to be an integer')


class Animal_voice(Animal):
    def __init__(self, name, species, age, mood):
        super().__init__(name, species, age)
        self.mood = mood

    def __call__(self):
        print(self.name + ' ですにゃ〜')


Cat_nya = Animal_voice('Nyanko Sensei', 'youkai', 500, 'bwe')
print(Cat_nya.mood)
Cat_nya()
