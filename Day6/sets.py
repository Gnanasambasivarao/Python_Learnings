# Set is special data type used to stode the heterogenious data and it is unorder collection of elements
# It does not allow duplicate

# a={2,3,4,5,6,5,13,54,35,5,1}
# b={55,75,8,5,6,46,26}

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
# Subset: check that b is the sub part of a set then it print true else false
print(a.issubset(b))
print(b.issubset(a))

# Superset: checks that b is the superset(parent) of the a set
print(a.issuperset(b))
print(b.issuperset(a))

# union:Used to combine both the sets into one
print(a.union(b))
# Intersection: USed to print all the common elements from both sets
print(a.intersection(b))

# Difference is used to return the uncommon elements from parent set not fron the child set
c={10,11,1,2,13,14,15,16}
d={3,4,5,6,7,8,9,1,2,13,15,16,14}
print(c.difference(d)) # here "c" is the parent set
print(d.difference(c)) # here "d" is the parent set

# symentricdifference: In this it return uncommon elements from both sets 
print(a.symmetric_difference(b))

# Update: It modifies and changes the original list
print(f"Before update {a}") 
a.update(b)
print(f"After update {a}")

# Interscetion_update: Returns the common elemets while updating the original set
e={1,2,3,4,5,6,4,5,6,7,6,8}
g={2,4,5,6,7,8,9,4,5,15,11,12}
e.intersection_update(g)
print(e) # {2,4,5,6,7,8}

# difference update
w={1,2,3,4,5,6,4,5,6,7}
w.difference_update(g)
print(w) #{1,3} are teh different one in w so it will be updated as return set

# symmetric_difference_update:
r={2,3,4,5,6,7,8,9}
t={5,6,7,8,9,10,11}
r.symmetric_difference_update(t)
print(r)

# Add, copy,clear,pop
r.add(12)
print(r)

t=r.copy()
print(t)

t.clear()
print(t)

print(r.pop())

r.remove(12)
print(r)
r.discard(11)
print(r)

# Disjoint: It return true when the both set donot contain any common value
set_a={1,2,3,4,5}
set_b={6,7,8,9,10}
print(set_a.isdisjoint(set_b))
set_c={2,11,12,13,14,15,16}
print(set_c.isdisjoint(set_a))

# Len()
print(len(set_a))
# In the set we donot have duplicates so count will not be used in sets
# In set the elements are unordered so in this it will not have any index method 