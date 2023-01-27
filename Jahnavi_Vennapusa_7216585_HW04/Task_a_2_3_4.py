'''
Create a 5x5 array with random values.
and find the minimum and maximum
values
'''
import numpy as np
import matplotlib.pyplot as plt
arr = np.random.random((5,5)) #generating random values
print("Array with random values :")
print(arr)

arrmin, arrmax = arr.min(), arr.max()
print("Minimum value:")
print(arrmin)
print("Maximum value:")
print(arrmax)

#creating a bar chart
plt.bar(np.arange(25), arr.flatten())
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()

#creating a pie chart

plt.pie(arr.flatten())
plt.title('Pie Chart')
plt.show()



# Normalize a 5x5 random matrix


original_matrix= np.random.random((5,5))
print("Original Matrix values:",original_matrix)

max, min = original_matrix.max(), original_matrix.min()
normalise_matrix = (original_matrix - min)/(max - min)
print("Normalised Matrix")
print(normalise_matrix)




# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)

arr1 = np.random.random((5,3)) #Generating a random 5x3
print("First matrix is:")
print(arr1)

arr2 = np.random.random((3,2)) #Generating a random 3x2
print("Second Matrix is:")
print(arr2)

matrixproduct = np.dot(arr1,arr2)
print("Product of the matrix is:")
print(matrixproduct)



