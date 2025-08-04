import numpy as np
X=np.array([[1,2,3],[4,4,4],[7,8,9]])

U,S,VT=np.linalg.svd(X)
n_components=2

X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("original matrix:")
print(X)
print("\n reconstructed matrix(with  reduced dimensions):")
print(X_reconstructed)