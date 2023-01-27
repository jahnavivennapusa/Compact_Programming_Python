'''
Consider a generator function that
generates 10 integers and use it to build an
array
'''
print ("****************************************\n")
print("Solution of Task 1")
print ("****************************************\n")
import numpy as np
def generate_func():
   for n in range(15):
       yield n
nums = np.fromiter(generate_func(),dtype=int,count=-1)
print("Printing the values generated from Generator function:",nums)
'''
Consider two random array A and B, check 
if they are equal
'''
print ("****************************************\n")
print("Solution of Task 2")
print ("****************************************\n")
arrA = np.random.randint(0,2,6)
print("First array values are:",arrA)
arrB = np.random.randint(0,2,6)
print("Second array values are:",arrB)
print("Checking if the two arrays are equal or not:")
array_eq = np.allclose(arrA, arrB)
print("Two arrays are equal:")
print(array_eq)
'''
Consider a random vector with shape 
(100,2) representing coordinates, find 
point by point distances
'''
print ("****************************************\n")
print("Solution of Task 3")
print ("****************************************\n")
vector_values = np.random.random((10,2))
Point1,Point2 = np.atleast_2d(vector_values[:,0]), np.atleast_2d(vector_values[:,1])
distance = np.sqrt( (Point1-Point1.T)**2 + (Point2-Point2.T)**2)
print("Distance between the points:")
print(distance)
'''
Subtract the mean of each row of a matrix
'''
print ("****************************************\n")
print("Solution of Task 4")
print ("****************************************\n")
arr = np.random.rand(3, 4)
print("Matrix values are:",arr)
mean_val = arr - arr.mean(axis=1, keepdims=True)
print("Mean Value of the matrix is:",mean_val)

'''
 How to I sort an array by the nth column?
'''
print ("****************************************\n")
print("Solution of Task 5")
print ("****************************************\n")
arr = np.array([[9, 2, 3],[4, 5, 6],[7, 0, 5]])
print("Printing the array without sorting")
arr = arr[arr[:,1].argsort()] #sorting second column of array
print("printing the array after sorting array second column")
print(arr)

'''
Compute a matrix rank
'''
print ("****************************************\n")
print("Solution of Task 6")
print ("****************************************\n")
matrixA = np.array([[1, 2, 3, 23],
                       [4, 5, 6, 25],
                       [7, 8, 9, 28],
                       [10, 11, 12, 41]])
print("the matrix is:",matrixA)
print("The Rank of a Matrix: ", np.linalg.matrix_rank(matrixA)) #rank is calcualted using SVD

'''
Consider a 16x16 array, how to get the 
block-sum (block size is 4x4)
'''

print ("****************************************\n")
print("Solution of Task 7")
print ("****************************************\n")
arra1 = np.ones((16,16)) #generating an array of one's
block_size = 4
print("printing the original array values")
print(arra1)
result = np.add.reduceat(np.add.reduceat(arra1, np.arange(0, arra1.shape[0], block_size), axis=0),
                                      np.arange(0, arra1.shape[1], block_size), axis=1) #reducing the array by specifying slices
print("\nBlock-sum (4x4) of the array:")
print(result)
