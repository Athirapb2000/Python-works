import json
# print(dir(json))

# x = {'name': 'Athira', 'age': 22, 'course': 'Python'}
# print(type(x))

# json
x = '{"name": "Athira", "age": 22, "course": "Python"}'
print(type(x))

# json to python(parsing)
y = json.loads(x)
print(type(y))

# python to json
z = json.dumps(x)
print(type(x))
