#coding=utf-8
__author__ = 'Administrator'


# 标识符可以包括英文、数字以及下划线，但不能以数字开头,区分大小写的。


#缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")

#Python语句中一般以新行作为为语句的结束符。但是我们可以使用斜杠（\）将一行的语句分为多行显示
item_one=1
item_two=2
item_three=3
total = item_one + \
        item_two + \
        item_three
#句中包含[], {} 或 () 括号就不需要使用多行连接符
days = ['Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday']


#Python 引号  Python 接收单引号(' )，双引号(" )，三引号(''' """)
word = 'word'
sentence = "This is a sentence."
#三引号可以由多行组成，编写多行文本的快捷语法，
paragraph = """This is a paragraph. It is 
made up of multiple lines and sentences."""

#Python空行
'''函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。
书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分。'''


#等待用户输入
#raw_input("\n\nPress the enter key to exit.")
#同一行显示多条语句
import sys; 
x = 'foo';
sys.stdout.write(x + '\n')


a=6
if a>10 :
    print(">0")
elif a<5 :
    print("<5")
else :
    print("5<=a<=10")

#Python保留字符,所有Python的关键字只包含小写字母
""" and         exec            not
    assert      finally         or
    break       for             pass
    class       from            print
    continue    global          raise
    def         if              return
    del         import          try
    elif        in              while
    else        is              with
    except      lambda          yield"""

#变量赋值
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
a = b = c = 1
a, b, c = 1, 2, "john"






###########################################################################
'''Python数据类型转换
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
'''

#int(x [,base])  将x转换为一个整数
print('1'+'1')
print(int('1')+int('1'))
#long(x [,base] )    将x转换为一个长整数
#3.x没这个
"print(type('1'))"

#float(x)    将x转换到一个浮点数
"print(type(float('1')))"
#complex(real [,imag])   创建一个复数
#str(x)  将对象 x 转换为字符串
#repr(x) 将对象 x 转换为表达式字符串
#eval(str)   用来计算在字符串中的有效Python表达式,并返回一个对象
#tuple(s)    将序列 s 转换为一个元组
#list(s)     将序列 s 转换为一个列表
#set(s)      转换为可变集合
#dict(d)     创建一个字典。d 必须是一个序列 (key,value)元组。
'''dict(one=1, two=2)
dict({'one': 1, 'two': 2})
dict(zip(('one', 'two'), (1, 2)))
dict([['two', 2], ['one', 1]])'''
#frozenset(s)    转换为不可变集合
#chr(x)  将一个整数转换为一个字符
#unichr(x)   将一个整数转换为Unicode字符
#ord(x)  将一个字符转换为它的整数值
#hex(x)  将一个整数转换为一个十六进制字符串
#oct(x)  将一个整数转换为一个八进制字符串v


