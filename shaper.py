import numpy as np

#Create 1D array and get shape
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1) #[ 1  2  3  4  5  6  7  8  9 10 11 12]
print(np1.shape) #(12,)

#Create 2D array and get shape
np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(np2) #[[ 1  2  3  4  5  6] 
# [ 7  8  9 10 11 12]]
print(np2.shape) #(2, 6) #2 rows and 6 columns

#Reshape 1D to 2D array
np3 = np1.reshape(3,4) # 3 rows and 4 columns
print(np3)
#[[ 1  2  3  4]       
# [ 5  6  7  8]       
# [ 9 10 11 12]]
print(np3.shape) #(3, 4)

#Reshape 1D to 3D array
np4 = np1.reshape(2,3,2)
print(np4)
#[[[ 1  2]
#  [ 3  4]
#  [ 5  6]]

# [[ 7  8]
#  [ 9 10]
#  [11 12]]]
print(np4.shape) #(2, 3, 2)

#Flatten back to 1D
np5 = np4.reshape(-1)
print(np5) #[ 1  2  3  4  5  6  7  8  9 10 11 12]
print(np5.shape) #(12,)