def p(*c):
    print(*c)
a=1
print(a)
print(id(a))

b=1
print(b)
print(id(b))
print(type('asd'))
print(len('whueb我'))
print('pyt'+'hon')
print('why'*7)
print('m"j')

text = 'asdf'
print(text.split('s'))

print(','.join(['asd','fgh']))

ss = 'assssdfgj'
print(ss[2:4])

a = [1,2,'a','s']
print(a)
print(type(1))
print(type(a))
print(type('aa'))

a = [1,2,3,'asd',True]
print(a)
print(a[2:4:1])
a[2] = '88'
print(a)

a.append(['www',1,2,3])
print(a)
a.insert(2,'999')
print(a)

print(a.pop())
a.extend([1,4,6])
print(a)
print(a.count(1))
www = ['w','e','sdf','gfser']
print(www)
www.sort()
print(www)

www.sort(key=len)

print('e' in www)
print(type(www))

asd = [1,2,3,4,6,8]
print(asd)
asd.insert(0,'e')
print(asd)

w = 1,3,5,['w','e',2]
print(w)
print(w[-1].pop())
print(w)

aaa = [-1,-4,3,'eee']
print(aaa)

x = -6
print(x)

y = abs(x)
print(y)

z = aaa[1]
print(z)

q = abs(aaa[1])
print(q)

print(abs(aaa[0]))

a = 'abc'
print(a)
print(a.upper())
print(a)

aaa.append('d')
print(aaa)

print(aaa.pop())
print('------------------------')
foo = a.upper()
print(foo)
print(a.upper())
print('------------------------')

dca = {'Abc':1,'Wdf':2,'Wfj':3,'Ter':4}
print(dca)

p(dca['Wdf'])

del dca['Abc']
p(dca)
p('Wdf' in dca)
print(dca.pop('Wfj'))
p(dca)
p(dca.pop('Wfj','asd'))

p(dca.setdefault('rrr','yui'))
p(dca.keys())
p(dca.values())
dca.clear()
p(dca)
p(None == None)
p('---------------------------------')
a = [4,1,6,8]
index = 0
flag = 1
while flag:
    if index < len(a):
        if a[index] % 2 == 0:
            print(a[index],'next')
        index +=1
    else:
        flag = 0
p('--------------------------------')
get = ['12','23']
for i in get:
    if i not in '0123456789':
        print('error')
    else:
        print('right')
p('-------------------------------')
a = [2,4,6,8]
for i in a:
    if i % 2 == 1:
        print(i)
        break
    else:
        print('ddd')
p('------------------------------')
print(any([0]))
print(isinstance(0,float))

def my_abs(x):
    if x >0:
        return x
    else:
        return -x
p(my_abs(-1))
print('-------------------------------')
sam = [1,2,3,4]
def fc(x):
    sam.append(x)
fc(4)
print(sam)

res = 0
n = 1
wt = 1
while wt:
    if n <101:
        res = res + n
        n = n + 1
    else:
        wt = 0
print(res)

ttt = 0
for i in range(101):
    ttt = ttt + i
print(ttt)
p('--------------------------------------')
r = ''
qqq = "hello, world, nice to meet you!"
for i in qqq:
    if i == 'o':
        r = r + 'a'
    else:
        r = r + i
print(r)

y = ''
q = "hello, world, nice to meet you!"
for i in q:
    if i == 'o':
        y = y
    else:
        y = y + i

print(y)

g = 'ha'
print(g*2)

def n(x,y):
    return x*y
print(n('haha',2))

for i in range(10,0,-1):
    print(i)

def ooo(x):
    res = []
    for i in range(len(x)-1, -1, -1):
        res.append(x[i])
    #return "".join(res)
    return res

print(ooo('hello'))

def wer(x):
    if x == 1:
        return 1
    else:
        return wer(x-1)*x

print(wer(4))

p('-------------------------------------------')

def foo(longString,shortString):
    for i in range(len(longString)-1,-1,-1):
        ok = 1

        for j in range(len(shortString)):
            print('long Str, ', longString[i-j], ' |  short str, ')
            if longString[i-j] != shortString[j]:
                ok = 0
                break
            if ok:
                return i
    return -1
print(foo('abcdefg','ef'))

a = ['12 ','er ']
p(list(map(lambda x: x.strip(),a)))

number = [1,2,3,4]
for i,itemi in enumerate(number):
    number1 = number[:]
    number1.remove(itemi)
    for j,itemj in enumerate(number1):
        number2 =number1[:]
        number2.remove(itemj)
        for k,itemk in enumerate(number2):
            res = []
            res.append(itemi)
            res.append(itemj)
            res.append(itemk)
            p(res)

count = 0
for i in number:
    for j in number:
        for k in number:
            if i!=j and j!=k and i!=k:
                p(i*100+j*10+k)
                count = count+1
p(count)
p('--------------------------------------')
import itertools

p(*itertools.permutations([1,2,3,4],3))
p('--------------------------------------')
p(*map(lambda x: int(''.join(map(str,x))),itertools.permutations([1,2,3,4],3)))
p('--------------------------------------')
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            if i !=0 and i**3 + j**3 + k**3 == i*100+j*10+k:
                p(i*100+j*10+k)

p('------------------------------------')
p(str(123))

for i in range(100,1000):
    if sum(map(lambda x: int(x)**3,str(i))) == i:
        p(i)

# map函数是用于把字符串或者列表中的元素一个个拿出来运用于函数
p('-----------------------------')

p('hello word')
import random
random1 = random.randint(1,10)
oooo = 7
count1 = 0

# while count1 <5:
#     if random1 != oooo:
#         count1 = count1 + 1
#         if random1 > oooo:
#             p('da,try again')
#         else:
#             p('xiao,try again')
#     else:
#         p('game over')
# else:
#     p('error')
count2 = 0
# while True:
#     try:
#         guess = int(input('请输入整数：'))
#         count2 += 1
#     except ValueError:
#         print('int')
#         continue
#     if oooo == random1:
#         p('yes')
#         break
#     elif oooo > random1:
#         p('xiao')
#     else:
#         p('da')
#     if count2 >= 5:
#         p('no')
#         break
p('---------------------------')
def aaa(c):
    p(str(c*9/5+32) + '"F')

a = aaa(8)

def yyy(x):
    return str(x/1000) + 'kg'

p(yyy(1999))
p('-----------------------------')

def ppp(x,y):
    jjj = (x**2 + y**2)**0.5
    return "The right triangle third side's length is" + str(jjj)
p(ppp(3,4))

import random
import math

p('----------------------------------')
n = 0
m = 0
while m <10000:
    a = random.random()
    b = random.random()
    c = (a**2+b**2)**0.5
    if c < 1:
        n += 1
        m += 1
    else:
        m += 1
π = 4*(n/m)
p(π)

def coo(x):
    pol = 0
    for i in range(x):
        x,y = random.random(),random.random()
        dist = x + y
        if dist < 1:
            pol += 1
    π = 4 * (pol/x)
    return π
p(coo(20))

print('hello')
pm = 20
count6 = 0
for i in range(pm):
    x,y = random.random(),random.random()
    dist = x + y
    if dist < 1:
        count6 += 1
π = 4 * (count6/pm)
p(π)

p('-------------------------------')
def hanoi(n,a,b,c):
    if n == 1:
        p('{}->{}'.format(a,c))
    else:
        hanoi(n-1,a,c,b)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)

p(hanoi(2,'A','B','C'))

print('      *','    *****','   *******','  *********',' ***********',
'      |',sep='\n')

# password = ['*##***','123456']
# def www():
#     count = 0
#     while count<=3:
#         password_input = input('请输入密码：')
#         if password_input == password[-1]:
#             p('密码正确')
#         elif password_input == password[0]:
#             reset = input('请重置密码:')
#             password.append(reset)
#             www()
#         else:
#             p('密码错误，请重新输入')
#             count += 1
#     else:
#         p('已输入三次，请等待5分钟后重新输入')
#         break
# www()

# def name():
#     for x in range(11):
#         path_file = 'C:/Users/leo/Desktop/' + str(x) + '.txt'
#         open(path_file,'w')
# name()

def invest(amount,rate,time):
    p('principal amount:'+str(amount))
    for i in range(1,time+1):
        amount = amount*(1+rate)
        p('year '+str(i)+': '+str(amount))
invest(100,0.05,8)

count8 = 0
for i in range(1,101):
    if i%2 == 0:
       count8 += 1
p(count8)
import random
p('-------------------------')
# def point_list():
#     count4 = 0
#     ty = 1
#     point_list = []
#     while ty:
#         point = random.randrange(1,7)
#         count4 += 1
#         if count4 <4:
#             point_list.append(point)
#         else:
#             ty = 0
#     return point_list

# point_list2 = []
#     for i in range(3):
#         point2 = random.randrange(1,7)
#         point_list2.append(point2)

#     return point_list
# points = point_list()
# point_total = sum(points)

# p('<<<<< GAME STARTS >>>>>')
# input1 = input('Big or Small: ')
# p('<<<<< ROLE THE DICE! >>>>>')
# if point_total >= 11 and point_total <=18:
#     output = 'Big'
# else:
#     output = 'Small'
# if input1 == output:
#     p('The points are ' + str(points) + 'You Win!')
# else:
#     p('The points are ' + str(points) + 'You Lose!')

def is_odd(n):
    return n % 2 == 1
foo = [1,2,3,4,5,6]
p(list(filter(is_odd,foo)))

b = [1,2,3,'a','e','r5']
p(list(filter(lambda x: isinstance(x,int),b)))
p(sorted(foo,key = lambda x: x%2,reverse = True))

import sys
p(sys.version)
p(sys.path)

zidian = {'aa':12,'ww':34}
for i in zidian.items():
    key = i[0]
    value = i[1]
    p(key,value)

a = 'rUUUTYd'
b = 'refhsighfsigt'
max1 = max(len(a),len(b))
for i in range(0,max1):
    a1 = a.lower()
    b1 = b.lower()
    numbera = ord(a1[i]) - 96
    numberb = ord(b1[i]) - 96
    if numbera > numberb:
        print('a>b')
        break
    elif numbera < numberb:
        print('a<b')
        break
    else:
        continue

hi = '{55*6*(7-4)}'
L = []
for i in hi:
    if i in '([{':
        L.append(i)
    elif i in ')]}':
        if '([{'.find(L[-1]) == ')]}'.find(i):
            L.pop()
        else:
            L.append(i)
if len(L) %2 == 0:
    p('yes')
else:
    p('no')

stro = 'fsjfs鹏fsspen鹏粉红色覅鹏鹏'

def str_find(x,y):
    result = []
    start = 0
    while True:
        temp = x.find(y,start)
        if temp == (-1): # find函数如果返回-1，则代表找不到
            break
        else:
            result.append(temp)
        start = temp + 1
    return result

p(str_find('fsjfs','鹏'))
p(stro.find('a'))

# f = open('D:/数据分析资料/每日课件/Python 课件/5.29-6.2python基础/bikes.csv')
# p(f.read())
# p(f.close())

# try:
#     f = open('D:/数据分析资料/每日课件/Python 课件/5.29-6.2python基础/bikes.csv')
#     p(f.read())
# finally:
#     f.close()

# import chardet  #编码方式推断
# with open('D:/数据分析资料/每日课件/Python 课件/5.29-6.2python基础/bikes.csv','rb') as f:
#     gg = f.read()
#     p(chardet.detect(gg))   # 必须用rb，以二进制的方式导进来，且必须是纯文本文件才行

# u = open('C:/Users/leo/Desktop/888.txt','w')
# u.write('hfshf\n')
# u.write('5354\n')
# u.write('fsdgds')

# u = open('C:/Users/leo/Desktop/888.txt','a')
# u.write('hfshf\n')
# u.write('5354\n')
# u.write('fsdgds')
# u.close()

import os
p(os.getcwd())  # 获取当前路径
# p(os.chdir(''))  # 转换当前路径

import time
p(time.time())

p(time.localtime(time.time()))
p(time.asctime(time.localtime(time.time()))) # asctime获取可读的时间模式

from datetime import datetime,timedelta
p(datetime.now())
p(datetime.now()+timedelta(days = 2,hours = 10))

import re
ss = 'fshsf+56ih849 hfsnhjf084rfs  uhrh34j fesuig-708/0fs//fdsfsg/n'
pattern = re.compile(r'\d+')
p(pattern.findall(ss))

p(re.findall(r'\d+',ss))

p(re.split('\d+| ',ss))
p(re.findall(r'[+-]?[1-9]\d*',ss))

# r'1[345789]\d{9}'  匹配手机号

p('----------------------------------')
#题目:每组输入一个字符串，按字符串原有的输入顺序，输出字符集合，
# 即重复出现且排位靠后的字母不输出
#方法1
sample = 'fdsgsgrthggfe'
out = ''
for i in sample:
    if i not in out:
        out = out + i
    else:
        continue
p(out)
#方法2
sample2 = 'fdsgsgrthggfe'
p(''.join(sorted(set(sample2),key = sample2.find)))

#方法3
L = []
sss = 'jfdsnskfnerfna'
for i,j in enumerate(sss):
    if i == 0:
        L.append(j)
    else:
        if j in L[0:i]:
            pass
        else:
            L.append(j)
p(L)

p(bin(90))  # 用于转换到二进制
p('------------------------------------')
# 题目：输入一个整数，求该整数二进制表达式中连续出现1最多的次数
#方法1
max0 = 0
max2 = 0
input1 = bin(900)[2:]
for i in input1:
    if i == '1':     # 这里是字符串‘1’
        max2 = max2 + 1
        if max2 > max0:
            max0 = max2
    else:
        max2 = 0   #####
p(max0)

#方法2
p(len(max(sorted(input1.split('0'),key = len))))
p('---------------------------')
# 题目
# 网易2017春招笔试（涂棋盘）
# 小易有一块n*n的棋盘，棋盘的每一个格子都为黑色或者白色，小易现在要用他喜欢的红色
# 去涂画棋盘。小易会找出棋盘中某一列或行中拥有相同颜色的最大的区域去涂画，帮助小易
# 算算他会涂画多少个棋格。
# 输入描述:
# 输入数据包括n+1行：
# 第一行为一个整数n(1 ≤ n ≤ 50),即棋盘的大小
# 接下来的n行每行一个字符串表示第i行棋盘的颜色，’W’表示白色，’B’表示黑色
# 输出描述:
# 输出小易会涂画的区域大小
# 输入例子:
#       3
#      BWW
#      BBB
#      BWW
# 输出例子:
#       3
# n = int(input())
# array = []
# for i in range(0,n):
#     array.append(input())
n = 3
a = 'bww'
b = 'wwb'
c = 'www'
array = [a,b,c]
# 方法1
# 计算行最大
max_count = 0
for i in array:
    max_b = len(max(i.split('w'),key = len))
    max_w = len(max(i.split('b'),key = len))
    max_count = max(max_count,max_b,max_w)
# 转置
sam = [*zip(*array)]
y = [*map(lambda x: ''.join(x),sam)]
# 计算列最大
for i in y:
    max_b = len(max(i.split('w'),key = len))
    max_w = len(max(i.split('b'),key = len))
    max_count = max(max_count,max_b,max_w)
p(max_count)
p('-------------------------')
# 方法2
import re
array = [a,b,c]
ff = len(max(re.findall('b+|w+',' '.join(array)),key = len))
row_array = [*map(lambda x: ''.join(x),zip(*array))]
tt = len(max(re.findall('b+|w+',' '.join(row_array)),key = len))
p(max(ff,tt))


# 题目
# 给定一个一元二次方程的参数，求相应的根（ax^2 + bx + c = 0)
def asd(a,b,c):
    if a == 0:
        p('不是一元二次方程')
        return None
    else:
        delta = b**2 - 4*a*c == 0
        x = b/(-2*a)
        if delta == 0:
            p('有一个根')
            return x
        elif delta > 0:
            p('有两个根')
            x1 = x + delta**0.5/(2*a)
            x2 = x - delta**0.5/(2*a)
            return x1,x2
        else:
            p('无实根')
            return None
p(asd(1,2,1))

# 名企笔试：美团2016招聘笔试（二维数组打印）
#  题目描述
#  有一个二维数组(n*n)，写程序实现从右上角到左下角沿主对角线方向打印。 给定一个二
#  维数组arr及题目中的参数n，请返回结果数组。
#  测试样例：
#  [[1，2，3，4]，[5，6，7，8]，[9，10，11，12]，[13，14，15，16]]，4
#  返回：
#  [4，3，8，2，7，12，1，6，11，16，5，10，15，9，14，13]
life = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(4):
    for j in range(1+i):
        if life[j]:
            p(life[j].pop())
        else:
            continue
for i in range(4):
    for j in life:
        if j:
            p(j.pop())
        else:
            continue
# 输入与第一列中所有项目匹配但与第二列中的所有项目不匹配的正则表达式
# 匹配
#        pit
#        spot
#        spate
#        slap two
#        respite
# 不匹配
#        pt
#        Pot
#        peat
#        part

good = ['pit','spot','spate','slap two','respite']
bad = ['pt','Pot','peat','part']
ggg = re.compile(r'^[sr]\w+\s?\w+|pit') # ^放在中括号里面表示“非”，
                                        #  放在外面表示开头
for i in good:
    p(ggg.search(i).group())   # group表示把search出来的东西展示出来

for i in bad:
    p(ggg.search(i))

# r'^[^p]\w'  表示不是以P开头
# re.compile(r'^[sr]\w+\s?\w+|pit',flag=re.I)  第二个参数flag，re.I表示忽略大小写

#生成18位激活码，内容为数字，大小写字母，不能重复
yyy = '0123456789qwertyuiopasdfghjklzxcvbnm'
#方法1
import random
po = []
for count in range(20):
    ss = ''
    for i in range(18):
        ss = ss + yyy[random.randint(0,35)]
    po.append(ss)
p(po)
p('--------------------------------')
# 方法2
L = set()  # 用集合可以避免重复
count = 20
while len(L) <= count:
    ss = ''
    for i in range(18):
        ss = ss + yyy[random.randint(0,len(yyy)-1)]
    L.add(ss)  # 集合里加内容是用add
p(L)

aaa = 'yyii'
aaa = 'oui'
bbb = aaa
p(aaa)
p(bbb)

a,b,*s = 1,2,3,4   # 用*表示把其余的数值赋值给后面的变量
p(a)
p(s)

a = 0.122
b = 0.122
p(a == b)
p(a is b)
p(a+b)






















































































































































































