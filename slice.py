import numpy as np

#Slicing NumPy arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])
print(np1[1:5]) #[2 3 4 5] #similar to list slice

#Return from something till end of array
print(np1[1:]) #[2 3 4 5 6 7 8 9]

#Negative slices
print(np1[-1]) #9
print(np1[::-1]) #[9 8 7 6 5 4 3 2 1]
print(np1[-3:-1]) #[7 8]

#Steps
print(np1[1:5:2]) #[2 4]

#Steps on entire array
print(np1[::2]) #[1 3 5 7 9]

#Slice 2D array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2[1][2]) #8
print(np2[1,2]) #8
print(np2[0:1,1:3]) #[[2 3]]

#Slice from both rows
print(np2[0:2,1:3]) 
#[[2 3]
# [7 8]]
 