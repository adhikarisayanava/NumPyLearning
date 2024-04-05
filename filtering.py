import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9,10])

#x = [True, True, False, False, False, False, False, False, False, False]
#print(np1[x]) #[1 2]

'''
filtered = []
for things in np1:
    if things % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)

print(filtered) #[False, True, False, True, False, True, False, True, False, True]
print(np1[filtered])  #[ 2  4  6  8 10]
'''
#OR
filtered = np1 % 2 == 0
print(filtered)#[False, True, False, True, False, True, False, True, False, True]
print(np1[filtered])#[ 2  4  6  8 10]