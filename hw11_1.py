"""
HW 11_1
Разработайте программное обеспечение для ведения журнала событий.
Вам необходим класс, который будет представлять строки журнала
и включать в себя информацию об авторе и времени создания каждой записи.

Создайте класс MyStr, который наследуется от встроенного класса str.
Этот класс будет представлять строки с информацией о событиях.

Класс MyStr должен иметь следующие атрибуты:

value (str): Строковое значение с описанием события.
author (str): Имя автора, создавшего запись.
time (float): Время создания записи в формате '%Y-%m-%d %H:%M'.

Реализуйте метод __new__(cls, value, author), который создает новый объект класса MyStr с заданным value и author.
Метод также автоматически фиксирует время создания записи.

Реализуйте метод __str__(self), который возвращает строковое представление
объекта класса MyStr с информацией о событии, авторе и времени создания.

Реализуйте метод __repr__(self), который возвращает строковое представление
объекта класса MyStr для отладки.
"""
import datetime


class MyStr(str):
    """Класс будет представлять строки с информацией о событиях"""
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.value = value
        instance.author = author
        return instance

    def __init__(self, value, author):
        self.value = value
        self.author = author
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"


event = MyStr("Завершилось тестирование", "John")
print(event)
print(event.__repr__())