# 顺序结构

# 把大象装进冰箱
print('-------程序开始---------')
print('1、打开冰箱门')
print('2、把大象装进冰箱')
print('3、关上冰箱门')
print('-------程序结束---------')

# 选择结构

money = 10000000
s = int(input('请输入取款金额: '))
# 判断余额是否充足
if s > 20000:
    print('取款金额过大，请去柜台办理')
elif money >= s:
    money -= s
    print('取款成功,余额为： ', money)
else:
    print('余额不足')

# 条件判断简写方式
print('取款成功' if money >= s else '取款失败')


score = int(input('请输入成绩： '))
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 90:
    print('B')
else:
    print('不合格')

# pass语句，什么都不做，只是一个占位符
if money >= s:
    pass
else:
    pass

