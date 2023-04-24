class Factory():
    pass


class Cat():
    name = 'Matroskin'
    color = 'black'


my_cat = Cat()


class Lion():
    def roar(self):
        return f'Rrrrrrrrrrrrrrrr!'


class Counter():
    value = 0

    def start_from(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def display(self):
        return f'Текущее значение счетчика = {self.value}'

    def reset(self):
        self.value = 0


class Pointer():
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance(self, example):
        if isinstance(example, Pointer):
            return ((example.x - self.x) ** 2 + (example.y - self.y) ** 2) ** 0.5
        else:
            return 'Передана не точка!'


class Laptop:

    def __init__(self, brand, model, price, laptop_name='<brand> <model>'):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'


laptop1 = Laptop('Acer', 'an515', 60000)
laptop2 = Laptop('HP', 'ah213', 55000)


# class SoccerPlayer:
#     goals = assists = number_goals = number_assists = 0
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def score(self, number_goals=1):
#         self.number_goals = number_goals
#         return self.goals + number_goals
#
#     def make_assict(self, number_assists=1):
#         self.number_assists = number_assists
#         return self.assists + number_assists
#
#     def statistics(self):
#         return f'Name: {self.name} Surname: {self.surname} - goals: {self.goals + self.number_goals}, assists: {self.assists + self.number_assists}'
#
#
# leo = SoccerPlayer('Leo', 'Messi')
# print(leo.score(700))
# print(leo.make_assict(500))
# print(leo.statistics())
# kokorin = SoccerPlayer('Alexander', 'Kokorin')
# print(kokorin.score())
# print(kokorin.statistics())
# chalov = SoccerPlayer('Fedor', 'Chalov')
# print(chalov.statistics())


# class Zebra:
#     counter = 'Полоска белая'
#     result = 0
#
#     def which_stripe(self, counter='Полоска черная'):
#         if self.result % 2 == 0:
#             self.result += 1
#             return self.counter
#         else:
#             self.result += 1
#             return counter
#
#
# z1 = Zebra()
# print(z1.which_stripe())
# print(z1.which_stripe())
# print(z1.which_stripe())
#
# z2 = Zebra()
# print(z2.which_stripe())
# print(z2.which_stripe())


# class Person:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def full_name(self):
#         return f'<{self.first_name}> <{self.last_name}>'
#
#     def is_adult(self):
#         return self.age >= 18
#
# person1 = Person('Ivan', 'Ivanov', 17)
# person2 = Person('Eva', 'Ivanova', 20)
# print(person1.full_name(), person1.is_adult())
# print(person2.full_name(), person2.is_adult())

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f'{self.name} is {self.age} years old.'
#
#     def speak(self, sound):
#         self.sound = sound
#         return f'{self.name} says {self.sound}'
#
#
# jack = Dog('Jack', 4)
# walt = Dog('Walt', 0.5)
# print(jack.description(), jack.speak('GAAAAAAAAAAAAFF'))
# print(jack.speak('GAV'))
# print(walt.description(), jack.speak('GAFFFFFF'))

# class Student:
#     def __init__(self, name, age, branch):
#         self.__name = name
#         self.__age = age
#         self.__branch = branch
#
#     def __display_details(self):
#         # return f'Имя: {self.__name} Возраст: {self.__age} Направление: {self.__branch}'
#         print(f'Имя: {self.__name} \nВозраст: {self.__age} \nНаправление: {self.__branch}')
#
#     def access_private_method(self):
#         self.__display_details()
#
#
# obj = Student('Adam Smith', 25, 'IT')
# # obj._Student__display_details()
# obj.access_private_method()


# class P:
#     def __a(self):
#         pass
#
#     def _b(self):
#         pass
#
#
# a1 = P()
# print(a1._b())
# print(a1._P__a())


