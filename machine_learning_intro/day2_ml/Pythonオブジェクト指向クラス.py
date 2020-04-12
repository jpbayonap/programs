
# coding: utf-8

# # 演習問題1

# In[25]:


class Animal():
    number = 0
print(Animal.number)


# # 演習問題2

# In[27]:


cat = Animal()
cat.name = "Kitty"
print(cat.name)


# # 演習問題3

# In[ ]:


def create_Animal(age, name):
    a = Animal()
    a.age = age
    a.name = name
    return a

dog = create_Animal(3, "Pochi")
print(dog.age, dog.name)


# # 演習問題4

# In[28]:


class Animal():
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def __del__(self):
        print("オブジェクトが削除されました")
        
cat = Animal("Kitty", "cat", 3)
del cat


# # 演習問題5

# In[32]:


class Animal():
    
    number = 0
    
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def __del__(self):
        print("オブジェクトが削除されました")
        
    def get_name(self):
        print(self.name)
        
    def add_age(self):
        self.age += 1
    
    @classmethod
    def add_number(self):
        self.number += 1

cat = Animal("Kitty", "cat", 3)
cat.get_name()
cat.add_age()
Animal.add_number()


# # 演習問題6

# In[35]:


class Animal:
    number = 0
    
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if type(new_age) == int:
            if 0 <= new_age:
                self._age = new_age
                return
        raise ValueError("int型で０以上の値を入れてください")
    
    def write(self):
        print("これは親クラスです")
        
cat = Animal("Kitty", "cat", 3) # 変数catに新しいオブジェクトを作って代入すると前のオブジェクトが削除されるため、最初にdelが実行されます
print(cat.age)
cat.age = 3


# # 演習問題7

# In[38]:


class Cat(Animal):
    def __init__(self, name, species, age, beard):
        super().__init__(name, species, age)
        self.beard = beard
        
    def write(self):
        print("これは子クラスです")

meary = Cat("Meary","cat", 3, "True")
meary.write()


# # 演習問題8

# In[39]:


class Cat(Animal):
    def __init__(self, name, species, age, beard):
        super().__init__(name, species, age)
        self.beard = beard
        
    def __call__(self):
        print("にゃー")
        
    def write(self):
        print("これは子クラスです")

meary = Cat("Meary","cat", 3, "True")
meary()

