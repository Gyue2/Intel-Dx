x = input("x = ")
y = input("y = ")
z = input("z = ")

print("x = {}, y = {}".format(x, y))

t = x
x = y
y = t

print("x = {}, y = {}".format(x,y))

x, y, z = z, x, y

print("x = {}, y = {}, z = {}".format(x,y,z))

