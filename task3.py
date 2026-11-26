import numpy as np
from pathlib import Path
from tempfile import TemporaryDirectory
from IPython import get_ipython
from timeit import repeat

# 3.1. Заполнение файла порциями
with TemporaryDirectory() as directory:
    path = Path(directory) / 'matrix.dat'
    rng = np.random.default_rng(42)
    m = np.memmap(path, dtype='float64', mode='w+', shape=(1000, 1000))
    for i in range(1000):
        m[i] = rng.random(1000)
    m.flush()
    del m
    # 3.2. Чтение отдельных срезов
    m = np.memmap(path, dtype='float64', mode='r', shape=(1000, 1000))
    print('Размер файла:', path.stat().st_size, 'байт')
    print('Строка 0 (5 первых элементов):', m[0, :5])
    print('Столбец 0 (5 первых элементов):', m[:5, 0])
    # 3.3. Одинаковые операции при разном порядке доступа
    def rows():
        return sum(m[i, :].sum() for i in range(1000))
    def columns():
        return sum(m[:, j].sum() for j in range(1000))
    assert np.isclose(rows(), columns())
    shell = get_ipython()
    for name in ('rows', 'columns'):
        print(name)
        if shell is not None:
            shell.run_line_magic('timeit', '-n 10 -r 5 '+name+'()')
        else:
            print(min(repeat(globals()[name], number=10, repeat=5))/10, 'с')
    del m
