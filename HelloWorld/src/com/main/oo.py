#coding=utf-8
class Hello:
    #构造方法
    def __init__(self,name):
        self._name=name
        
    
    def sayHello(self):
        print("say Hello {0}".format(self._name))

#h=Hello()
h=Hello("张三")
h.sayHello()

#继承
class Hi(Hello):
    def __init__(self,name):
        Hello.__init__(self, name)
    def sayHi(self):
        print("Hi {0}".format(self._name))
        
h1=Hi("Python")
h1.sayHi()