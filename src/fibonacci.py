a = b = 1
for x in range(1, 21):
    if x <= 2:
        print('第%d行:1' % x)
    else:
        c = a + b
        a = b
        b = c
        print('第%d行:%d' % (x, c))
