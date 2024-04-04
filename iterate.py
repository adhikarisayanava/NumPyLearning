import numpy as np
'''
#1D
np1 = np.array([1,2,3,4,5,6,7,8,9,10])
for i in np1:
    print(np1[i-1])
    #OR
    #print(i)

#2D
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np2: #iterate the 2 rows first
    print(i) 
    for j in i: #iterate within each row now to get each elements
        print(j)
'''
#3D
np3 = np.array([[[1,2,3],[4,5,6], [7,8,9],[10,11,12]]])
#print(np3)
'''
for x in np3:
    for y in x:
        for z in y:
            print(z)
'''
#OR better way use np.nditer(),can be used with any dimensional array
for x in np.nditer(np3):
    print(x)