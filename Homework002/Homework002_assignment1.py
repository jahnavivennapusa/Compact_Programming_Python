'''
Write a function which will return how many times a word (symbols separated with space, coma and dot) meet in the string
Input: s – string
Output: word1 = number, word2 = number
Input: s= “Tom eats and eats”
Output: Tom = 1, eats = 2, and = 1
'''

# break the string into list of words

s = input("Enter the string in which you want to count the words")
s = s.split()
s2 = []

# loop till the string values is present in the list
for i in s:

    # checking if duplicate elements are present
    if i not in s2:
    # insert the values in s2
            s2.append(i)

for i in range(0, len(s2)):
    # count the frequency of each word in new list
    print('Frequency of', s2[i], 'is :', s.count(s2[i]))

