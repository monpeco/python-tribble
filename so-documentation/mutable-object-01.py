x = y = [7, 8, 9]   # x and y refer to the same list; i.e., they refer to same memory location
print(y)
print(x)
x = [13, 8, 9]      # now we are assigning a brand new list to x (memory location for x changed!)
print(y)            # y is unchanged, so it's OK
print(x)
""" Out:
[7, 8, 9]
[7, 8, 9]
[7, 8, 9]
[13, 8, 9]
"""
