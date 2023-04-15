import numpy as np

c = [(1, 1, 1, 1), (2, 1, 1, 3), (1, 6, 1, 6)]
c_a = np.array(c)

zwei = np.where(np.all(c_a == np.array((1, 6, 1, 6)), axis = 1))
for i in c_a:
    print(tuple(i))
f = c_a[2]
b = c_a.tolist()
print(c_a)
print(b)
print(zwei[0][0])
print(f)



