import numpy as np

#Copy vs View

#Create a view(change in one changes the other)
np1 = np.array([1,2,3,4,5,6])
np2 = np1.view()
print(f"Original np1 {np1}") #[1 2 3 4 5 6]
print(f"Original np2 {np2}") #[1 2 3 4 5 6]

np1[0] = 7
print(f"Changed np1 {np1}") #[7 2 3 4 5 6]
print(f"Changed np2 {np2}") #[7 2 3 4 5 6]


#Create a copy(change in one does not change the other)
np1 = np.array([1,2,3,4,5,6])
np2 = np1.copy()
print(f"Original np1 {np1}")#[1 2 3 4 5 6]
print(f"Original np2 {np2}")#[1 2 3 4 5 6]
np1[0] = 7
print(f"Changed np1 {np1}")#[7 2 3 4 5 6]
print(f"Changed np2 {np2}")#[1 2 3 4 5 6]
