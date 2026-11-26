import numpy as np
from timeit import repeat
from sum_squares import sum_squares_cython

# 5.1. Обычный Python

def sum_squares_python(values):
    total = 0.0
    for x in values:
        total += x*x
    return total

# 5.2–5.3. Один набор значений для обеих функций
values = np.arange(10**7, dtype=np.float64) % 100 / 100
values_list = values.tolist()
expected = sum_squares_python(values_list)
actual = sum_squares_cython(values)
assert np.isclose(expected, actual)
print('Python:', expected, '\nCython:', actual)
p = min(repeat(lambda: sum_squares_python(values_list), number=1, repeat=3))
c = min(repeat(lambda: sum_squares_cython(values), number=1, repeat=3))
print('Python:', p, 'с; Cython:', c, 'с; ускорение:', p/c)
