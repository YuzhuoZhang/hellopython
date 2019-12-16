# import turtle
#
# turtle.pensize(1)
# # turtle.pencolor('blue')
# turtle.pencolor('purple')
#
# turtle.forward(100)
# '''
# right是顺时针 left是逆时针
# forword是长度
# '''
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(45)
# turtle.forward(70.7)
# '''turtle.left(90)'''
# turtle.right(90)
# turtle.forward(70.7)
#
# turtle.mainloop()
import sys

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
