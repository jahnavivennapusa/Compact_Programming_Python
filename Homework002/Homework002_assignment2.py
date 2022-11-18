'''
Write a Python function to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

tupList =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print("List of Tuple before sorting : " + str(tupList))
# sort list of typles in ascending order - bubble sort
listSize = len(tupList);
for i in range(0, listSize):
    for j in range(0, listSize - i - 1):
        if(tupList[j][-1] > tupList[j + 1][-1]):
            temp = tupList[j]
            tupList[j] = tupList[j + 1]
            tupList[j + 1] = temp

print("List of Tuple after sorting : " + str(tupList))