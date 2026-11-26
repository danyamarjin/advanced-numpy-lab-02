import numpy as np
from scipy import sparse
from timeit import repeat

rng = np.random.default_rng(42)
# 4.1. CSR с пятью ненулевыми элементами
A = sparse.random(5, 5, density=0.2, format='csr', random_state=rng)
print('CSR:\n', A.toarray(), '\nПлотность:', A.nnz/25)
# 4.2. COO и CSC
print('COO:', A.tocoo())
print('CSC:', A.tocsc())
# 4.3. Умножение на вектор
v = np.arange(1, 6)
print('Вектор:', v, '\nРезультат:', A @ v)
# 4.4. Сравнение производительности
S = sparse.random(1000, 1000, density=0.01, format='csr', random_state=rng)
D = S.toarray()
x = rng.random(1000)
assert np.allclose(S @ x, D @ x)
for name, matrix in [('CSR', S), ('Dense', D)]:
    t = min(repeat(lambda: matrix @ x, number=100, repeat=5))/100
    print(name, 'время:', t, 'с')
print('CSR, байт:', S.data.nbytes + S.indices.nbytes + S.indptr.nbytes)
print('Dense, байт:', D.nbytes)
