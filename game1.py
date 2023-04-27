#
import random
import sys

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


# 设定角色出生点
point = random.randint(1, 3)
if home == 10:
    # 第一档
    print('你出生在帝都 你很牛逼')
    home += 1
    iq += 1
    face += 1

elif 9 >= home >= 7:
    # 第二档
    if point == 1:
        print('你出生在二线城市 你还不错 父母是公务员')
        face += 2
    elif point == 2:
        print('你出生在二线城市 你父母是高管 不错')
        home += 2
    else:
        print('你出生在二线城市 你父母是大学教授 不错')
        iq += 2

elif 6 >= home >= 4:
    # 第三档
    if point == 1:
        print('你出生在三线城市 你还不错 父母是医生')
        strong += 1
    elif point == 2:
        print('你出生在三线城市 你父母是老湿 不错')
        iq += 1
    else:
        print('你出生在三线城市 你父母是小饭馆的老板 不错')
        home += 1
else:
    # 第四档
    print('你太惨了')
    if point == 1:
        print('你出生在村子里 父母是农民')
        strong += 1
        face -= 2
    elif point == 2:
        print('你出生在村子里 你父母无业游民')
        home -= 1
    else:
        print('你出生在村子里 但是父母感情不好')
        strong -= 1


print(f'颜值 {face} 体质 {strong} 智力 {iq} 家庭 {home}')


# 幼年阶段
for age in range(1, 11):
    # 把一整阶段的全部存储到一个字符串里面 最后一起打印
    info = f'今年你{age}岁, '

    point = random.randint(1,3)

    # 现在根据随机数生成事件
    if gender == 'gril' and home <= 3 and point == 1:
        info += '你的家里人重男轻女非常严重， 你被遗弃了！'
        print(info)
        print('游戏结束')
        sys.exit()

    # 体质触发的事件
    elif strong < 6 and point < 3:
        info += '你生了一场病， '
        if home >= 5:
            info += '在父母的照料下 你恢复健康了， '
            strong += 1
            home -= 1
        else:
            info += '你的父母没精力管你， 你的身体更糟糕了， '
            strong -= 1
    # 颜值触发事件
    elif face <= 4 and age >= 7:
        info += '你长得太丑了， 其余的小朋友不喜欢你， '
        if iq > 5:
            info += '你决定用学习填充自己， '
            iq += 1
        else:
            if gender == 'boy':
                info += '你和其他小朋友经常打架， '
                strong += 1
                iq -= 1
            else:
                info += '你经常被欺负'
                strong -= 1
