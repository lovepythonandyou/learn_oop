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


class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.rating
        elif isinstance(other, ChessPlayer):
            return other.rating == self.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, int):
            return other < self.rating
        elif isinstance(other, ChessPlayer):
            return other.rating < self.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, int):
            return other > self.rating
        elif isinstance(other, ChessPlayer):
            return other.rating > self.rating
        else:
            return 'Невозможно выполнить сравнение'


magnus = ChessPlayer('Carlson', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000)
print(ian == 2789)
print(ian == magnus)
print(magnus > ian)
print(magnus < ian)
print(magnus < [1, 2])


class City:

    def __init__(self, name_city):
        name_city_low = name_city.lower()
        self.name = name_city_low.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return not self.name[-1] in ['a', 'e', 'i', 'o', 'u']


p1 = City('new york')
print(p1)
print(bool(p1))
p2 = City('SaN frANCISco')
print(p2)
print(p2 == True)


class Quadrilaterial:

    def __init__(self, width, heigth=0):
        self.width = width
        if heigth == 0:
            self.heigth = width
        else:
            self.heigth = heigth

    def __str__(self):
        if self.width == self.heigth:
            return f'Куб размером {self.width}x{self.heigth}'
        else:
            return f'Прямоугольник размером {self.width}x{self.heigth}'

    def __bool__(self):
        return isinstance(self, Quadrilaterial)


q1 = Quadrilaterial(10)
print(q1)
print(bool(q1))
q2 = Quadrilaterial(3, 5)
print(q2)
print(q2 == True)


class Addition:

    def __call__(self, *args, **kwargs):
        self.result = 0
        self.args = list(args)
        for i in range(len(self.args)):
            if isinstance(self.args[i], (int, float)):
                self.result += self.args[i]
        print(f'Сумма переданных значений = {self.result}')


add = Addition()

add(10, 20)
add(1, 2, 3.4)
add(1, 2, 'hello', [1, 2], 3)

import time


class Timer:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.func()
        finish_time = time.time()
        return f'Время работы программы {finish_time - start_time}'


@Timer
def calculate():
    for i in range(100000000):
        2 ** 100


print(calculate())


class UnitedKingdom:

    def capital(self):
        print('London is the capital of Great Britain.')

    def language(self):
        print('English is the primary language of Great Britain.')


class Spain:

    def capital(self):
        print('Madrid is the capital of spain.')

    def language(self):
        print('Spanish is the primary language of Spain')


class Building:

    def __init__(self, number_floors):
        self.number_floors = [None] * number_floors

    def __setitem__(self, key, value):
        if self.number_floors[key] == None:
            self.number_floors[key] = value

    def __getitem__(self, item):
        return self.number_floors[item]

    def __delitem__(self, key):
        del self.number_floors[key]


house1 = Building(22)
house1[0] = 'Reception'
house1[1] = 'Cinema'
house1[2] = 'SPA'
print(house1[2])
del house1[2]
print(house1[2])


class PowerTwo:

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index <= self.number:
            result = 2 ** self.index
            self.index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        result = self.count + 10
        self.count += 10
        return result


numbers = PowerTwo(2)
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


class InfinityIterator:

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        result = self.count
        self.count += 10
        return result


class Vechicle:
    pass


class Car(Vechicle):
    pass


class Plane(Vechicle):
    pass


class Boat(Vechicle):
    pass


class RaceCar(Car):
    pass


class NewInt(int):

    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(bin(self)[2:])


a = NewInt(9)
print(a.repeat())
d = NewInt(a + 5)
print(d.repeat(3))
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin())


class Transport:

    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/час'


class Car(Transport):

    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f'Осталось бензина на {self.__gasoline_residue} км'

    @gasoline.setter
    def gasoline(self, value):
        if not isinstance(value, int):
            print('Ошибка заправки автомобиля')
        else:
            self.__gasoline_residue += value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')


class Boat(Transport):

    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


class Plane(Transport):

    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'


transport = Transport('Telega', 10)
print(transport)
bike = Transport('shkolnik', 20, 'bike')
print(bike)

first_plane = Plane('Virgin Athlantic', 700, 450)
print(first_plane)
first_car = Car('BMW', 230, 75000, 300)
print(first_car)
print(first_car.gasoline)
first_car.gasoline = 20
print(first_car.gasoline)
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)


class Initialization:

    def __init__(self, capacity, food):
        if not isinstance(capacity, int):
            print('Количество людей должно быть целым числом')
        else:
            self.capacity = capacity
            self.food = food


class Vegetarian(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


class SweetTooth(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}! Их самая любимая еда {self.food}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.capacity == other
        elif isinstance(other, (Vegetarian, MeatEater)):
            return self.capacity == other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {self.capacity}'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        elif isinstance(other, (Vegetarian, MeatEater)):
            return self.capacity < other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {self.capacity}'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.capacity > other
        elif isinstance(other, (Vegetarian, MeatEater)):
            return self.capacity > other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {self.capacity}'


v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)
v_second = Vegetarian([23], ['nothing'])
m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)
s_first = SweetTooth(30000, ['Мороженное', 'Чипсы', 'ШОКОЛАД'])
print(s_first)
print(s_first > v_first)
print(30000 == s_first)
print(s_first == 25000)
print(100000 < s_first)
print(100 < s_first)


class A: pass


class B(A): pass


class C: pass


class D(C): pass


class E(B, D): pass


def get_mro(cls):
    print(*[c.__name__ for c in cls.mro()], sep=' -> ')


print(E.mro())
