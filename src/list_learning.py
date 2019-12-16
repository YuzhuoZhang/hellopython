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
list1.clear()
print(list1)
