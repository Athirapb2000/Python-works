d = [{'item': 'item1', 'amount': 400},
     {'item': 'item2', 'amount': 300},
     {'item': 'item1', 'amount': 750}]
lst = {}
for i in d:
    if i['item'] not in lst:
        lst[i['item']] = i['amount']
    else:
        lst[i['item']] += i['amount']
print(lst)
