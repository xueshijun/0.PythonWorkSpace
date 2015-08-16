#coding=utf-8
'''
Created on 2015年7月20日

@author: Administrator
'''




#################################################    多态
'''    方法与函数
    绑定到对象特性上面的函数称为方法
'''
#    从序列中随机选出元素,不关心是什么类型，只关心变量x中字符e出现多少次
from random import choice
x=choice(['Hello','world',[1,2,'3','e','e',4]])
print(x.count('e'))                                        #2

#    多态的多种形式
1+2
'fish' + 'license'
def add_obj(x,y):
    return x+y

#    
def length_msg(x):
    print('the length of %s is %s' % (repr(x),len(x)))
length_msg('Fnord')                                            #the length of 'Fnord' is 5
length_msg([1,2,3,4])                                          #the length of [1, 2, 3, 4] is 4     

#################################################    类
class Person:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print("Hello,world!I'm %s" % (self.name))
foo=Person()
bar=Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()                                             #Hello,world!I'm Luke Skywalker
bar.greet()                                             #Hello,world!I'm Anakin Skywalker

print(bar.name)                                         #Anakin Skywalker                                       #Hello,world!I'm Anakin Skywalker
bar.name='Yoda'
bar.greet()                                             #Hello,world!I'm Yoda  

#    方法/绑定方法
#将它们的第一个参数绑定到所属的实例上,这个参数可以不必提供
class BirdClass:
    song='HellKitty!'
    def sing(self):                              ####方法#
        print('I am singing %s' % (self.song))

    #为了让方法或者特性变为私有,只要在它的名字前面加上双下划线
    def __fly(self):
        print('Bet you can\'t see me...')
    
    def fly(self):
        self.__fly()
def fun_demo():
    print('I don\'t....')
bird=BirdClass()
bird.sing()                              #I am singing HellKitty!
bird.sing=fun_demo
bird.sing()                              #I don't....                                
'''
变量birdsong引用绑定方法bird.sing上,即意味着这还是对self参数 的访问（它仍旧绑定到类的相同的实例上）
'''
birdsong=bird.sing
birdsong()                               #I don't....                                

#bird.__fly()                            #不可访问
bird.fly()                               #Bet you can't see me...

#在类的内部定义中,所有以双下划线开始的名字都被翻译成前面加上单下划线和类名的形式
#BirdClass._BirdClass__fly()             #unbound method __fly()
bird._BirdClass__fly()                   #Bet you can't see me...
#但是前面有双下划线的名字都不会被带星号的import语句导入


#################################################    类的命名空间

#类作用域内的变量可以被所有实例访问
class MemberCounter:
    counter=0
    def init(self):
        MemberCounter.counter+=1
m1=MemberCounter()
m1.init()
print(MemberCounter.counter)                    #1
print(m1.counter)                               #1
m2=MemberCounter()
m2.init()
print(MemberCounter.counter)                    #2
print(m2.counter)                               #2
#在实例中重绑定特性
m1.counter='Two'
print(m1.counter)                               #Two
print(m2.counter)                               #2

#################################################    指定超类
class Filter:
    def init(self):
        self.blockded=[]
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blockded]

class SPAMFilter(Filter):
    #重写了超类Filter的init定义
    def init(self):
        self.blockded=['SPAM']
f=SPAMFilter()
f.init()
print f.filter(['SPAM','SPAM','eggs','SPAM','dogs','cats']) #['eggs', 'dogs', 'cats']

#查看一个类是否是另一个的子类
print(issubclass(SPAMFilter, Filter))#true
#查看已知类的基类
print(SPAMFilter.__bases__)                     #(<class __main__.Filter at 0x0252BF48>,)
print(Filter.__bases__)                         #()
#查看对象是否是一个类的实例
print(isinstance(f,SPAMFilter))                 #True
print(isinstance(f,Filter))                     #True
#查看对象属于哪个类
print(f.__class__)                              #__main__.SPAMFilter



#多继承
'''
如果一个方法从多个超类继承，需要注意超类的顺序：
先继承的类中的方法会重写后继成的类中的方法(先继承的生效)
'''
class Calculator:
    def calculate(self,expression):
        self.value=eval(expression)
class Talker:
    def talk(self):
        print("Hi,my value is %s" % (self.value))
class TalkingCalculator(Calculator,Talker):
    pass
tc=TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()                                       #Hi,my value is 7
#判断对象是否包含方法
print(hasattr(tc, 'talk'))                      #True
#判断某特性是否可以调用
print(callable(getattr(tc,'talk',None)))        #True
#python 3.x换成
print(hasattr(tc, '__call__'))                  #False
setattr(tc, 'name', 'Mr.Gumy')
print(tc.name)                                  #Mr.Gumy
