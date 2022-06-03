def product(x, y):
  if y == 0:
    return 0
  
  else:
    return x + product (x, y - 1)

print (product (20, 21))
