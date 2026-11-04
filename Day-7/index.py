# DDOF = 1 , Sample
# DDOF = 0 , population


# DDOF = 1
# import numpy as np

# marks = np.array([1,50,100])

# print(np.mean(marks))
# print(np.var(marks,ddof=1))
# print(np.std(marks,ddof=1))

# DDOF = 0

# import numpy as np

# marks = np.array([
#   42, 7, 85, 16, 93, 28, 54, 61, 3, 77,
#   19, 100, 35, 68, 12, 49, 81, 24, 56, 90,
#   5, 73, 31, 64, 18, 97, 40, 22, 59, 8,
#   86, 14, 52, 70, 33, 95, 1, 47, 63, 26,
#   79, 11, 58, 37, 92, 4, 66, 21, 84, 45,
#   10, 75, 30, 99, 53, 17, 69, 38, 88, 2,
#   57, 25, 72, 43, 96, 13, 60, 34, 80, 6,
#   51, 23, 89, 41, 15, 67, 29, 94, 55, 9,
#   76, 32, 62, 20, 87, 46, 0, 71, 36, 98,
#   50, 27, 83, 44, 74,  54, 65, 39, 91, 48
# ])

# print(np.mean(marks))
# print(np.var(marks,ddof=1))
# print(np.std(marks,ddof=1))


# import numpy as np

# marks = np.array([49,50,51])

# print(np.mean(marks))
# print(np.var(marks,ddof=0))
# print(np.std(marks,ddof=0))

# Reshape & Flatten

# import numpy as np

# numbers = np.array([10,20,30,40,50,60])
# table = numbers.reshape(2,3)

# print(table)
# print(numbers.shape)

import numpy as np

# table = np.array([10,20,30,40,50,60])

# print(table.reshape(2,-1))
# print(table.reshape(3,-1))
# table = np.array([[10,20,30],[40,50,60]])

# a = table.reshape(-1)
# b = table.ravel()
# c = table.flatten()

# a[0] = 99

# print(a)
# print(b)
# print(c)

# Transponse


# data = np.array([[1,2,3],
#                  [4,5,6]])

# print(data.T)
# print(data.T.shape)

# Broadcasting

# marks = np.array([[60,70,80],
#                   [75,85,95]])

# bonus = np.array([5,10,2])

# print(marks.shape)
# print(bonus.shape)

# print(marks + bonus)

# a = np.array([[1,2,3],[4,5,6]])

# b = np.array([10,20])

# print(a + b)
# print(a.shape)
# print(b.shape)

# Scalar
# a = np.array([1,2,3])

# print(a + 10)

# Joining & Splitting

# a = np.array([[1,2],
#              [3,4],
#           ])

# b = np.array([[5,6]])


# print(np.concatenate((a,b),axis=0))
# print(a.shape)
# print(b.shape)

# left = np.array([[1,2],[3,4]])

# right = np.array([[5],[6]])

# print(np.concatenate((left,right),axis=1))

# stack
# a = np.array([10,29])
# b = np.array([30,40])

# print(np.stack((a,b),axis=0))
# print(np.stack((a,b),axis=1))