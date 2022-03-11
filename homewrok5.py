import numpy as np

A=np.array([[2,3,4],
            [4,8,2],
            [1,2,1]])

B = A.T

C = np.array_equal(A,B)

if C == True:
    print("대칭행렬입니다.")
else:
    print("대칭행렬이아닙니다.")
