#
import random

print('-----------------------------------------------------------------')
print('|                                                                |')
print('|                    花有重开日 人无在少年                           |')
print('|                                                                |')
print('|                    欢迎来到 认识模拟重开器                         |')
print('|                                                                |')
print('|                                                                |')
print('|                                                                |')
print('-----------------------------------------------------------------')

# 设置初始初始属性
# 颜值 智力 家境 体质 总值不能超过 20 每一项取值 1 - 10

# 使用while 循环 使玩家输入错误的时候 可以重新输入
while True:
    print('请设置初始属性（max 20)')
    face = int(input('请输入颜值（1-10）： '))
    strong = int(input('请输入体质（1-10）： '))
    iq = int(input('请输入智力（1-10）： '))
    home = int(input('请输入家境（1-10）： '))

    # 判断输入值是否正确
    if face < 1 or face > 10:
        print('颜值输入有误， 请重新输入')
        continue

    if strong < 1 or strong > 10:
        print('体质输入有误， 请重新输入')
        continue

    if iq < 1 or iq > 10:
        print('智力输入有误， 请重新输入')
        continue

    if home < 1 or home > 10:
        print('家境输入有误， 请重新输入')
        continue

    if face + iq + strong + home > 20:
        print('总属性和超过了20  请重新输入')
        continue


    print('初始属性设置完毕！')
    print(f'颜值 {face} 体质 {strong} 智力 {iq} 家庭 {home}')

    break


# 随机生成角色性别

point = random.randint(1, 6)
if point % 2 == 1:
    gender = 'boy'
    print('男孩')
else:
    gender = 'girl'
    print('女孩')


