# import cv2, keras, skimage as ski
import sys

arrA = [1,2,3,4,5]
arrB = ["a", 24, 3.14, 1]
tam = sys.getsizeof(arrA)
print(tam)
tam += sum (sys.getsizeof(x) for x in arrB)
print(tam)

# Cool python things
A = [[0]*3]*3
print(A)
A[1][1] = 1
print(A)

# Operador de rebanada genera una copia
arr = [[1,2,3],[4,5,6],[7,8,9]]
# result1 = arr[1:, 1:]
# print(result1)

arr = [1,2,3,4,5,6]
changed = arr[2:]
changed[0] = -1

print(arr)
print(changed)
