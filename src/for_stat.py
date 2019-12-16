import random

sum = 0
for a in range(2, 11, 2):
    sum += a
print(sum)

# 三角形
height = int(input('三角形高度:'))
for x in range(height):
    for y in range(height + x):
        if y < (height - x - 1):
            print(' ', end='')
        elif y < (height + x):
            print('*', end='')
    print()
# for x in range(height):
#     for y in range(height - x - 1):
#         print(' ', end='')
#     for y in range(2 * x + 1):
#         print('*', end='')
#     print()

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入一个数字（1-100之间）：'))
    if number > answer:
        print('大了')
    elif number < answer:
        print('小了')
    else:
        print('bingo, 答案正确:%d' % answer)
        break
print('共猜了%d次' % counter)
