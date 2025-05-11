import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 3], [3, 4]])
shape = a.shape
dtype = a.dtype
data = a.data

print(shape)
print("data--", data)
print("dtype --", dtype)
print(a.flatten())
print(a.flatten('F'))
print(a.flatten('C'))
print(a.flatten('A'))
print(a.flatten('K'))
print(a.copy())
print(np.copyto(a, b))

print("b---", b)
ones = np.ones((2, 4))
print("ones--", ones)
# np.append(b)

transpose = np.transpose(a)
trace = np.trace(a)
inv = np.invert(a)

print("transpose", transpose)
print("trace--", trace)
print("inv---", inv)

print("base", a.base)
print("list", a.tolist())
