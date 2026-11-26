import numpy as np
from decimal import Decimal

# 1.1. Сумма и ошибка округления
for dtype in (np.float32, np.float64):
    a = np.array([0.1, 0.2, 0.3], dtype=dtype)
    s = a.sum()
    print(dtype.__name__, 'сумма:', format(float(s), '.17g'))
    print('Ошибка:', Decimal.from_float(float(s)) - Decimal('0.6'))
    # 1.2. Машинное эпсилон
    print('Эпсилон:', np.finfo(dtype).eps)
    # 1.3. Вычитание близких чисел
    x, y = dtype(1.00000001), dtype(1.0)
    print('Разность:', x-y, '; точное значение: 1e-8')
