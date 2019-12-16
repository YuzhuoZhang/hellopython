user = input('请输入用户名: ')
if user == 'zyz':
    print('hello, %s' % user)
elif user == 'zzz':
    print('hi, %s' % user)
else:
    print('您不在我们的系统中，请先注册!同意扣1，不同意扣2')
    if int(input())==1:
        print('注册连接为:xxxx.xx')
    else:
        print("一边玩去")
