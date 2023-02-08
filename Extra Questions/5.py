""" Dictionary comprehension """
def doller_to_rupee():
    # create a new dictionary
    price = {'Laptop': 10, 'Mobile': 5, 'Watch': 3, 'Keyboard': 1}
    # multiply the price and convert to rupee
    # convert_to_rupee = one doller convert to indian rupee
    convert_to_rupee = 81.38
    n_price = {i: j*convert_to_rupee for (i, j) in price.items()}
    return n_price
rc = doller_to_rupee()
print(rc)
