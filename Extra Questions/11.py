"""
dictionary comprehension : changing from kilogram to pounds
"""
old_weights = {
    'book': 0.5,
    'milk': 2.0,
    'tv': 7.0
}
new_weights = {key: value*2.2 for (key, value) in old_weights.items()}
print(new_weights)