#coding=utf-8
'''
Created on 2015年8月21日

@author: Administrator
'''  


'''
###########################################    python中对文件、文件夹（文件操作函数）的操作需要涉及到os模块和shutil模块。

os.getcwd()                       得到当前工作目录，即当前Python脚本工作的目录路径: 
os.listdir()                      返回指定目录下的所有文件和目录名
os.remove()                       函数用来删除一个文件
os.removedirs（r“c：\python”）                     删除多个目录
os.path.isfile()                  检验给出的路径是否是一个文件：
os.path.isdir()                   检验给出的路径是否是一个目录：
os.path.isabs()                   判断是否是绝对路径：
os.path.exists()                  检验给出的路径是否真地存:
os.path.split()                   返回一个路径的目录名和文件名:
    eg os.path.split('/home/swaroop/byte/code/poem.txt') 结果：('/home/swaroop/byte/code', 'poem.txt') 
os.path.splitext()                分离扩展名：
os.path.dirname()                 获取路径名：
os.path.basename()                获取文件名：
os.system()                       运行shell命令: 
os.getenv() 与os.putenv()          读取和设置环境变量:
os.linesep                        给出当前平台使用的行终止符:
    Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
os.name                           指示你正在使用的平台：
             对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
os.rename（old， new）                                                     重命名：
os.makedirs（r“c：\python\test”）            创建多级目录：

os.mkdir（“test”）                                                                创建单个目录：
os.stat（file）                                                                            获取文件属性：
os.chmod（file）                                                                        修改文件权限与时间戳：
os.exit（）                                                                                          终止当前进程：
os.path.getsize（filename）                                  获取文件大小：


###########################################    文件操作：
os.mknod("test.txt")                创建空文件
fp = open("test.txt",w)             直接打开一个文件，如果文件不存在则创建文件

关于open 模式：
    w     以写方式打开，
    a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
    r+     以读写模式打开
    w+     以读写模式打开 (参见 w )
    a+     以读写模式打开 (参见 a )
    rb     以二进制读模式打开
    wb     以二进制写模式打开 (参见 w )
    ab     以二进制追加模式打开 (参见 a )
    rb+    以二进制读写模式打开 (参见 r+ )
    wb+    以二进制读写模式打开 (参见 w+ )
    ab+    以二进制读写模式打开 (参见 a+ )

            第三个参数：控制着文件的缓冲
        0/False    I/O无缓冲（所有读写操作都是直接针对硬盘）
        1/True     I/O有缓冲(使用内存代替硬盘),只有flush或者close时才会更新硬盘上的数据
                                                                    大于1的数字代表缓冲区的大小（字节）,-1(或者任何负数)代表使用默认的缓冲区的大小
 

fp.read([size])                         #size为读取的长度，以byte为单位
fp.readline([size])                     #读一行，如果定义了size，有可能返回的只是一行的一部分
fp.readlines([size])                    #把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。
fp.write(str)                           #把str写到文件中，write()并不会在str后加上一个换行符
fp.writelines(seq)                      #把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。

fp.close()                              #关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。  如果一个文件在关闭后还对其进行操作会产生ValueError
fp.flush()                              #把缓冲区的内容写入硬盘
fp.fileno()                             #返回一个长整型的”文件标签“
fp.isatty()                             #文件是否是一个终端设备文件（unix系统中的）
fp.tell()                               #返回文件操作标记的当前位置，以文件的开头为原点
fp.next()                               #返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
fp.seek(offset[,whence])                #将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。
fp.truncate([size])                     #把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。

 
###########################################    目录操作： 
os.mkdir("file")                       创建目录

shutil.copyfile("oldfile","newfile")   复制文件,    oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile")       复制文件,    oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
shutil.copytree("olddir","newdir")     复制文件夹：   olddir和newdir都只能是目录，且newdir必须不存在
os.rename("oldname","newname")         重命名文件（目录）    文件或目录都是使用这条命令
shutil.move("oldpos","newpos")         移动文件（目录）
os.remove("file")                      删除文件
os.rmdir("dir")                        删除目录,只能删除空目录
shutil.rmtree("dir")                   删除目录,空目录、有内容的目录都可以删
os.chdir("path")                       转换目录,换路径
'''
import os 
#获取当前文件所在路径
print os.getcwd()                           #E:\0.PythonWorkSpace\HelloWorld\src\com\main
print os.getcwdu()                          #E:\0.PythonWorkSpace\HelloWorld\src\com\main
import sys
print (os.path.abspath(sys.argv[0]))        #E:\0.PythonWorkSpace\HelloWorld\src\com\main\CH11.py

 
#截取字符串至项目名：HelloWorld\
thePath = os.getcwdu()
thePath=thePath[:thePath.find("HelloWorld")]
thePath=thePath+"HelloWorld"                               
print thePath                                                   ##E:\0.PythonWorkSpace\HelloWorld


'''获得一个目录中所有文件的列表''' 
for name in os.listdir(thePath+'\Files') :  
    print os.path.join(thePath,name)
    
    
'''
返回一个三元组，
遍历的路径、当前遍历路径下的目录、当前遍历目录下的文件名
thePath=thePath+'Files'
print thePath
for root,dirs,files in os.walk(os.getcwdu()):
    print root                                                           #输出当前的根目录                                                                               
    print dirs                                                          #该根下的子目录，返回为列表    
    print len(files)                                                    #文件的个数                                         
 
    print sum(getsize(join(root,name)) for name in files)               #输出该目录下（不包括目录）文件的total size。
    print [name for name in files]                                      #返回目录下的所有的文件名
    print len(files)                                                    #文件的个数
'''
    
thePath=thePath[:thePath.find("HelloWorld")]+"\\HelloWorld\\Files\\file.txt" 
print thePath                   
#######################################################    [1]、输入
'''
1、read():            读取字节到字符串中，有可选参数size，默认是-1，如果为-1或复数则文件将会被读取到文件末尾。
2、readline():        读取文件的一行，包括行结束符。同read()也有个可选参数size。
3、readlines()：                        读取所有（剩余的）然后将它们作为字符串列表返回，它有个可选参数sizhint代表返回的最大字大小。
'''
f=open(thePath,'r')
print f.read(5)                                                     #Hello
print f.read(3)                                                     #.Ki
print f.read()                                                      #tty.
print f.readline()                                                  #I am Chinese!
                                                                    #my name is BeginMan,
                                                                    #I like coding
f.close()

'''
当使用read()或者readlines()从文件中读取行时，Python并不会删除行结束符，这个操作留给了程序员。
'''
thePath=thePath[:thePath.find("HelloWorld")]+"\\HelloWorld\\Files\\read.txt" 
f=open(thePath,'r')
print f.readlines()                                                 #['Hello.Kitty.\n', 'I am Chinese!\n', 'my name is BeginMan,\n', 'I like coding']
f.seek(0,0)    #[2]                                                 #指向开始处
print f.tell()                                                      #0
print [line.strip() for line in f.readlines()]                     #['Hello.Kitty.', 'I am Chinese!', 'my name is BeginMan,', 'I like coding']
 



#######################################################    [2]、输出
'''
1、write():            把含有文本数据或二进制数据块的字符串写入到文件中去。
2、writelines()：                        针对列表操作，接受一个字符串列表作为参数，将它们写入文件，行结束符并不会被自动加入，如果需要的话必须在调用writelines方法前给每一行结尾加上结束符。
类似的，write()和writelines()也不会自动加入行结束符，应该自己添加。
'''
f=open(thePath,'w')
f.write('Hello.')                                                                          
f.write('Kitty.\n')                                               #已经换行了                                                             
f.writelines('I am Chinese!\n')                                   #已经换行了 
f.writelines(['my name is BeginMan,\nI like coding'])           
f.close()




#######################################################    [3]、文件内移动 
"""
【1】：tell():
tell 方法确认了已经移到当前文件位置
一个文件对象维护它所打开文件的状态。文件对象的 tell 方法告诉你在打开文件中的当前位置。
因为我们还没有对这个文件做任何事，当前位置为 0，它是文件的开始处。
"""
"""
【2】：seek():
文件对象的 seek 方法在打开文件中移动到另一个位置。第二个参数指出第一个参数是什么意思：
0 表示移动到一个绝对位置 （从文件开始算起），
1 表示移到一个相对位置 （从当前位置算起），
还有 2 表示文件末尾
""" 
thePath=thePath[:thePath.find("HelloWorld")]+"\\HelloWorld\\Files\\file.txt" 
f = open(thePath,'rb')
print '11111111'
print f.tell()          #[0]
f.seek(10,1)            
print f.tell()          #10
print f.read(10)        #y.
                        #I am C
print f.read(18)        #hinese!
                        #my name i
print f.tell()          #38

#######################################################    [4]、文件迭代
f = open(thePath,'rb')
for eachline in f:
    print eachline
'''
Hello.Kitty.

I am Chinese!

my name is BeginMan,

I like coding

'''
    
'''
 四、相关属性
file.closed:文件已被关闭，否则为False
file.mode:文件访问模式
file.name:文件名称
'''

fileHandle = open (thePath,'r' ) 
fileList = fileHandle.readlines() 
for fileLine in fileList: 
    print '>>', fileLine 
fileHandle.close()







