#coding=utf-8
'''
Created on 2015年8月12日

@author: Administrator
'''
from _pyio import __metaclass__
import new


'''

'''
########################    构造函数
class FooBar:
    def __init__(self):
        self.somevar=42
fooBar=FooBar()
print(fooBar.somevar)               #42
########################    析构函数
#在对象就要被垃圾回收之前调用，但发生的调用的具体时间是不可知的


class Animal:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print("I'm eating")
            self.hungry=False
        else:
            print("No.Thanks!")
    def sayHello(self):
        print("Hello,I'm animal")

#不重写构造函数
#重写方法
class Dog(Animal):
    def sing(self):
        print("汪汪")
dog=Dog()
dog.eat()                                               #I'm eating
dog.eat()                                               #No.Thanks!

class Bird(Animal):
    def __init__(self):
        self.sound="Squawk"
    def sing(self):
        print(self.sound) 
bird=Bird()
#不能访问eat方法，因为构造函数已重写,不存在hungry变量了
#bird.eat()                                             #Bird instance has no attribute 'hungry'
bird.sing()                                             #Squawk

class Cat(Animal):
    def __init__(self):
        #调用未绑定的超类构造方法
        Animal.__init__(self)
        self.sound="喵喵"
    def sing(self):
        print(self.sound) 
cat=Cat()
cat.eat()                                               #I'm eating
cat.eat()                                               #No.Thanks!
cat.sing()                                              #喵喵


########################    
########################    super函数
#针对python3.0，super函数只在新式类中起作用
'''即使类已经继承多个超类，它也只需要使用一次super函数
'''
class Sheep(Animal):
    def __init__(self):
        super(Sheep,self).__init__()
        self.sound="咩咩"
    def sing(self):
        print(self.sound)
sheep=Sheep()
sheep.eat()                                             #I'm eating
sheep.eat()                                             #No.Thanks!
sheep.sing()                                            #咩咩


###################    成员访问
'''
序列和映射是对象的集合。
如果对象是不可变的，就需要使用2个魔法方法；
如果对象是可变的，就需要使用4个魔法方法。
__len__(self)                                    返回集合中所含项目的数量。
__getitem__(self,key)                            返回与所给键对应的值
——setitem__(self,key,value)
__delitem__(self,key)
'''

def checkIndex(key):
    if not isinstance(key,(int,long)):raise TypeError
    if key<0:raise IndexError
#该类没有__len__方法,因为它是无限长的
#没有__del__方法,因为希望不允许删除元素
class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        self.start=start
        self.step=step
        self.changed={}
    def __getitem__(self,key):
        checkIndex(key)
        try:return self.changed[key]    #修改了吗
        except KeyError:
            return self.start+key*self.step
    def __setitem__(self,key,value):
        checkIndex(key)
        self.changed[key]=value
seq=ArithmeticSequence(1,2)
print(seq[4])                   #9
seq[4]=2
print(seq[4])                   #2
print(seq[5])                   #11

#继承list
class MyList(list):
    def __init__(self,*arg):
        super(MyList,self).__init__(*arg)
        self.counter=0
    '''重写__getitem__并非获取用户访问的万全之策，因为还有其他访问方法，如pop '''
    def __get__(self,index):
        self.counter+=1
        return super(MyList,self).__getitem__(index)

##########################################  属性
__metaclass__=type
class Rectangle:
    def __init__(self):
        self.width=0;
        self.height=0
    def setSize(self,size):
        self.height,self.width=size
    def getSize(self):
        return self.width,self.height
    #property(fget=None, fset=None, fdel=None, doc=None) -> property 
    size=property(getSize,setSize)
rect=Rectangle()
rect.height=150
rect.width=100
print(rect.size)                                        #(100, 150)
rect.size=100,150
print(rect.height)                                      #100



######################################    静态方法与类成员方法
__metaclass__=type
class MyClass:
    @staticmethod
    def smeth():
        print("This is a static method")
    @classmethod
    def cmeth(cls):
        print("This is a class method of %s" % cls)

MyClass.smeth()                                         #This is a static method
myclass=MyClass()
myclass.cmeth()                                         #This is a class method of <class '__main__.MyClass'>
myclass.smeth()                                         #This is a static method



##########################    拦截对象的所有特性访问
'''
__getattribute__(self,name)                   (只支持新式类)当特性name被访问时自动被调用
____getattr__(self,name)                      当特性被访问且对象没有相应的特性时被自动调用
____setattr__(self,name,value)                当试图给特性name赋值时会被自动调用
____delattr__(self,name)                      当试图删除特性name时被自动调用
'''
class Rectangles:
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self,name,value):
        if name=='size':
            self.width,self.height=value
        else:
            self.__dict__[name]=value
    def __getattr__(self,name):
        if name=='size':
            return self.width,self.height
        else:
            raise AttributeError
'''
__getattribute__拦截所有特性的访问,也拦截对__dict__的访问！
访问__getattribute__中与Self相关的特性时，使用超类的__getattribute__(使用super函数)是唯一安全的途径
'''
rects=Rectangles()
rects.size=100,130
rects.othersize=200,230
print(rects.size)                                   #(100, 130)
print(rects.othersize)                              #(200, 230)


#########################    迭代器
#一个实现了next方法的对象则是迭代器
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs=Fibs()
for f in fibs:
    if(f>1000):
        print f                                     #1597
        break

#内建函数iter可以从可迭代的对象中获得迭代器
it=iter([1,2,3])
print(it.next())                                    #1
print(it.next())                                    #2
print(it.next())                                    #3

#从迭代器获得序列
class TestIterator:
    value=0
    def next(self):
        self.value+=1
        if(self.value>10):raise StopIteration
        return self.value
    def __iter__(self):
        return self
it=TestIterator()
print(list(it))                                     #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


############################################    生成器
############################################    1.创建生成器
nested=[[1],[2,3],[4,5,6]]
def flatten(nested):
    for sublist in nested:
        for elem in sublist:
            #yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
            yield elem
'''
1
2
3
4
5
6
'''
for num in flatten(nested):
    print(num)
print(list(flatten(nested)))                #[1, 2, 3, 4, 5, 6]

g=((i+2)**2 for i in range(2,27))
print(g.next())                             #16
print(sum(i**2 for i in range(10)))         #285



############################################    2.递归生成器
#解决不知道几层嵌套
def flatten2(nested):
    try:
        #不要迭代类似字符串的对象
        try:nested+''
        except TypeError:pass
        else: raise TypeError
            
        for sublist in nested:
            for elem in flatten2(sublist):
                yield elem
    except TypeError:
        yield nested

print(list(flatten2([1,2,[3,4],[5,[6],[7,8]]])))                #[1, 2, 3, 4, 5, 6, 7, 8]

print(list(flatten2(['foo',['bar',['baz']]])))                  #['foo', 'bar', 'baz']


'''
生成器由两部分组成：生成器的函数和生成器的迭代器
生成器的函数是def语句定义的,包含yield的部分
生成器的迭代器是这个函数返回的部分
'''


############################################    3.通用生成器
def simple_generator():
    yield 1
simple_generator()

############################################    4.生成器方法
'''
生成器方法生成器和外部世界进行交流的渠道：
1)外部作用域访问生成器的send方法,参数则是要发送的"消息"
2)在内部则挂起生成器,yield现在作为表达式而不是语句使用。
即当生成器重新被使用的时候,yield方法返回一个值,也就是外部通过send方法发送的值
'''
def repeater(value):
    while True: 
        new =(yield value)
        if new is not None:value=new
rep=repeater(42)
print(rep.next())                                   #42
print(rep.send('Hello,World!'))                     #Hello,World!

############################################    5.模拟生成器方法


