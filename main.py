#money为余额
money = int(input('输入一个数字'))
print(money)

#s为取款金额
s = 100
if money >= s:
    money -= s
    print('余额为',money)


num=int(input('请输入一个整数'))
if num%2 == 0:
    print('该数字为偶数')
else:
    print('该数字为奇数')

score = int(input('请输入你的成绩'))
if score >= 90 and score <= 100:
    print('A级')
elif score >= 80 and score < 90:
    print('B级')
elif score >= 70 and score <80:
    print('c级')
elif score >= 60 and score < 70:
    print('D级')
else:
    print('重开吧你')