"""
HW 11-4
Реализуйте класс Matrix, представляющий матрицу и поддерживающий следующие операции:

Инициализация матрицы.
Конструктор класса должен принимать количество строк rows
и количество столбцов cols и создавать матрицу с нулевыми значениями.

Операция сложения матриц.
Реализуйте метод __add__, который позволяет складывать две матрицы одинаковых размеров.

Операция умножения матриц.
Реализуйте метод __mul__, который позволяет умножать две матрицы
с согласованными размерами (количество столбцов первой матрицы должно быть равно количеству строк второй матрицы).

Сравнение матриц на равенство.
Реализуйте метод __eq__, который позволяет сравнивать две матрицы на равенство.

Представление матрицы в виде строки.
Реализуйте метод __str__, который возвращает строковое представление матрицы,
где элементы строки разделены пробелами, а строки сами разделены символами новой строки.

Представление матрицы в виде строки для создания нового объекта.
Реализуйте метод __repr__, который возвращает строку, которую можно использовать
для создания нового объекта класса Matrix.
"""

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.data)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __add__(self, other):
        instance = Matrix(self.rows, self.cols)
        if self.rows == other.rows and self.cols == other.cols:
            for row in range(self.rows):
                for col in range(self.cols):
                    instance.data[row][col] = self.data[row][col] + other.data[row][col]
            return instance
        else:
            raise ValueError('This operation is impossible.')

    def __mul__(self, other):
        instance = Matrix(self.rows, other.cols)
        if self.cols == other.rows:
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        instance.data[i][j] += self.data[i][k] * other.data[k][j]
            return instance
        else:
            raise ValueError('This operation is impossible.')

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        else:
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.data[row][col] != other.data[row][col]:
                        return False
        return True


a = Matrix (2, 3)
a.data = [[1, 2, 3], [4, 5, 6]]
b = Matrix(2, 3)
b.data = [[1, 1, 1], [2, 2, 2]]
print(a)
print(b)
c = a + b
print(c)
d = Matrix(3, 2)
d.data = [[2, 3], [2, 2], [3, 3]]
print(d)
e = a * d
print(e)