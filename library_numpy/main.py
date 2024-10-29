import numpy as np

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ,19, 20]
lst3 = [[1, 2],[3, 4]]

print('array', np.array(lst))
print('array*', np.array(lst) * 10)

print('arange', np.arange(10, 20))

print('linspace', np.linspace(0, 30, 11))

print('ones', np.ones(10))

print('zeros', np.zeros((2, 5, 3)))

lst = np.array(lst)
lst.shape = (5, 4)
print('shape', lst)

print('row/column', lst[2,1])

lst2 = 0 == (lst % 2)
print('', lst2)

left = np.arange(10).reshape(2, 5)
right = np.arange(15).reshape(5, 3)
print('left', left)
print('right', right)
print('dot', np.dot(left, right))

rnd_lst = np.random.random((7, 5)) #Рандомная матрица
print('random', rnd_lst)

np.set_printoptions(4) #Установка знаков после запятой с округлением до целого (В большую и в меньшую)
print('random', rnd_lst)

print(lst[0,:])

a = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

print(0 in a)