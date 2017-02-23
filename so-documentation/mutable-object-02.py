x = y = [7, 8, 9]   # x and y refer to the same list i.e. refer to same memory location
x[0] = 13           # now we are replacing first element of x with 13 (memory location for x unchanged)
print(x)
print(y)            # this time y changed!
# Out: [13, 8, 9]