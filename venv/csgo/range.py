'''r = range(10)
print(r)
print(list(r))

r = range(1,10)
print(r)
print(list(r))

r = range(1,10,2)
print(r)
print(list(r))

a = 1
sum = 0
while a <= 100:
    if a%2 == 0:
        sum += a
        a += 2
    else:
        a += 1
print(sum)'''
'''for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '528':
        print('密码正确')
        break
    else:
        print('哼哼')
else:
    print('你好久都没再来')

a = 0
while a<3:
    pwd = input('请输入密码：')
    if pwd == '528':
        print('密码正确')
        break
    else:
        print('哼哼')
    a +=1
 '''

import math
a = math.acos(0.5)
print(a)
