'''
Write a Python program to convert a given list of strings into list of lists using map function
'''

def converttolist(str):
    result = map(list, str)
    print(list(result))

phonecolours = ['Black', 'Gold', 'Blue']
converttolist(phonecolours)

