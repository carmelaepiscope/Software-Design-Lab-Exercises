def maxmin(data,a):
  if a == 1:
     return data[0], data[0]
  else:
    x, y= maxmin(data, a-1)
    return data[a - 1] if (data[a - 1] > x) else x, data[a - 1] if (data[a - 1] <y) else y

data=[1,2,3,4,5,6,7,8,9,10]
m, a=maxmin(data, 10)
print(m, a)