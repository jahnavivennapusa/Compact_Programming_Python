###Count number of vowels (a,o,u,e,i) in the string s
##Intput: s – string
##Output: Number of vowels = XX

vowels=['a','e','i','o','u','A','E','I','O','U']
s=input("Enter the word to search for vowels: ")
vowelFound=[]
for letter in s:
    if letter in vowels:
        #if letter not in vowelFound: #To eliminate redundant vowels
            vowelFound.append(letter)
print(vowelFound)
print("Number of vowels = ",len(vowelFound))