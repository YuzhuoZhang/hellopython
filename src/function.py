import src.hello


def param_order(a=1, b=2, c=3):
    print('a = %d  ' % a)
    print('b = %d  ' % b)
    print('c = %d  ' % c)


def function_a(num):
    return True if num == 1 else False


param_order(c=4, a=5, b=6)
param_order(7, 8)
print(function_a(2))
