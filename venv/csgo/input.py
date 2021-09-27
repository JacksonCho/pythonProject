#相当于先printf关键字，再scanf输入内容



'''a = int(input('先输入一个数字：'))
#a = int(a)
b = int(input('再输入一个数字：'))
#b = int(b)
print(a+b)'''

'''print(2**3)

a = 12
b = 16
c = 12
print(a < b)
print(a == b)
print(a is c)'''

'''answer = input('是会员吗')
money = int(input('请输入消费金额'))
if answer == 'vip':
    print('会员')
    if money >= 100:
        money = money * 0.9
        print(int(money))
    elif money >= 200:
        money = money * 0.8
        print(money)
else:
    print('你寄吧谁啊')
    if money >= 200:
        money *=  0.95
        print(money)
    else:
        print('回家吧')'''

'''#使用条件表达式进行比较
num1 = int(input('输入一个数'))
num2 = int(input('输入第二个数'))
print(str(num1)+'大于等于'+str(num2) if num1 >= num2 else str(num1)+'小于'+str(num2))'''

