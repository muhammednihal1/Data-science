import numpy as np;

A=np.array([[1, 2], [3, 4]])
B=np.array([[5, 6], [9, 8]])
print("Matrix Operations\n----------------")
print(f"\nMatrix A:\n{A}")
print(f"\nMatrix B:\n{B}")

print("\nMatrix addition :\n",A+B)
print("\nMatrix Substraction :\n",B-A)
print("\nMatrix Multiplication :\n",np.dot(A,B))
print("\nTranspose of matrix A :\n",A.T)
