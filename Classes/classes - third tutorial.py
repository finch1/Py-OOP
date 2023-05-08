## Collections - allows different kinds of data types, sort info, iterate info
from cgi import print_form
from collections import Counter, namedtuple, deque

# Containers
# List
# Set
# Dict
# Tuple - immutable

# Types
# counter
# deque
# namedTuple()
# orderedDict
# defaultdict

c = Counter() # class accepts any data type or container. 

c = Counter('gallad')
print(c)
print(c.most_common(1))# find number of most common elements
c = Counter(['a', 'b', 'c', 'a', 'b'])
print(c)

c = Counter({'a':1, 'b':2, 'a':2})
print(c)
print(list(c.elements())) # prints elements times their value

c = Counter(cats=4, dogs=7)
print(c)
print(list(c.elements()))
# can count items and not throw error if not exists
print(c['cats'])
print(c['pets'])

# add list to dict
c = Counter(a=4, b=9, c=7, d=0)
d = ['a','b','c']
c.update(d)
print(c)

d = Counter(d)
print(c+d) # anything equal to zero or below is removed
print(c-d)


# intersecting = inner join and count key occurances in d wrt c
print(c&d)

# union = max velue of each key
print(c|d)

# Namedtuple
Point = namedtuple('Point', {'x':5, 'y':6, 'z':7})
newP = Point(1,1,1) # replace values
print(newP)

# Deque - faster for appending in the beginning and end, a mizture of types
d = deque('hello')
d.append('4')
d.append(5)

print(d)
d.pop() # removes the last element
print(d)

d.popleft() # removes the first element
print(d)

d.clear()
print(d)

# takes iteratable argument like string or list or... to list
d.extend('467')
d.extend('hello') # avoids adding to list with forloop
d.extendleft(['hello','9',10]) # appends in reverse order
print(d)

d.rotate(-3)
print(d)

# max len deletes from the begining and appends at the end
d = deque('hello', maxlen=5)
d.extend('498')

print(d)