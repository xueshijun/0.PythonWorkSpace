#coding=utf-8
'''
Created on 2015-6-29

@author: Administrator
''' 

if __name__ == '__main__':
    pass

import math;
import string;
import copy;

'''=======================================常量 ==================================================================='''
'''
import const
const.value=5
print(const.value)
'''
'''=======================================Python包含六种内建的序列==================================================================='''
''' 1.List（列表）；    2.Tuple（元组）； 3.String（字符串）； 4.Unicode字符串；5.buffer对象；6.xrange对象；'''

'''------------------------------------------通用序列操作-------------------------'''
''' 从左到右索引，第一个元素为0，第二个为1.     从右到左索引，倒数第一个-1，倒数第二个-2，'''

'''------------------------------------------1.序列索引-------------------------'''
greeting='Hello'
print(greeting[0])#H
print('Hello'[0])#H
print(greeting[-1])#o

# fourth=raw_input('Year:')[3] #2015
# print(fourth)#5

'''------------------------------------------2.序列分片-------------------------'''
'''第一个索引为需要提取部分的第一个元素编号，第二个索引为剩余部分的第一个元素编号'''

tag='<a href="http://www.python.org">Python WebSite</a>'
print(tag[9:30])#http://www.python.org

nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[3:6])                #[4,5,6]
print(nums[0:1])                #[1]
#访问最后三个元素
print(nums[7:10])               #[8，9，10]注意:索引10的元素不存在,却是在最后一个元素之后。
print(nums[-3:])                #[8，9，10]
print(nums[:3])                 #[1，2，3]
print(nums[-3:-1])              #[8，9]
print(nums[-3:0])               #[] +++++【注意】：只要分片中最左边的索引比右边的索引晚出现在序列中，则为空序+++++
print(nums[:])                  #[1,2,3,4,5,6,7,8,9,10]

#步长 默认1
print(nums[0:10:1])             #[1,2,3,4,5,6,7,8,9,10]    
print(nums[0:10:2])             #[1,3,5,7,9]
print(nums[3:6:3])              #[4]
#步长    将每4个元素中的第1个元素提取出来
print(nums[::4])                #[1,5,9]
#步长不能为0,可以为负
print(nums[8:3:-1])             #[9,8,7,6,5]
print(nums[0:10:-2])            #[]
print(nums[::-2])               #[10,8,6,4,2]
print(nums[5::-2])              #[6,4,2]
print(nums[:5:-2])              #[10,8]



'''------------------------------------------3.序列加-------------------------'''
#只有相同类型的序列才能连接
print([1,2,3]+[4,5,6])              #[1,2,3,4,5,6]
print('Hello '+'World!')            #Hello World!
#print([1,2,3]+'World!')             #出错


'''------------------------------------------4.序列乘-------------------------'''
print('Hello' * 5)              #HelloHelloHelloHelloHello
print([1,2] * 5)                #[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
#空列表：[]
#创建一个占用10个元素空间，
print([0] * 10)
#创建一个占用10个元素空间，却不包括任何有用内容的列表
print([None] * 10)
 
#Demo
sentence=raw_input("Sentence:")
screen_width=80
text_width=len(sentence)
box_width=text_width+2
magin=(screen_width-text_width)/2;
print(' '*magin +'+'+ '-' *(box_width-2) +'+')
print(' '*magin +'|'+sentence+'|')
print(' '*magin +'+'+ '-' *(box_width-2) +'+')
'''
                              +-------------------+
                              |This is a sentence.|
                              +-------------------+
'''


'''------------------------------------------5.迭代-------------------------'''
for i in range(0,3):
    print("Item {0}".format(i))                 #Item i
    print("Item {0},{1}".format("Hello",i))     #Item Hello,i
'''------------------------------------------6.成员资格-------------------------'''
permission='rw'
print('r' in permission)                        #True
print('x' in permission)                        #False

users=['tom','jack','sony']
print(raw_input("name:") in users)

subject='$$$Get rich now!$$$'
print('$$$' in subject)                         #True            

database=[
          ['XUE1','1111'],
          ['XUE2','2222'],
          ['XUE3','3333'],
          ['XUE4','4444'],
          ['XUE5','5555']
     ]
# username=raw_input("UserName:")
# pin=raw_input("PIN:")
# if([username,pin] in database):print("Access Granted!")

'''------------------------------------------7.序列长度-------------------------'''
'''------------------------------------------8.最大元素-------------------------'''
'''------------------------------------------9.最小元素-------------------------'''
nums=[1,312,43,645]
print(len(nums))
print(max(nums))
print(min(nums))



print(
      '''========================================五个标准的数据类型========================================================================''')

''' 1.Numbers（数字）；    2.String（字符串）；    3.List（列表）；    4.Tuple（元组）；    5.Dictionary（字典）''' 



print(
'''----------------------------------------1.Numbers----------------------------------------------------------------------------''')
''' 
数字数据类型用于存储数值。
他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
当你指定一个值时，Number对象就会被创建:'''
var1 = 1
var2 = 10
var3=12
'使用del语句删除一些对象引用。' \
'del语句的语法是：del var1[,var2[,var3[....,varN]]]]'
del var1
del var2, var3

########################Python支持四种不同的数值类型：
''' int（有符号整型）:
        10   100     -782    080     -0490       -0x260      0x69
    long（长整型[也可以代表八进制和十六进制]）
                            长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型。
        51924361L   -0x19323L   0122L   0xDEFABCECBDAECBFBAEl    535633629843L
        -052318172735L  -4721885298529L
    float（浮点型）
        0.0     15.20   -21.9       32.3+e18    -90.    -32.54e100      70.2-E12
    bool（布尔型）
        true    false
    complex（复数）
        Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
        3.14j   45.j    9.322e-36j      .876j       -.6545+0J       3e+26J      4.53e-7j
'''

########################Python数字类型转换
'''
int(x [,base ])         将x转换为一个整数
long(x [,base ])        将x转换为一个长整数
float(x )               将x转换到一个浮点数
complex(real [,imag ])  创建一个复数
str(x )                 将对象 x 转换为字符串
repr(x )                将对象 x 转换为表达式字符串
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s )               将序列 s 转换为一个元组
list(s )                将序列 s 转换为一个列表
chr(x )                 将一个整数转换为一个字符
unichr(x )              将一个整数转换为Unicode字符
ord(x )                 将一个字符转换为它的整数值
hex(x )                 将一个整数转换为一个十六进制字符串
oct(x )                 将一个整数转换为一个八进制字符串
'''

###############Python数学函数
'''
函数    返回值 ( 描述 )
abs(x)          返回数字的绝对值，如abs(-10) 返回 10
fabs(x)    返回数字的绝对值，如math.fabs(-10) 返回10.0

ceil(x)         返回数字的上入整数，如math.ceil(4.1) 返回 5
floor(x)    返回数字的下舍整数，如math.floor(4.9)返回 4

cmp(x, y)       如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1

exp(x)    返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045

log(x)    如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)    返回以10为基数的x的对数，如math.log10(100)返回 2.0

max(x1, x2,...)    返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)    返回给定参数的最小值，参数可以为序列。

modf(x)    返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)    x**y 运算后的值。
round(x [,n])    返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)    返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j
'''
#################################Python随机数函数
'''
函数    描述
choice(seq)    从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])    从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()    随机生成下一个实数，它在[0,1)范围内。
seed([x])    改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)    将序列的所有元素随机排序
uniform(x, y)    随机生成下一个实数，它在[x,y]范围内。
'''

################################Python三角函数
'''
函数    描述
sin(x)    返回的x弧度的正弦值。
cos(x)    返回x的弧度的余弦值。
tan(x)    返回x弧度的正切值。
asin(x)    返回x的反正弦弧度值。
acos(x)    返回x的反余弦弧度值。
atan(x)    返回x的反正切弧度值。
atan2(y, x)    返回给定的 X 及 Y 坐标值的反正切值。
hypot(x, y)    返回欧几里德范数 sqrt(x*x + y*y)。
degrees(x)    将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)    将角度转换为弧度
'''
###############################Python数学常量
'''
常量    描述
pi    数学常量 pi（圆周率，一般以π来表示）
e    数学常量 e，e即自然常数（自然常数）。
''' 
print(
'''----------------------------------------2.String（字符串）----------------------------------------------------------------------------''')
 
''' python的字串列表有2种取值顺序:
        从左到右索引，第一个元素为0，第二个为1.
        从右到左索引，倒数第一个-1，倒数第二个-2，

    截取相应的字符串:下标是从0开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
        变量[头下标:尾下标]
'''


#########################################    Python三引号（triple quotes）
'''
python中三引号可以将复杂的字符串进行复制:
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。
'''
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''

"""
cursor.execute('''
CREATE TABLE users (
login VARCHAR(8),
uid INTEGER,
prid INTEGER)
''')
"""
################################    字符串运算符
'''
a="Hello"
b="Python"
操作符                                描述    实例
+            字符串连接    a + b 输出结果： HelloPython
*            重复输出字符串    a*2 输出结果：HelloHello
[]           通过索引获取字符串中字符    a[1] 输出结果 e
[ : ]        截取字符串中的一部分    a[1:4] 输出结果 ell
in           成员运算符 - 如果字符串中包含给定的字符返回 True    H in a 输出结果 1
not in       成员运算符 - 如果字符串中不包含给定的字符返回 True    M not in a 输出结果 1
r/R          原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。    print r'\n' prints \n 和 print R'\n' prints \n
%            格式字符串
''' 
s = 'ilovepython'
print(s[1:5])                       #love。
str1 = 'Hello World!'
print(str1)                         # 输出完整字符串Hello World!
print(str1[0])                      # 输出字符串中的第一个字符H
print(str1[2:5])                    # 输出字符串中第三个至第五个之间的字符串llo
print(str1[2:])                     # 输出从第三个字符开始的字符串llo World
print(str1 * 2)                     # 输出字符串两次Hello World!Hello World!
print(str1 + "TEST")                # 输出连接的字符串Hello World!TEST
#Python不支持单字符类型，单字符也在Python也是作为一个字符串使用。

################################    字符串更新
var1 = 'Hello World!'
print("Updated String :- ", var1[:6] + 'Python')

################################    字符串格式化符号:
'''
python字符串格式化符号
    符   号    描述
     %c     格式化字符及其ASCII码
     %s     格式化字符串
     %d     格式化整数
     %u     格式化无符号整型
     %o     格式化无符号八进制数
     %x     格式化无符号十六进制数
     %X     格式化无符号十六进制数（大写）
     %f     格式化浮点数字，可指定小数点后的精度
     %e     用科学计数法格式化浮点数
     %E     作用同%e，用科学计数法格式化浮点数
     %g     %f和%e的简写
     %G     %f 和 %E 的简写
     %p     用十六进制数格式化变量的地址

格式化操作符辅助指令:
    符号    功能
    *    定义宽度或者小数点精度
    -    用做左对齐
    +    在正数前面显示加号( + )
    <sp>    在正数前面显示空格
    #    在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
    0    显示的数字前面填充'0'而不是默认的空格
    %    '%%'输出一个单一的'%'
    (var)    映射变量(字典参数)
    m.n.    m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''

print("I'm %s. I'm %d year old" % ('Jack', 99))                             #I'm Jack. I'm 99 year old
print("I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99})    #I'm Vamei. I'm 99 year old

print('%10f'    % (math.pi))                 #  3.141593
print('%10.2f'  % (math.pi))                 #      3.14
print('%.2f'    % (math.pi))                 #3.14 
print('%.5s'    % ('China!I love you!'))        #China

'''
%[(name)][flags][width].[precision]typecode
(name)       为命名
flags        可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
width        表示显示宽度
precision    表示小数点后精度
'''

################################    在宽度和精度值之前可以放置一个标表:零、加号、减号、空格
print("%+10x" % 10)                             #+a
print("%+10d" % 10)                             #+10
print("%04d" % 5)                               #0005
print('%010.2f' % math.pi)                      #0000003.14
print("%6.3f" % 2.3)                            # 2.300
#-号用来左对齐
print('%-10.2f' % math.pi)                      #3.14
#空白在正数前加空格
print('% 5d' %   10)                            #   10
print('% 5d' %   -10)                           #  -10

#上面的width, precision为两个整数。我们可以利用*，来动态代入这两个量。实际的模板为"%.4f"。
print("%.*f" % (4, 1.2))                        #1.2000



################################    转义字符:
#\xyy    十六进制数，yy代表的字符，例如：\x0a代表换行
"""
转义字符    描述
\(在行尾时)    续行符
\\    反斜杠符号
\'    单引号
\"    双引号
\a    响铃
\b    退格(Backspace)
\e    转义
\000    空
\n    换行
\v    纵向制表符
\t    横向制表符
\r    回车
\f    换页
\oyy    八进制数，yy代表的字符，例如：\o12代表换行
\other    其它的字符以普通格式输出
"""
keywords="I'm a Chinese";
print(keywords)     #I'm a Chinese
path='C:\\programs'
print(path)         #C:\programs

'''原字符串以r开头,可以在原始字符串中放入任何字符，但是不能再原始字符串结尾输入反斜线'''
path=r'C:\\programs'
print(path)         #C:\\programs
path=r'C:\\programs''\\'
print(path)         #C:\\programs\




############################################Unicode 字符串
'''python中的普通字符串在内部是以8位的ASCII形成存储，而Unicode字符串则存储为16位的Unicode字符'''
myunicode=u'HelloWorld'
print(myunicode)#HelloWorld



##########################################    字符串常量
print(string.digits)                                    #数字
#具体值取决于python所配置的语言
print(string.letters)                                   #
#确定使用ascii
print(string.ascii_letters)
print(string.letters)                                   #
print(string.lowercase)
print(string.uppercase)
print(string.printable)                                 #可打印字符
print(string.punctuation)                               #所有标点字符


##########################################    字符串内建函数
#    string.capitalize()                                                   把字符串的第一个字符大写

#    string.count(str, beg=0, end=len(string))                             返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
'''
string.encode(encoding='UTF-8', errors='strict')
以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
string.decode(encoding='UTF-8', errors='strict')
以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者'replace'

str = "this is string example....wow!!!";
str = str.encode('base64','strict');
print("Encoded String: " + str);
print("Decoded String: " + str.decode('base64','strict'));
'''




#   string.expandtabs(tabsize=8)                                              把字符串 string 中的 tab 符号转为空格，默认的空格数 tabsize 是 8.
str1 = "this is\tstring example....wow!!!";
print("Original string: " + str1)                                        #this is    string example....wow!!!
print("Default exapanded tab: " +  str1.expandtabs());                   #this is string example....wow!!!
print("Double exapanded tab: " +  str1.expandtabs(16));                  #this is         string example....wow!!!

#   string.center(width)                                                     返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
str1 = "this is string example....wow!!!";
print("str.center(40) : ", str1.center(40))                              #      this is string example....wow!!!
print("str.center(40, 'a') : ", str1.center(40, 'a'))                    #aaaathis is string example....wow!!!aaaa

#   string.ljust(width)                                                      返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
#   string.rjust(width)                                                      返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
#   string.zfill(width)                                                      返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
str1 = "this is string example....wow!!!";
print(str1.ljust(50, '0'))                                               #this is string example....wow!!!000000000000000000

#   string.startswith(obj, beg=0,end=len(string))                            检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
#   string.endswith(obj, beg=0, end=len(string))                             检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
#   string.find(str, beg=0, end=len(string))                                 返回子串所在位置的最左端索引，如果是返回开始的索引值，否则返回-1
#   string.rfind(str, beg=0,end=len(string) )                                类似于 find()函数，不过是从右边开始查找.
str1='$$$ Get rich now!!! $$$'
print(str1.find('$$$'))                         #0
print(str1.find('!!!'))                         #16
print(str1.find('!!!',0,16))                    #-1

#   string.index(str, beg=0, end=len(string))                                跟find()方法一样，只不过如果str不在 string中会报一个异常.
#   string.rindex( str, beg=0,end=len(string))                               类似于 index()，不过是从右边开始
str1 = "this is string example....wow!!!";
print(str1.rindex("is"));                       #5
print(str1.index("is"));                        #2

#   string.partition(str)                                                    有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
#   string.rpartition(str)                                                   类似于 partition()函数,不过是从右边开始查找.
str1 = "http://www.w3cschool.cc/"
print(str1.partition("://"))                                             #('http', '://', 'www.w3cschool.cc/')


#   string.isalnum()                                                         如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
#   string.isalpha()                                                         如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
#   string.isdecimal()                                                       如果 string 只包含十进制数字则返回 True 否则返回 False.
#   string.isdigit()                                                         如果 string 只包含数字则返回 True 否则返回 False.
#   string.islower()                                                         如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
#   string.isupper()                                                         如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
#   string.isnumeric()                                                       如果 string 中只包含数字字符，则返回 True，否则返回 False
#   string.isspace()                                                         如果 string 中只包含空格，则返回 True，否则返回 False.
#   string.istitle()                                                         如果 string 是标题化的(见 title())则返回 True，否则返回 False
#   string.isdecimal()                                                       isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
#   string.join(seq)                                                         #以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
str1 = "-";
seq = ("a", "b", "c");
print(str1.join( seq ))                                                  #a-b-c
# 失败,需要添加的队列元素必须是字符串
# str1 = "+";
# seq = [1,2,3,4,5]
# print(str1.join( seq )) #  
str1 = "+";
seq = ['1','2','3','4','5']
print(str1.join( seq ))                                                 #1+2+3+4+5  
dirs=('','usr','bin','env')
print('/'.join(dirs))                                                   #usr/bin/env
print('C:'+'\\'.join(dirs))                                             #C:\usr\bin\env

#    max(str)                                                                返回字符串 str 中最大的字母。
#    min(str)                                                                返回字符串 str 中最小的字母。


#   string.lower()                                                           转换 string 中所有大写字符为小写.
#   string.upper()                                                           转换 string 中的小写字母为大写
#   string.swapcase()                                                        翻转 string 中的大小写
#   string.title()                                                           返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
#   string.translate(str, del="")                                            根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
if('JACK' in ['jack','tom']):print('JACK IN list')

str1 = "this is string example....wow!!!";
print(str1.title());                                                    #This Is String Example....Wow!!!



#   string.lstrip()                                                          截掉 string 左边的空格
#   string.rstrip()                                                          删除 string 字符串末尾的空格.
#   string.strip([obj])                                                      在 string 上执行 lstrip()和 rstrip()
#   string.replace(str1, str2,  num=string.count(str1))                      把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
#   string.split(str="", num=string.count(str))                              以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
#   string.splitlines(num=string.count('\n'))                                按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.
print('Hello world!'.replace('world', 'python'))
print('1+2+3+4+5'.split('+'))                                           #['1','2','3','4','5']
print('/usr/bin/env'.split('/'))                                        #['','usr','bin','env']

var="你好中国    Hello China";
print(repr(var))                                                        #返回字符串的表现形式        '\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\xad\xe5\x9b\xbd  Hello China'

#   string.maketrans(intab, outtab])                                         maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
#转换表是包含替换ASCII字符集中256个字符的替换字母的字符串
str1 = "this is string example....wow!!!";
table  = string.maketrans("aeiou", "12345")
print(len(table))                                                       #256
print(table[97:123])                                                    #1bcd2fgh3jklmn4pqrst5vwxyz
print(string.maketrans('','')[97:123])                                  #abcdefghijklmnopqrstuvwxyz
print(str1.translate(table));                                           #th3s 3s str3ng 2x1mpl2....w4w!!!
#并删除所有空格
print(str1.translate(table,' '));                                       #th3s3sstr3ng2x1mpl2....w4w!!!




print(
'''---------------------------------------3.List（列表） 是 Python 中使用最频繁的数据类型。-------------------------------------------------------------------''')
'''
    截取相应的列表，
    从左到右索引默认0开始的，
    从右到左索引默认-1开始，
    下标可以为空表示取到头或尾。
    加号（+）是列表连接运算符，星号（*）是重复操作
'''
##########################################    字符串与列表相互转换
list3=list('Hello')                                             #字符串不可以修改，可以转成列表['H','e','l','l','o']
str3=''.join(list3)


##########################################    访问列表中的值
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print("list1[0]: ", list1[0])       #physics
print("list2[1:5]: ", list2[1:5])   #[2, 3, 4, 5]




##########################################    分片赋值
list1 = list('Perl')        #['P', 'e', 'r', 'l']
print(list1)
#替换与原序列一样长
list1[2:]=list('ar')        #['P', 'e', 'a', 'r']
print(list1)
#替换与原序列不一样长
list1[1:]=list('ython')     #['P', 'y', 't', 'h','o','n']
print(list1)
#通过分片赋值插入元素
numbers=[1,5]
numbers[1:1]=[2,3,4]
print(numbers)              #[1,2,3,4,5]

#通过分片赋值删除元素
numbers=[1,2,3,4,5]
numbers[1:4]=[]
print(numbers)              #[1,5]

##########################################    更新列表
list1 = ['physics', 'chemistry', 1997, 2000]
print(list1[2])  #1997
list1[2] = 2001 
print(list1[2])  #2001

##########################################    删除列表元素
list1 = ['physics', 'chemistry', 1997, 2000];
del list1[2];
print("After deleting ",list1)       #['physics', 'chemistry', 2000]

##########################################    Python列表脚本操作符
#列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
print(len([1, 2, 3]))           #    3    长度
print([1, 2, 3] + [4, 5, 6])    #    [1, 2, 3, 4, 5, 6]    组合
print(['Hi!'] * 4)              #    ['Hi!', 'Hi!', 'Hi!', 'Hi!']    重复
print(3 in [1, 2, 3])           #    True    元素是否存在于列表中
for x in [1, 2, 3]:
    print(x)#    1 2 3    迭代

#Python列表截取
list1 = [1, 2, 3]
print(list1[2])         #   3    读取列表中第三个元素
print(list1[-2])        #   2    读取列表中倒数第二个元素
print(list1[1:])        #   [2,3]    从第二个元素开始截取列表

#Python列表函数
#   cmp(list1, list2)   比较两个列表的元素
#   len(list)   列表元素个数
#   max(list)   返回列表元素最大值
#   min(list)   返回列表元素最小值
#   list(seq)   将元组转换为列表

##########################################    Python列表方法
#1.   list.append(obj)    在列表末尾添加新的对象
list1=[1,2,3]
list1.append(4) 
print(list1)            #[1,2,3,4]
#2.   list.count(obj)     统计某个元素在列表中出现的次数
print(['to','be','or','not','to','be'].count('to'))     #2
list1=[[1,2] , 1 , 1 , [2,1,[1,2]]]
print(list1.count(1))                                   #2
print(list1.count([1,2]))                               #1
#3.   list.extend(seq)    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list1=[1,2,3,4]
list2=[3,4,5,6]
list1.extend(list2)
print(list1)                    #[1,2,3,4,3,4,5,6]
list1=[1,2,3,4]
list2=[3,4,5,6]
print(list1+list2)              #[1,2,3,4,3,4,5,6]
'''两者区别：前者改变被扩展的序列,连接操作创建了包含list1和list2副本的新列表'''
list1=[1,2,3,4]
list2=[3,4,5,6]
list1[len(list1):]=list2
print(list1)                    #[1,2,3,4,3,4,5,6] 

#4.   list.index(obj)     从列表中找出某个值第一个匹配项的索引位置
list1=['We','are','the','knights','who','say','ni']
print(list1.index('who'))       #4

#5.   list.insert(index, obj) 将对象插入列表
list1=[1,2,3,5,6]
list1.insert(3,'four')
print(list1)                    #[1,2,3,'four',5,6]
list1=[1,2,3,5,6]
list1[3:3]=['four'];
print(list1)                    #[1,2,3,'four',5,6]

#6.   list.pop(obj=list[-1])  移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list1=[1,2,3]
print(list1.pop())              #3
print(list1)                    #[1,2]

list1=[1,2,3]
list1.append(list1.pop())
print(list1)                    #[1,2,3]

#7.   list.remove(obj)    移除列表中某个值的第一个匹配项
list1=['to','be','or','not','to','be']
list1.remove('be')
print(list1)                    #['to','or','not','to','be']

#8.   list.reverse()      反向列表中元素
list1=[1,2,3]
list1.reverse()
print(list1)                    #[3,2,1]


#9.   list.sort([func])   对原列表进行排序
#*******易错*******#
list1=[4,6,2,1,7,9]
#将list1的副本赋值给list2
#区别list2=list1    这让list1和list2都指向一个列表
list2=list1[:]
list2.sort()    
print(list1)                #[4,6,2,1,7,9]
print(list2)                #[1,2,4,6,7,9]

list1=[4,6,2,1,7,9]
list2=sorted(list1)
print(list1)                #[4,6,2,1,7,9]
print(list2)                #[1,2,4,6,7,9]

print(sorted('Python'))     #['P', 'h', 'n', 'o', 't', 'y']



print(
'''---------------------------------------4.Tuple（元组）-------------------------------------------------------------------''')
'''元组用"()"标识。内部元素用逗号隔开。但是元素不能修改。'''
tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print(tuple1)                   # ('abcd', 786, 2.23, 'john', 70.2)    输出完整元组
print(tuple1[0])                # abcd                                 输出元组的第一个元素
print(tuple1[1:3])              # (786, 2.23)                          输出第二个至第三个的元素
print(tuple1[2:])               # (2.23, 'john', 70.2)                 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)            # (123, 'john', 123, 'john')           输出元组两次
print(tuple1 + tinytuple)       # ('abcd', 786, 2.23, 'john', 70.2, 123, 'john')    打印组合的元组

#空元组
tuple2=()
#实现一个值的元组,必须加逗号，即使一个值
tuple2=(1,)

tuple1=3*(40+2)
print(tuple1)                   #126
tuple1=3*(40+2,)       
print(tuple1)                   #(42,42,42)

#tuple函数
print(tuple([1,2,3]))           #(1,2,3)
print(tuple('abc'))             #('a','b','c')
print(tuple((1,2,3)))           #(1,2,3)



##########################################    Python基本元组操作
# 访问元组 元组可以使用下标索引来访问元组中的值，如下实例:
tup = ('physics', 'chemistry', 1997, 2000);
print(tup[0])                   #'physics'   
tup = (1, 2, 3, 4, 5, 6, 7 )
print(tup[1:5])     
#修改元组   元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
# 以下修改元组元素操作是非法的。
# tup1[0] = 100;
# 创建一个新的元组
tup3 = tup1 + tup2;
print(tup3);


# #删除元组
# tup = ('physics', 'chemistry', 1997, 2000);
# print(tup);
# del tup;
# print( "After deleting tup : "+tup)

#元组运算符
print(len((1, 2, 3)))           #   3    计算元素个数
print((1, 2, 3) + (4, 5, 6))    #   (1, 2, 3, 4, 5, 6)    连接
print(['Hi!'] * 4)              #   ['Hi!', 'Hi!', 'Hi!', 'Hi!']    复制
print(3 in (1, 2, 3))          #True    元素是否存在
for x in (1, 2, 3): print(x)     #   1 2 3    迭代

#元组索引、元组截取
L = ('spam', 'Spam', 'SPAM!')
print(L[2]) #    'SPAM!'    读取第三个元素
print(L[-2])#    'Spam'    反向读取；读取倒数第二个元素
print(L[1:])#    ('Spam', 'SPAM!')    截取元素


#无关闭分隔符 任意无符号的对象，以逗号隔开，默认为元组
print('abc', -4.24e93, 18+6.6j, 'xyz')#abc -4.24e+93 (18+6.6j) xyz
x, y = 1, 2;
print( "Value of x , y : ", x,y)#Value of x , y :  1 2


#Python元组包含了以下内置函数
#   cmp(tuple1, tuple2)
#   len(tuple)
#   max(tuple)
#   min(tuple)
#   tuple(seq)









print(
      '''---------------------------------------5.Dictionary（字典）-------------------------------------------------------------------''')
'''字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。
列表是有序的对象结合，字典是无序的对象集合。
字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。'''
dict1 = {}
dict1['one'] = "This is one"
dict1[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict1)                                                # {2: 'This is two', 'one': 'This is one'}
print(dict1['one'])                                         # This is one
print(dict1[2])                                             # This is two
print(tinydict)                                             # {'dept': 'sales', 'code': 6734, 'name': 'john'}
print(tinydict.keys())                                      # ['dept', 'code', 'name']
print(tinydict.values())                                    # ['sales', 6734, 'john']

##########################################    dict函数
items=[('name','Jack'),('age','20')]
dict1=dict(items)                                                       
print(dict1)                                                # {'age': '20', 'name': 'Jack'}  

##########################################    基本字典操作
#    len(d)
dict1= {'age': '20', 'name': 'Jack'}
print(len(dict1))
print(dict1['age'])
dict1['age']=27
dict1['gender']='男'                             #相当于新增一个
del dict1['age']
#字典中检查成员资格更加有效
if('age' in dict1):print('')                    #

'''
键类型不一定为整型数据
自动增加，假如键字典中不存在时，也可以赋值，相当于新增
成员资格，查找的是键，
'''

##########################################    字典示例
people={
            'Alice':{
                     'phone':'1234',
                     'addr':'China'
                     },
            'Jack':{
                     'phone':'5678',
                     'addr':'Japan'
                     },
            'Beth':{
                     'phone':'9012',
                     'addr':'Canada'
                     }
        }
labels={
       'phone':'phone number',
       'addr':'address'
        }
print(people)
name=raw_input("Name:")
if name in people:print ("%s's %s is %s."    % \
                           (name,labels['phone'],people[name]['phone']))



##########################################    字典格式化字符串
dict1={'title':'this is title!','text':'this is text!'}
temp='''<html>
            <head><title>%(title)s</title></head>
            <body>
                <h1>%(title)s</h1>
                <p>%(text)s</p>
            </body>    
        </html>'''
print(temp  %   dict1)


##########################################    字典方法
#1.    clear    
d= {'age': '20', 'name': 'Jack'}
d.clear()           #无返回值或返回值为None            
print(d)                                                #{}

#2.    copy        浅复制
'''在副本中替换值,原字典不受影响,
            但是若是修改某个值,而不是替换,则原字典的值也会变化
'''
d1={'name':'jack','age':'18'}
c1=copy.copy(d1)
print(c1)                                                #{'age': 18, 'name': 'jack'}
c1['name']='tony'
c1['age']='20'
c1['gender']='man'
print(d1)                                                #{'age': 18, 'name': 'jack'}
print(c1)                                                #{'gender': 'man', 'age': '20', 'name': 'tony'}

d2 = {'name':'jack','age':'18'}
c2=copy.copy(d2)
d2['name']='tony'
d2['age']=20
print(d2)                                                #{'age': 20, 'name': 'tony'}
print(c2)                                                #{'age': '18', 'name': 'jack'}

#    deepcopy    深度复制
d3= {'name':'jack','age':'18'}
print(d3)                                #{'age': 18, 'name': 'jack'} 
c3=copy.copy(d3)
print(c3)                                #{'age': 18, 'name': 'jack'} 
dc3 = copy.deepcopy(d3)
#修改原始字典
d3['gender']='Man'           #新增一个项
d3['name']='tony'            #修改一个项 
print(c3)                                #{'age': 18, 'name': 'jack'}
print(d3)                                #{'gender': 'Man', 'age': 18, 'name': 'tony'}
print(dc3)                               #{'age': 18, 'name': 'jack'}

d4 = {'name':'jack','age':'18'}
print(d4)                                #{'age': 18, 'name': 'jack'} 
c4=copy.copy(d4)
print(c4)                                #{'age': 18, 'name': 'jack'} 
dc4 = copy.deepcopy(d4)
#修改深度拷贝的字典
dc4['gender']='Man'           #新增一个项
dc4['name']='tony'            #修改一个项 
print(c4)                                #{'age': 18, 'name': 'jack'}
print(d4)                                #{'age': 18, 'name': 'jack'}
print(dc4)                               #{'gender': 'Man', 'age': 18, 'name': 'tony'}



#3.    fromkey    使用给定的键建立新的字典,每个键对应的值为None
dict1={}.fromkeys(['name','age'])
print(dict1)                            #{'age': None, 'name': None}
#使用指定的默认值
dict1=dict.fromkeys(['name','age'],'(unknown)')
print(dict1)                            #{'age': '(unknown)', 'name': '(unknown)'}



#4.    get    
#访问不存在的键时，不会出异常,返回None
print dict1.get('tech')
#自定义不存在该键时返回值
print dict1.get('tech','N/A')

#5.    has_key    等价于k in d        
#Python 3.0中不存在


#6.    items                将字典中的键值对以列表返回
#      iteritems
d={'title':'标题党','text':'正文'}
print(d.items())                            #[('text', '标题党'), ('title', '正文')]

#7.    keys    以列表形式返回
#8.    pop    弹出,并从字典中移除
d={'x':1,'y':2}
print(d)                                    #{'y': 2, 'x': 1}
print(d.pop('x'))                           #1

#iterkeys


#9.    popitem    弹出随机项,若想一个个移除时,比较高效
#区别于list.pop
d={
    'title':'Python WebSite',
    'url':'www.baidu.com'
   }
print(d.popitem())


#10.   setdefault        当键值不存在的时候设置默认值
d={}
d.setdefault('name','N/A')      
print(d)                                            #{'name': 'N/A'}

d['name']='Alice'
d.setdefault('name','N/A')
print(d)                                            #{'name': 'Alice'}

#11.   update
d={
    'title':'Python WebSite',
    'url':'www.baidu.com'
   }
print(d)                                            #{'url': 'www.baidu.com', 'title': 'Python WebSite'}
x={'title':'HelloWebSite'}
d.update(x)
print(d)                                            #{'url': 'www.baidu.com', 'title': 'HelloWebSite'}

#12.   values和itervalues    以列表形式返回字典中的数据
d={}
d[1]=1
d[2]=2
d[0]=0 
print("%s:%s"   %   ("values",d.values()))          #values:[0, 1, 2]
print("%s:%s"   %   ("viewitems",d.viewitems()))    #viewitems:dict_items([(0, 0), (1, 1), (2, 2)])
print("%s:%s"   %   ("viewkeys",d.viewkeys()))      #viewkeys:dict_keys([0, 1, 2])
print("%s:%s"   %   ("viewvalues",d.viewvalues()))  #viewvalues:dict_values([0, 1, 2])






print(
      '''========================================赋值、输出、import的一些用法========================================================================''')
#打印多个表达式
print 'age',42                                          #age 42
print 1,2,3                                             #1 2 3
print(1,2,3)                                            #(1,2,3)

name='Alice'
salutation='MR.'
greeting='Hello.'
print('%s.%s.%s' % (greeting,salutation, name))                       #Hello.MR.Alice

#导入模块
#from somemodule import somefunction,antherfunction
#from somemodule import * 

#设置别名
#from somemodule as module1
#from othermodule as module2
#module1.open()
#module2.open()

#from somemodule import open as open1
#from othermodule import open as open2

##########################################    赋值-序列解包
x,y,z=1,2,3
print x,y,z                         #1 2 3
x,y=y,x
print x,y,z                         #2 1 3

val=1,2,3
print(val)                          #(1,2,3)

x,y,z=val
print(x)                            #1


d={
    'title':'Python WebSite',
    'url':'www.baidu.com'
   }
print(d.popitem())
key,val=d.popitem()
print(key)
print(val)




##########################################    赋值-链式赋值
'''
x=y=sunmefunction()

等价写法
y=sunmefunction()
x=y

不一定等价
y=sunmefunction()
x=sunmefunction()
'''
##########################################    赋值-增量赋值
x=2
x+=1
x*=2

msg='foo'
msg+='bar'
msg*=2









print(
      '''========================================条件语句========================================================================''')

'''
下面的值作为布尔表达式的时候为假,
其他一切都解释为真
False    None    0    ""    ()    []    {}
'''
print(True==1)                          #False
print(False==0)                         #True
print(True+False+42)                    #43

print(bool('Hello'))                    #True
print(bool(42))                         #True
print(bool(''))                         #False
print(bool(0))                          #False




name = 'luren'
if name == 'python':
    if(name.startswith('Mr。')):
        print('Mr. boss') 
    elif name.startswith('Mrs'):
        print('Mrs. boss')       
      
else:
    print(name)

num = 5
if num == 3:         
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:          
    print('error')
else:
    print('roadman')   



x = 9
y = 10
list1=[1,3,8,9]
if(x==y):
    print("")
    if("foo"=="foo"):print("")              #True
elif x!=y:
    if(x >= 0 and x <= 10 ):   
        print('hello')
    elif(x < 0 or x > 10):     
        print('hello')
    else:
        print('undefine')

x = y = [1,2,3,4]
z =  [1,2,3,4]
if(x == y):                             
    print(x == y)                           #True
if(x == z):                             
    print(x == z)                           #True
if(x is y):                             
    print(x is y)                           #True
if(x is z):                             
    print(x is z)                           #False


if(x in list1):
    print("")
elif(x not in list1):
    print("")

num = 8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15): # 判断值是否在0~5或者10~15之间
    print('hello')
else:
    print('undefine') # 输出结果undefine


#按照字母顺序排列进行比较
if ( 'alpha'  < 'beta' ) : print('alpha'  < 'beta')                         #True                            

if('FnOrD'.lower()=='Fnord'.lower()): print("")                             #True                          

if([2,[1,4]]<[2,[1,5]]): print("")                                          #True    
  
  



##########################################    断言
# 让程序在出现错误条件时直接崩溃
'''
1、assert语句用来声明某个条件是真的。
2、如果你非常确信某个你使用的列表中至少有一个元素，而你想要检验这一点，并且在它非真的时候引发一个错误，那么assert语句是应用在这种情形下的理想语句。
3、当assert语句失败的时候，会引发一AssertionError。
'''
# age=-1
# assert 0<age<100,'The age must be realistic'




print(
      '''========================================循环语句========================================================================''')

'''
循环控制语句    描述
break 语句    在语句块执行过程中终止循环，并且跳出整个循环
continue 语句    在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
pass 语句    pass是空语句，是为了保持程序结构的完整性。
'''
count = 0
while (count < 2):
    print('The count is:', count)
    count = count + 1

name=''
while not name or name.isspace():   #while not name.strip():
    name=raw_input("Please enter your name:")
print('Hello.%s!' % name)
#死循环
'''
while (1): 
    print('Given flag is really true!')
print("Good bye!")
'''


#循环使用 else 语句
#else 中的语句会在循环正常执行完的情况下执行
count = 0
while count < 2:
    print(count, " is  less than 2")
    count = count + 1
else:
    print(count, " is not less than 2")

#for
for letter in 'Python':     # First Example
    print('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
    print('Current fruit :', fruit)
print("Good bye!")

#通过序列索引迭代
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print( 'Current fruit :', fruits[index])
print("Good bye!")


#Python 循环嵌套
d={'x':1,'y':2,'z':3}
for key in d:
    print("%s corresponds to %s" % (key,d[key]))

for key,val in d.items():
    print("%s corresponds to %s" % (key,val))

#Python break 语句
#Python continue 语句
#Python pass 语句
#Python pass是空语句，是为了保持程序结构的完整性
for letter in 'Python':
    if letter == 't':
        pass    #去掉则会报错,因为python中空代码块是非法的
    elif letter == 'h':
        print('Current Letter :', letter)
print("Good bye!")

#Python else 语句
# else 中的语句会在循环正常执行完的情况下执行
range(0,10)                                                                     #[0,1,2,3,4,5,6,7,8,9]
range(10)                                                                       #[0,1,2,3,4,5,6,7,8,9]
from math import sqrt 
for num in range(5,0,-1): 
    if sqrt(num)==2:
        print('%s' % num)
        break
else:
    print("Didn't find it")    

##########################################    一些迭代的工具
#1.    并行迭代
names = ['anne','beth','george','damon']
ages = [12,45,32,102]
for i in range(len(names)):
    print('%s : %s'    %   (names[i],ages[i]))

#zip    将两个函数进行并行迭代
for name,age in zip(names,ages):
    print("%s : %s",(name,age))
#可以应付长度不一样的序列，当最短的序列用完时就会停止
zip(xrange(2),xrange(10000000))         #[(0,0),(1,1),(2,2)] 

#2.    编号迭代

# strs= "abcabcabcabcabcabcabcabc"
# for index,str1 in enumerate(strs):
#     if 'a' in str1:
#         strs[index]='[ssss]'
#     index+=1
# print(strs)                     #abcabcabcabcabcabcabcabc


#3.    翻转和排序迭代
#sorted 、 reversed：作用于任何序列或可迭代的对象上，不是原地修改对象    
print(sorted([4,3,6,8,3]))                              #[3, 3, 4, 6, 8]
print(sorted('Hello,world'))                            #[',', 'H', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(reversed('Hello,world'))                          #<reversed object at 0x0215A650>
print("".join(reversed('Hello,world')))                 #dlrow,olleH
print(list(reversed('Hello,world')))                    #['d', 'l', 'r', 'o', 'w', ',', 'o', 'l', 'l', 'e', 'H']




##########################################    列表推导式-轻量级循环
#利用其他列表创建新列表
ls=[x*x for x in range(10)]
print(ls)                                                       #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
ls=[x*x for x in range(10) if x%3==0]                           
print(ls)                                                       #[0, 9, 36, 81]
ls=[(x,y) for x in range(3) for y in range(3)]
print(ls)                                                       #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

#名字首字母相同的男孩女孩
girls=['alice','bernice','clarice']
boys=['chris','arnold','bob']
letters=[b+'+'+g for b in boys for g in girls  if b[0]==g[0]]
print(letters)                                                  #['chris+clarice', 'arnold+alice', 'bob+bernice']
#效率高点的

girls=['alice','bernice','clarice']
boys=['chris','arnold','bob']
letterGirls={}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]        #['chris+clarice', 'arnold+alice', 'bob+bernice']




print(
      '''========================================特殊函数========================================================================''')


#    del删除
x=1
del x                                   #垃圾收集
x={'name':'Alice','age':'20'}
y=x
#x,y绑定在同一个字典                                                                            
del x                                   #删除的只是名称,而不是列表本身的值，python中是没有办法删除值！！！！
print(y)


#    exec            动态的创建代码字符串

#    eval





print(
      '''========================================运算符========================================================================''')

''' 1.算术运算符；    2.比较（关系）运算符；    3.赋值运算符；   4.逻辑运算符；   5.位运算符；   6.成员运算符；  7.身份运算符
    运算符优先级'''
    
##########################################    1.算术运算符
a = 2
b = 3
c = 0
c = a + b
c = a - b
c = a * b
c = a / b
#取模 - 返回除法的余数
c = a % b
#幂 - 返回x的y次幂
c = a**b
#取整除 - 返回商的整数部分
c = a//b 
##########################################    2.比较（关系）运算符 
'''==    等于 - 比较对象是否相等
!=    不等于 - 比较两个对象是否不相等
>    大于 - 返回x是否大于y
<    小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。    (a < b) 返回 true。
>=    大于等于 - 返回x是否大于等于y。
<=    小于等于 - 返回x是否小于等于y。'''

if ( a != b ):
    print ("Line 1 - a is equal to b")
else:
    print ("Line 1 - a is not equal to b")
 
##########################################    3.赋值运算符 
'''
=    简单的赋值运算符    c = a + b 将 a + b 的运算结果赋值为 c
+=    加法赋值运算符    c += a 等效于 c = c + a
-=    减法赋值运算符    c -= a 等效于 c = c - a
*=    乘法赋值运算符    c *= a 等效于 c = c * a
/=    除法赋值运算符    c /= a 等效于 c = c / a
%=    取模赋值运算符    c %= a 等效于 c = c % a
**=    幂赋值运算符    c **= a 等效于 c = c ** a
//=    取整除赋值运算符    c //= a 等效于 c = c // a
''' 

##########################################    4.位运算符  

'''
&     按位与运算符    (a & b) 输出结果 12 ，二进制解释： 0000 1100
|     按位或运算符    (a | b) 输出结果 61 ，二进制解释： 0011 1101
^     按位异或运算符    (a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~     按位取反运算符    (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<    左移动运算符    a << 2 输出结果 240 ，二进制解释： 1111 0000
>>    右移动运算符    a >> 2 输出结果 15 ，二进制解释： 0000 1111
'''


##########################################    5.逻辑运算符 
'''
and    布尔"与" - 如果x为False，x and y返回False，否则它返回y的计算值。    (a and b) 返回 true。
or     布尔"或" - 如果x是True，它返回True，否则它返回y的计算值。    (a or b) 返回 true。
not    布尔"非" - 如果x为True，返回False。如果x为False，它返回True。    not(a and b) 返回 false。
'''
a = 10
b = 20
c = 0
if ( a and b ):
    print("Line 1 - a and b are true")
else:
    print("Line 1 - Either a is not true or b is not true")

if ( a or b ):
    print("Line 2 - Either a is true or b is true or both are true")
else:
    print("Line 2 - Neither a is true nor b is true")


a = 0
if ( a and b ):
    print("Line 3 - a and b are true")
else:
    print("Line 3 - Either a is not true or b is not true")

if ( a or b ):
    print("Line 4 - Either a is true or b is true or both are true")
else:
    print("Line 4 - Neither a is true nor b is true")

if not( a and b ):
    print("Line 5 - Either a is not true or b is  not true or both are not true")
else:
    print("Line 5 - a and b are true")
 
'''--------------------------------------6.成员运算符----------------------------'''
'''
in    如果在指定的序列中找到值返回True，否则返回False。    x 在 y序列中 , 如果x在y序列中返回True。
not in    如果在指定的序列中没有找到值返回True，否则返回False。    x 不在 y序列中 , 如果x不在y序列中返回True。
'''
a = 1
b = 20
list1 = [1, 2, 3, 4, 5 ];

if ( a in list1 ):
    print(" in the given list")
else:
    print("Line 1 - a is not available in the given list")

if ( b not in list1 ):
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")
 
'''--------------------------------------7.身份运算符----------------------------''' 
'''
is                 is是判断两个标识符是不是引用自一个对象    x is y, 如果 id(x) 等于 id(y) , is 返回结果 1
is not             is not是判断两个标识符是不是引用自不同对象    x is not y, 如果 id(x) 不等于 id(y). is not 返回结果 1
'''
a = 20
b = 20
print(id(a))
print(id(b))
if ( a is b ):
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")

if ( id(a) == id(b) ):
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")

b = 30
if ( a is b ):
    print("Line 3 - a and b have same identity")
else:
    print("Line 3 - a and b do not have same identity")

if ( a is not b ):
    print("Line 4 - a and b do not have same identity")
else:
    print("Line 4 - a and b have same identity")
 
'''----------------------运算符优先级----------------------------''' 
'''
以下表格列出了从最高到最低优先级的所有运算符：

运算符    描述
**    指数 (最高优先级)
~ + -    按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //    乘，除，取模和取整除
+ -    加法减法
>> <<    右移，左移运算符
&    位 'AND'
^ |    位运算符
<= < > >=    比较运算符
<> == !=    等于运算符
= %= /= //= -= += *= **=    赋值运算符
is is not    身份运算符
in not in    成员运算符
not or and    逻辑运算符
'''


print(
      '''========================================小demo段========================================================================''')
##########################用python提取url链接中的域名与端口 
import  urllib
proto, rest = urllib.splittype("http://www.baidu.com/11/12.htm")  
host, rest = urllib.splithost(rest)  
print host  
host, port = urllib.splitport(host)  
if port is None:  
    port = 80  
print port  
