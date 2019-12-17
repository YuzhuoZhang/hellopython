dict1 = dict(apple='true', feiowfj=2, ekfjwo=3)
print(dict1)
dict1 = dict(zip(['a', 'b', 'c', 'd'], '123'))
print(dict1)
dict1 = dict(zip(['a', 'b', 'c'], '1234'))
print(dict1)
# 字典的生成式语法
dict2 = {num: num ** 2 for num in range(1, 10)}
print(dict2)

