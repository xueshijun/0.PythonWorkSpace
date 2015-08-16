#coding=utf-8
'''
Created on 2015年7月17日

@author: Administrator
'''

if __name__ == '__main__':
    pass


def fibs(num):
    result=[0,1]
    for i in range(num-2):
        print(i)    
        result.append(result[-2]+result[-1])
    return result

print(fibs(4))                                          #[0, 1, 1, 2]



'''
n和names两个变量同时引用一个列表
'''
def change(n):
    n[0]='Mr.Gumby'
names=['Mrs.Entity','Mrs.Thing']            

'''
当在序列中做切片的时候,返回的切片总是一个副本
'''
n=names
print(n==names)                 #True
print(n is names)               #True
change(names)
print(names)                    #['Mr.Gumby', 'Mrs.Thing']


names=['Mrs.Entity','Mrs.Thing']
n=names[:]
print(n==names)                 #True
print(n is names)               #False
change(names[:])                
print(names)                    #['Mrs.Entity','Mrs.Thing']





##########################################################################################################################################
def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
        
def lookup(data,label,name):
    return data[label].get(name)
    
def store(data,full_name):
    names=full_name.split()
    if len(names)==2: 
        names.insert(1,'')
    labels=['first','middle','last']
    for label,name in zip(labels,names):
        people=lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name]=[full_name]

storage={}
init(storage)
store(storage,'Magnus Lie Hetland')
print lookup(storage, 'middle','Lie')
store(storage,'Robin Hood')
print lookup(storage, 'first','Robin')


#                改变参数,将值放在列表
def inc_funtion(x):
    x[0]=x[0]+1
foo=[10]
inc_funtion(foo)
print(foo)                          #[11]

def inc_funtion_2(x):
    x+=1
foo=10
inc_funtion_2(foo)
print(foo)                          #10



#    位置参数
def hello(greeting,name):
    print('%s,%s' % (greeting,name))
#顺序没有影响了            
hello('Hello','world')     #Hello,world
hello('world','Hello')     #world,Hello
#    关键字参数
hello(greeting='Hello',name='world')     #Hello,world
hello(name='world',greeting='Hello')     #Hello,world  
  
#    提供默认值
def hello_1(greeting='Hello',name='world'):
    print('%s,%s' % (greeting,name))
    
hello_1()                                #Hello,world 
hello_1('Greeting')                      #Greeting,world
hello_1('Greeting','universe')           #Greeting,universe  
hello_1(name='Gumby')                    #Hello,Gumby

def hello_2(name,greeting='Hello',punctuation='!'): 
    print('%s,%s%s' % (greeting,name,punctuation)) 

hello_2('Mars')                         #Hello,Mars!
hello_2('Mars','Howdy')                 #Howdy,Mars!
hello_2('Mars','Howdy','...')           #Howdy,Mars...


#    收集位置参数
def print_params(*params):
    print(params)
print_params('testing')                 #('testing',)    
print_params(1,2,3,4)                   #(1, 2, 3, 4)

def print_params_1(title,*params):
    print('%s %s' % (title,params)) 

print_params_1('params:',1,2,3,4)       #params: (1, 2, 3, 4)
print_params_1('params:')               #params: ()

#    收集关键字参数
'''
print_params_1('Hmm...:',something=42)  #params: ()
'''
def print_params_2(**params):
    print(params)
print_params_2(x=1,y=2,z=3)             #{'y': 2, 'x': 1, 'z': 3}

def print_params_3(x,y,z=3,*pospar,**keypar):
    print(z,y,z)
    print(pospar)
    print(keypar)

print_params_3(1,2,3,5,6,7,foo=1,bar=2)
'''
1,2,3
(5,6,7)
{'foo':1,'bar':2}
'''
print_params_3(1,2)
'''
1,2,3
()
{}
'''
def foo(x,y,z,m=0,n=0):
    print (x,y,z,m,n)
def call_foo(*args,**kwds):
    call_foo(*args,**kwds)


#函数内部访问全局变量
'''
如果局部变量或参数的名字和想要访问的全局变量名相同的话,就不能直接访问了
全局变量会被局部遍历屏蔽。如果的确需要的话，可使用globals
'''
def combine(param):print param+external
external='berry'
combine('Shrub')                            #Shrubberry







def combine_1(parameter): print(parameter+globals()['parameter'])
parameter='berry'
combine_1('Shrub')                          #Shrubberry


#重绑定全局变量
gb=6
def change_global():
    global gb
    gb=gb+1
    
change_global()
print(gb)                                   #7


#函数嵌套
'''
函数本身被返回了，却没有被调用
返回的函数还可以访问它的定义所在的作用域
每次调用外层函数,它内部的函数都会被重新绑定,factor变量每次都有一个新的值.

类似multiplyByFactor函数存储子封闭作用域的行为叫做闭包
'''
def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor

double=multiplier(2)
print(double(3))                                 #6

triple=multiplier(3)
print(triple(3))                                 #9

print(multiplier(5)(4))                          #20






#############################################    递归

#    阶乘
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
#    幂
def power(x,n):
    if n==1:
        return 1
    else :
        return x * power(x,n-1)

#    二元查找
# def search_binary(sequence,number,lower=0,higher=None):
#     if higher is None:higher=len(sequence)-1
#     if lower==higher:
#         assert number==sequence[higher]
#         return higher
#     else:
#         middle =(lower+higher)//2
#         if number>sequence[middle]:
#             return search_binary(sequence,middle+1,higher) 
#         else :
#             return search_binary(sequence,lower,middle) 
#         
# seq=[34,67,8,123,4,100,95]
# seq.sort()
# print(seq)
# print search_binary(seq,34)


