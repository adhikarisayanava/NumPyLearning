import numpy as np

#Numpy Universal Function

np1 = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
print(np1)

#Square root of each element
print(np.sqrt(np1))
#[0.         1.         1.41421356 1.73205081 2.         2.23606798
# 2.44948974 2.64575131 2.82842712 3.        ]

#Absolute Value
print(np.absolute(np1)) #[3 2 1 0 1 2 3 4 5 6 7 8 9]

#Exponents
print(np.exp(np1))
#[4.97870684e-02 1.35335283e-01 3.67879441e-01 1.00000000e+00
# 2.71828183e+00 7.38905610e+00 2.00855369e+01 5.45981500e+01
# 1.48413159e+02 4.03428793e+02 1.09663316e+03 2.98095799e+03
# 8.10308393e+03]

#Min/Max
print(np.min(np1)) #-3
print(np.max(np1)) #9

#Sign positive(1) or negative(-1)
print(np1)          #[-3 -2 -1  0  1  2  3  4  5  6  7  8  9]
print(np.sign(np1)) #[-1 -1 -1  0  1  1  1  1  1  1  1  1  1]