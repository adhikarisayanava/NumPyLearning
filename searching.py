import numpy as np

#Search
np1 =  np.array([1,2,3,4,6,7,8,9,10,9])

x = np.where(np1 == 9)
print(x[0]) #[7 9]

print(np1[x[0]]) #[9 9]

y = np.where(np1 % 2 == 0)
print(np1[y[0]]) #[ 2  4  6  8 10]