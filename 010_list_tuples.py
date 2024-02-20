# index starts with 0, so first item in list is the 0th item
# items do not have to match in data type

# list defined
x = [4, True, 'Hi!'] # list is ordered and order matters
y = 'Hello!'
# can use functions on lists
print('original length:', len(x))
print(len(x))
# can use methods on lists

# append - adds an item to list
x.append(y)
print('After append: ')
print(x)
print('length:', len(x))

# extend - adds another list
x.extend([1,2,3,4, "What's up dawg?"])
print('After extend: ')
print(x)
print('length:', len(x))

# pop - gets value from list and removes it
x.pop()
print(x)

# index
x[0] = "Salut!" # lists are mutable so can be changed
print(x)
print(x[1])

# copying list
y = x[:] # creates a unique copied instance, y can be modified and x won't be affected

# tuples work same way as lists but immutable, can not be changed once defined.
z = (0,0,2,2)


# lists can contain tuples or lists within lists!