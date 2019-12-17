import sys
list1 = [1, 2, 3, 4, 5]
print(list1)
list1.append(6)
print(list1)
list1.extend([7])
print(list1)
list1 += [8]
print(list1)
if 1 in list1:
    list1.remove(1)
    print(list1)
list1.insert(0, 1)
print(list1)
list1.pop(0)
print(list1)
# list1.clear()
# print(list1)
print(sorted(list1, reverse=True))
g = [x for x in range(10)]
print(sys.getsizeof(g))
f = (x for x in range(10))
print(sys.getsizeof(f))
for var in f:
    print(var)
t = (1, True)
t[0] = 2
print(t)
