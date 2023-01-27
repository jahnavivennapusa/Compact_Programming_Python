#Create vector with values ranging from 10 to 49
import numpy as np
import matplotlib.pyplot as plt
vectorvalues = np.arange(10,49) #Generating values within interval
print("Vector values from 10 to 49 are: ")
print(vectorvalues)

#Reversing a vector
reversevector= np.flipud(vectorvalues)

print("Vector values in reverse:")
print(reversevector)

# Creating a bar plot
plt.bar(np.arange(len(vectorvalues)), vectorvalues)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Bar Plot')
plt.show()

# Create a pie plot
plt.pie(vectorvalues)
plt.title('Pie Plot')
plt.show()
