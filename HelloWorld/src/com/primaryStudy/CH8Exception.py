#coding=utf-8
'''
Created on 2015年8月12日

@author: Administrator
'''
'''
raise Exception()
raise Exception('自定义异常')
'''
import exceptions
#列出模块内容
print  dir(exceptions)
#自定义异常
class MyException(Exception):
    pass

#########################    捕捉异常
class MuffledCalculator():
    def calculate1(self,expression):
        try:
            print eval(expression)
        except ZeroDivisionError:
            print("分母出现0")
        except TypeError:
            print("除数、被除数类型不对")
        except NameError:
            print("存在未定义的参数")
        else:
            print("总支出错了")
    #用一个块捕捉多个异常
    def calculate2(self,expression):
        try:
            print eval(expression)
        except (ZeroDivisionError,TypeError,NameError):
            print("存在bug")
        else:
            print("总支出错了")
    def calculate3(self,expression):
        try:
            print eval(expression)
        except (ZeroDivisionError,TypeError,NameError) as e:
            print(e)
        else:
            print("总支出错了")
    def calculate4(self):
        x=None
        try:
            x=2/'2'
            print x
        except (ZeroDivisionError,TypeError,NameError) as e:
            print(e)
        finally:
            print("清理出错的变量")
            del x
            
muff=MuffledCalculator()
muff.calculate1('1/0')                   #分母出现0
muff.calculate1("2/'s'")                 #除数、被除数类型不对
muff.calculate1("2/s")                   #存在未定义的参数

muff.calculate2("2/s")                   #存在bug

muff.calculate3("2/s")                   #name 's' is not defined

muff.calculate4()                      
                                        #unsupported operand type(s) for /: 'int' and 'str' 
                                        #理出错的变量'''



