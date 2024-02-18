x = 9
y = 2

result_add = (x + y)
result_sub = (x - y)
result_div = (x / y) # returns float, need to convert to int if required
result_mul = (x * y)
result_sqrd = (x ** y) # exponent, squared, to the power of
result_idiv = (x // y) # integer division, returns int not float
result_mod = (x % y) # modulus, returns remainder

print(str(x),"+",str(y), '=', result_add)
print(str(x),"-",str(y), '=', result_sub)
print(str(x),"/",str(y), '=', result_div)
print(str(x),"*",str(y), '=', result_mul)
print(str(x),"to the power of",str(y), '=', result_sqrd)
print(str(x),"//",str(y), '=', result_idiv)
print(str(x),"modulus",str(y), '=', result_mod)

# Order Of Operation
# B - Brackets
# I - Indices
# D - Division
# M - Multiplication
# A - Addition
# S - Subtraction