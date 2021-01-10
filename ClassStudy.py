class User:
    active_users = 0

    @classmethod
    def display_active_user(cls):
        return f'There are currently{cls.active_users} active users'

    @classmethod
    def from_string(cls,data_str):
        first,last,age = data_str.split(",")
        return cls(first,last,int(age))

    def __repr__(self):
        return f"{self.first} is my name"


    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self._age = age
        self.__name = "i'm visible"
        User.active_users += 1

    @property #此方法不用（）拿age
    def age(self):
        return self._age

    @property
    def full_name(self):
        return f"{self.first}{self.last}"

    @age.setter
    def age(self,value):
        self._age = value

    @full_name.setter
    def full_name(self,value):
        self.first,self.last = value.split(" ")

   # def full_name(self):
     #   return f"{self.first}{self.last}"

    def likes(self,thing):
        return f"{self.first} likes {thing}"

#    def __str__(self):
#        return 'object override print'

    def __add__(self,other):
        if isinstance(other,User):
            return User(first = "Newborn", last= self.last,age = 0)
        return "You can't add that"

user1 = User("joe","Smith",68)
user2 = User("zh","Smith",44)
new_user = user1 +user2
print(new_user.last)
print(user1)
user1.age = 19
user1.full_name = "David Wang"
print(user1.first)


class Pet:
    allowed = ['cat','dog','fish','rat']

    def __init__(self,name,species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} not in pet")
        self.name = name
        self.species = species

    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f"you can't have a {species} pet")
        self.species = species

class Chicken:
    total_eggs = 0

    def __init__(self,name,species):
        self.name = name
        self.species = species
        self.egg = 0

    def Lay_eggs(self):
        self.eggs +=1
        Chicken.total_eggs +=1
        return self.eggs

class GrumpyDict(dict):
    def __repr__(self):
        return "NONE OF YOUR BUSINESS"

    def __missing__(self,key):
        print(f"you want {key}? well it ain't here!")

    def __setitem__(self,value,key):
        print("you wanna change the dictionary?")
        print("ok,fine")
        super().__setitem__(key,value)
a_dict = GrumpyDict({'one':1,'two':2,'three':3})
#print(a_dict["four"])
#a_dict['three'] = 'drei'

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

class Cat(Animal):
    def __init__(self,name,species,breed,toy):
        # Animal.__init__(self,name,species)
        super().__init__(name,species = "cat")
        self.breed = breed
        self.toy = toy

a_cat = Cat("apple","male",'haha','fish')
#print(a_cat.name)


class Aquatic:
    def __init__(self,name):
        self.name = name
    def swim(self):
        return f"{self.name} is swimming"
    def greet(self):
        return f"I am {self.name} of the sea"

class Ambulatory:
    def __init__(self,name):
        self.name = name
    def walk(self):
        return f"{self.name} is walking"
    def greet(self):
        return f"I am {self.name} of the land!"

class Penguin(Ambulatory,Aquatic):
    def __init__(self,name):
        super().__init__(name = name)

Penguin('hello')
