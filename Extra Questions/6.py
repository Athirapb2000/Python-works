""" List Comprehension"""
"""
Find all the words in a string that are less than 4 letters
"""
sentence = input('Enter a sentence : ')
words = sentence.split()
print(words)
result = [x for x in words if len(x) < 4]
print(result)
