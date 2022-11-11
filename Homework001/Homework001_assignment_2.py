##### Write a Python program which accepts the user's
## first and last name and print them in reverse order with a space between them.


FirstName = input("Enter Your First Name : ")

LastName = input("Enter Your Last Name :")

print("Printing the name in reverse order :",LastName[-1::-1],FirstName[-1::-1])