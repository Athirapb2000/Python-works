"""
Creating a dictionary from two, unlike lists
"""

def dict1(keys, values):
    return{keys[i]: values[i] for i in range(len(keys))}
movie = ['RDB', 'Wanted', 'DDLG', 'Sholay', 'War']
actor = ['Aamir', 'Salman', 'SRK', 'Amitabh', 'Hritik']
print('dictionary :', str(dict1(movie, actor)))
