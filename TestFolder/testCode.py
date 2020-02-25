import numpy as np

A = np.array([[1, 2], [3, 4]])
AT = A.T
ATA = AT @ A
print("NIPPLS")
print(ATA)
