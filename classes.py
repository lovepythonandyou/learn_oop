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


class SoccerPlayer:
    goals = assists = number_goals = number_assists = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def score(self, number_goals=1):
        self.number_goals = number_goals
        return self.goals + number_goals

    def make_assict(self, number_assists=1):
        self.number_assists = number_assists
        return self.assists + number_assists

    def statistics(self):
        return f'Name: {self.name} Surname: {self.surname} - goals: {self.goals + self.number_goals}, assists: {self.assists + self.number_assists}'


leo = SoccerPlayer('Leo', 'Messi')
print(leo.score(700))
print(leo.make_assict(500))
print(leo.statistics())
kokorin = SoccerPlayer('Alexander', 'Kokorin')
print(kokorin.score())
print(kokorin.statistics())
chalov = SoccerPlayer('Fedor', 'Chalov')
print(chalov.statistics())


class Zebra:
    counter = 'Полоска белая'
    result = 0

    def which_stripe(self, counter='Полоска черная'):
        if self.result % 2 == 0:
            self.result += 1
            return self.counter
        else:
            self.result += 1
            return counter


z1 = Zebra()
print(z1.which_stripe())
print(z1.which_stripe())
print(z1.which_stripe())

z2 = Zebra()
print(z2.which_stripe())
print(z2.which_stripe())


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'<{self.first_name}> <{self.last_name}>'

    def is_adult(self):
        return self.age >= 18

person1 = Person('Ivan', 'Ivanov', 17)
person2 = Person('Eva', 'Ivanova', 20)
print(person1.full_name(), person1.is_adult())
print(person2.full_name(), person2.is_adult())

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old.'

    def speak(self, sound):
        self.sound = sound
        return f'{self.name} says {self.sound}'


jack = Dog('Jack', 4)
walt = Dog('Walt', 0.5)
print(jack.description(), jack.speak('GAAAAAAAAAAAAFF'))
print(jack.speak('GAV'))
print(walt.description(), jack.speak('GAFFFFFF'))

class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        # return f'Имя: {self.__name} Возраст: {self.__age} Направление: {self.__branch}'
        print(f'Имя: {self.__name} \nВозраст: {self.__age} \nНаправление: {self.__branch}')

    def access_private_method(self):
        self.__display_details()


obj = Student('Adam Smith', 25, 'IT')
# obj._Student__display_details()
obj.access_private_method()


class P:
    def __a(self):
        pass

    def _b(self):
        pass


a1 = P()
print(a1._b())
print(a1._P__a())


class UserMail:

    def __init__(self, login, email):
        self.login = login
        self._email = email

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        if not isinstance(new_email, str):
            print(f'ErrorMail: {new_email}')
        else:
            if new_email.count('@') == 1 and new_email.count('.') == 1:
                self._email = new_email
            else:
                print(f'ErrorMail: {new_email}')

    email = property(fget=get_email, fset=set_email)


k = UserMail('bb', 'prince@wait.you')
print(k.email)
k.email = [1, 2, 3]
k.email = 'p@rince@wait.you'
k.email = 'prince@still.wait'
print(k.email)


class Notebook:

    def __init__(self, some_list):
        self._notes = some_list

    def notes_list(self):
        for i, self._notes in enumerate(self._notes):
            print(f'{i + 1}. {self._notes}')


note = Notebook(['flesh', 'adrenalin', 'monster'])
note.notes_list()


class Money:

    def __init__(self, dlrs, cnts):
        self.total_cents = dlrs * 100 + cnts

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = value * 100 + self.cents
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 100 > value >= 0:
            self.total_cents = self.dollars * 100 + value
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'

Bill = Money(101, 99)
print(Bill)
print(Bill.dollars, Bill.cents)
print(Bill.total_cents)
Bill.dollars = 666
print(Bill)
Bill.cents = 12
print(Bill)


class Rectangle:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def area(self):
        return self.__a * self.__b


r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area)
print(r2.area)

class Date:

    def __init__(self, day, mouth, year):
        self.__day = day
        self.__mouth = mouth
        self.__year = year

    @property
    def date(self):
        return f'{self.__day:02}/{self.__mouth:02}/{self.__year:04}'

    @property
    def use_date(self):
        return f'{self.__mouth:02}-{self.__day:02}-{self.__year:04}'


d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 9)
print(d1.date)
print(d1.use_date)
print(d2.date)
print(d2.use_date)


class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print(f'Робот {self.name} создан')

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} разрушен')

    def say_hello(self):
        print(f'{self.name} приветствует тебя')

    @classmethod
    def how_many(cls):
        print(f'Нас осталось столько: {cls.population}')



r = Robot('terry')
r.say_hello()
Robot.how_many()
r.destroy()


class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = gender
        if self.gender != 'male' and self.gender != 'female':
            print('Пусть будет мальчиккккк!')
            self.gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.name} {self.surname}'
        else:
            return f'Гражданка {self.name} {self.surname}'


p1 = Person('Chuck', 'Norris')
print(p1)
p2 = Person('Mila', 'Kunis', 'female')
print(p2)
p3 = Person('Оби-Ван', 'Кеноби', True)
print(p3)


class Vector:

    def __init__(self, *args):
        a = []
        for i in args:
            if isinstance(args, int):
                a.append(i)
        self.values = sorted(a)

    def __str__(self):
        if self.values == []:
            return 'Пустой вектор'
        else:
            b = tuple(self.values)
            return f'Вектор {b}'

    def __add__(self, other):
        if isinstance(other, int):
            b = [number + other for number in self.values]
            return Vector(*b)
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                b = [sum(i) for i in zip(self.values, other.values)]
                # return [i + k for i in self.values for k in other.values]
                return Vector(*b)
            else:
                print('Сложение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            b = [number * other for number in self.values]
            return Vector(*b)
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                b = [i[0] * i[1] for i in zip(self.values, other.values)]
                return Vector(*b)
            else:
                print('Умножение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя умножать с {other}')


v1 = Vector(1, 2, 3)
print(v1)
v2 = Vector()
print(v2)
v3 = v1 + v2
print(v3)
v4 = v3 + 5
print(v4)
v5 = v1 * 2
print(v5)
print(v5 + 'hi')