import numpy as np

# 2.1. Индексация и срезы (индексы начинаются с нуля)
A = np.arange(-10, 10).reshape(4, 5)
print('A:\n', A)
print('Вторая строка:', A[1, :])
print('Столбец 3:', A[:, 3])
print('Строки 1–3, столбцы 2–4:\n', A[1:4, 2:5])
# 2.2. Все сочетания указанных строк и столбцов
print('Fancy-индексация:\n', A[np.ix_([0, 2, 3], [1, 4])])
# 2.3. Логическая индексация
A[A < 0] = 0
print('После замены:\n', A)
# 2.4. Broadcasting
B = np.arange(4).reshape(4, 1)
C = np.arange(5).reshape(1, 5)
print('B:\n', B, '\nC:\n', C, '\nB+C:\n', B+C)
