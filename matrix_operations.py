import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Addition
print("\nMatrix Addition:")
print(A + B)

# Subtraction
print("\nMatrix Subtraction:")
print(A - B)

# Multiplication
print("\nMatrix Multiplication:")
print(np.dot(A, B))

# Transpose
print("\nTranspose of A:")
print(A.T)

# Inverse
try:
    A_inv = np.linalg.inv(A)
    print("\nInverse of A:")
    print(A_inv)
except np.linalg.LinAlgError:
    print("Matrix A is not invertible.")
