"""
Set Items are unchangeable but we can remove or add items from/to a set
"""

st1 = {"True", " ", 0, False, 1, True}
st2 = {"Apple", "Mango", "Banana"}
st1.add("Hello")
st1.update("Hello")
st1.remove(0)
print(st1)

# Removing set Items
st1 = {True, 0, "Hello", "Sabzi", "Mandi"}
print(st1.pop())
st1.clear()
print(st1)
del st1
del st2

# Joining Sets
st1 = {"Hello"}
st2 = {"Adnan"}
st1.union(st2)
print(st2)
print(st1)

# I(ntersection Update)
del st1
del st2
st1 = {"Adnan", "Ansari"}
st2 = {"Arish", "Ansari"}
print(st1.intersection(st2))
print(st1)

# symmetric difference
