## MUTABLE
# list, set, dict

## IMMUTABLE
# int, str, float, tuple

# mutable
y = [1,2]
print(y)

y.append(3)
print(y)

y[1] = 7
print(y)

# immutable
x = 'string'
print(x)

print(x + 's')
print(x)

# clone mutable
lst = y # we created an alias so any change on one shall reflect on other

lst.append(4)
print(y)

# immutable
z = x

z = z + 's'
print(x)
print(z)

# mutable and immutable
def changeList(li):
    li.append(100)

def copyList(li):
    newLst = li[:] # copy of li
    newLst.append(100)
    return newLst

x = [1,2,3]
changeList(x) # mutable
print(x) # change

copyList(x)
print(x) # no change

y = copyList(x)
print(x) # no change
print(y) # change

# is operator
lst = x
print(lst is x) # True

lst = x[:]
print(lst is x) # False