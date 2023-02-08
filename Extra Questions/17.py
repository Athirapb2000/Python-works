"""
Write a python program to convert a dictionary of celsius temperatures into Fahrenheit.
"""
celsius = {'t1': 35, 't2': 36.5, 't3': 35.8, 't4': 37.5}
# get the corresponding 'fahrenheit' values and create the new dictionary
fahrenheit = {key: (value * 1.8) + 32 for (key, value) in celsius.items()}
print(fahrenheit)