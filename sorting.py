import numpy as np

#np.sort() 

#Numerical
np1 = np.array([7,6,4,8,2,1])
print(np1) #[7 6 4 8 2 1]
print(np.sort(np1)) #[1 2 4 6 7 8]
print(np1) #Original does not gets changed [7 6 4 8 2 1]

#Alphabetical
#for array
np2 = np.array(["John", "Tina", "Aaron", "Zed"])
print(np.sort(np2)) #['Aaron' 'John' 'Tina' 'Zed']
#for list
list1 = ["John", "Tina", "Aaron", "Zed"]
list1.sort()
print(list1)

#Boolean
np3 = np.array([True, False, False, True])
print(np.sort(np3))

#2D
np4 = np.array([[4,3,8,2],[7,9,1,5]])
print(np4)
#[[4 3 8 2]
# [7 9 1 5]]
print(np.sort(np4))
#[[2 3 4 8]
# [1 5 7 9]]

