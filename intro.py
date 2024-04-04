#list examples:
list1 = [1,2,3,4,5]
print(list1)
print(list1[0])

list2 = ["John Elder", 41, list1, True] #List can contain elements of different types but is computationaly not effective
print(list2) 

import numpy as np
#Numeric python
#ndarray = n-dimensional array

np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1) #[0 1 2 3 4 5 6 7 8 9]
print(np1.shape) #(10,)

#Range
np2 = np.arange(10)
print(np2) #[0 1 2 3 4 5 6 7 8 9]

#Step
np3 = np.arange(0,10,2)
print(np3) #[ 0  2  4  6  8]

#Zeros
np4 = np.zeros(10)
print(np4) #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] #float iis returned

#Mutidimensional zeros
np5 = np.zeros((2,10)) #here 2 signifies the rows and 10 the columns
print(np5)
#[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] 
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

#Full
np6 = np.full((2,5),6) #2 rows, 5 columns, 6 is the content of the 2D array
print(np6) 
#[[6 6 6 6 6]
# [6 6 6 6 6]]

#Convert Python lists to np
my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8) #[1 2 3 4 5]
print(np8[0]) #1
