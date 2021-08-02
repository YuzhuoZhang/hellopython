str1 = 'hello '
str2 = 'python'
str1 += str2
print(str1 * 3)
print('python' in str2)
print(len(str1))
print(str1[-1:-13:-2])
# num = int(input('input a number: '))
# str3 = str(num)
# str3 = str3[::-1]
# print(int(str3))
# 字符串长度
print(len(str2))
# 强行变成标题...
print('fjeowfja,jefwoiajeofji'.title())
print(str1.center(100, '-'))
print(str1.rjust(100, '-'))
# 判断字符串是否以数字组成
print(str1.isdigit())
# 判断字符串是否以字母组成
print('str'.isalpha())
a = 1
b = 2
print(f'{a} + {b} = {a + b}')
# 区分rfind和find的区别,rfind是找到最后一次出现的索引，find是第一次出现的索引
print(str1.find('o'))
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]][2]
print(array)
