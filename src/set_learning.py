set1 = {1, 1, 2, 3}
print(len(set1))
print(set1)
set1.add(4)
print(set1)
set1.update([5, 6])
print(set1)
# 使用discard和remove都可以删除set当中的元素，区别就是remove的元素在set当中没有的话会报错，而discard不会
set1.discard(6)
set2 = {4, 5, 6, 7, 8}
print(set1, set2)
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set1 ^ set2)
