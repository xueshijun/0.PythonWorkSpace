#coding=utf-8
'''
Created on 2015年8月21日

@author: Administrator
'''  
#安装MYSQL DB for python
'''
下载 MySQL for Python 
地址：http://sourceforge.net/projects/mysql-python/files/mysql-python/
'''

'''
commit() 提交
rollback() 回滚

cursor用来执行命令的方法:
    callproc(self, procname, args):            用来执行存储过程,接收的参数为存储过程名和参数列表,返回值为受影响的行数
    execute(self, query, args):                执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
    executemany(self, query, args):            执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
    nextset(self):                             移动到下一个结果集

cursor用来接收返回值的方法:
    fetchall(self):                            接收全部的返回结果行.
    fetchmany(self, size=None):                接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
    fetchone(self):                            返回一条结果行.
    scroll(self, value, mode='relative'):      移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,如果 mode='absolute',则表示从结果集的第一行移动value条.

cursor对象特性
    description                                返回描述的序列，只读
    rowcount                                   返回结果中的行数,只读
    arraysize                                  fetchmany中返回的行数,默认为1

                    异常                                                                                                                                          超类
    StandardError                                                          所有异常的泛型基类
        Warning                                StandardError                   非致命错误发生时引发
        Error                                  StandardError                   所有错误条件的泛型超类
            InterfaceError                         Error                           关于接口而非数据库的错误
            DatabaseError                          Error                           与数据库相关的错误研发
                DataError                              DataBaseError                   与数据相关的异常,比如值超出范围
                OperationalError                       DataBaseError                   数据库内部操作错误
                IntegrityError                         DataBaseError                   关系完整性受到影响,比如键检查失败
                InternalError                          DataBaseError                   数据库内部错误，比如非法游标
                ProgrammingError                       DataBaseError                   用户编程出错,比如不存在该表
                NotSupportedError                      DataBaseError                   请求不支持的特性,如回滚
'''
########################################    实例1、取得MYSQL版本
import MySQLdb as mdb
con = None
try:
    #连接mysql的方法：connect('ip','user','password','dbname')
    #charset是要跟你数据库的编码一样，如果是数据库是gb2312 ,则写charset='gb2312' 
    con=mdb.connect(host='127.0.0.1',user='root',passwd='pass',db='test',port=3306,charset='utf8') 

    cur = con.cursor()                                                                      #所有的查询，都在连接con的一个模块cursor上面运行的
    cur.execute("SELECT VERSION()")                                                         #执行一个查询
    
    data = cur.fetchone()                                                                   #取得上个查询的结果，是单个结果
    print "Database version : %s " % data

except mdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1]) 
finally:
    if cur:
        cur.close()
    if con: 
        con.close()


########################################    实例2、创建一个表并且插入数据
#import MySQLdb as mdb
#import sys
#将con设定为全局连接con = None
try:
    con=mdb.connect(host='127.0.0.1',user='root',passwd='pass',db='test',port=3306)
    with con:
        cur = con.cursor()                                                                  #获取连接的cursor，只有获取了cursor，我们才能进行各种操作
        cur.execute("CREATE TABLE IF NOT EXISTS \
                        Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")      #创建一个数据表 writers(id,name)
        #以下插入了5条数据
        cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
        
except mdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1]) 
finally:
    if con:
        con.close()                                                                         #无论如何，连接记得关闭

########################################    实例3、python使用slect获取mysql的数据并遍历
# import MySQLdb as mdb
# import sys
try:
    con=mdb.connect(host='127.0.0.1',user='root',passwd='pass',db='test',port=3306)
    with con:
        cur = con.cursor()                                                                  #仍然是，第一步要获取连接的cursor对象，用于执行查询
        cur.execute("SELECT * FROM Writers")                                                #类似于其他语言的query函数，execute是python中的执行查询函数
        #我们使用了fetchall这个方法.这样,cds里保存的将会是查询返回的全部结果.每条结果都是一个tuple类型的数据,这些tuple组成了一个tuple 
        rows = cur.fetchall()                                                               #使用fetchall函数，将结果集（多维元组）存入rows里面
        #因为是tuple,所以可以这样使用结果集
        print rows                                                                          #((1L, 'Jack London'), (2L, 'Honore de Balzac'), (3L, 'Lion Feuchtwanger'), (4L, 'Guy de Maupasant'), (5L, 'Truman Capote'), (6L, 'Jack London'), (7L, 'Honore de Balzac'), (8L, 'Lion Feuchtwanger'), (9L, 'Emile Zola'), (10L, 'Truman Capote'), (11L, 'Jack London'), (12L, 'Honore de Balzac'), (13L, 'Lion Feuchtwanger'), (14L, 'Emile Zola'), (15L, 'Truman Capote'), (16L, 'Jack London'), (17L, 'Honore de Balzac'), (18L, 'Lion Feuchtwanger'), (19L, 'Emile Zola'), (20L, 'Truman Capote'), (21L, 'Jack London'), (22L, 'Honore de Balzac'), (23L, 'Lion Feuchtwanger'), (24L, 'Emile Zola'), (25L, 'Truman Capote'), (26L, 'Jack London'), (27L, 'Honore de Balzac'), (28L, 'Lion Feuchtwanger'), (29L, 'Emile Zola'), (30L, 'Truman Capote'), (31L, 'Jack London'), (32L, 'Honore de Balzac'), (33L, 'Lion Feuchtwanger'), (34L, 'Emile Zola'), (35L, 'Truman Capote'), (36L, 'Jack London'), (37L, 'Honore de Balzac'), (38L, 'Lion Feuchtwanger'), (39L, 'Emile Zola'), (40L, 'Truman Capote'), (41L, 'Jack London'), (42L, 'Honore de Balzac'), (43L, 'Lion Feuchtwanger'), (44L, 'Emile Zola'), (45L, 'Truman Capote'), (46L, 'Jack London'), (47L, 'Honore de Balzac'), (48L, 'Lion Feuchtwanger'), (49L, 'Emile Zola'), (50L, 'Truman Capote'), (51L, 'Jack London'), (52L, 'Honore de Balzac'), (53L, 'Lion Feuchtwanger'), (54L, 'Emile Zola'), (55L, 'Truman Capote'), (56L, 'Jack London'), (57L, 'Honore de Balzac'), (58L, 'Lion Feuchtwanger'), (59L, 'Emile Zola'), (60L, 'Truman Capote'), (61L, 'Jack London'), (62L, 'Honore de Balzac'), (63L, 'Lion Feuchtwanger'), (64L, 'Emile Zola'), (65L, 'Truman Capote'), (66L, 'Jack London'), (67L, 'Honore de Balzac'), (68L, 'Lion Feuchtwanger'), (69L, 'Emile Zola'), (70L, 'Truman Capote'), (71L, 'Jack London'), (72L, 'Honore de Balzac'), (73L, 'Lion Feuchtwanger'), (74L, 'Emile Zola'), (75L, 'Truman Capote'))
#       print rows[0][3] #或者直接显示出来,看看结果集的真实样子
        for row in rows:                                                                    #依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
            print row
except mdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1]) 
finally:
    if con:
        con.close()

########################################    实例4、使用字典cursor取得结果集（可以使用表字段名字访问值）
# import MySQLdb as mdb
# import sys 
try:
    con=mdb.connect(host='127.0.0.1',user='root',passwd='pass',db='test',port=3306)
    with con: 
        cur = con.cursor(mdb.cursors.DictCursor)                                            #获取连接上的字典cursor，注意获取的方法，每一个cursor其实都是cursor的子类
        cur.execute("SELECT * FROM Writers")
        rows = cur.fetchall()
        for row in rows: 
            print "%s----%s" % (row["Id"], row["Name"])                                     #这里，可以使用键值对的方法，由键名字来获取数据
except mdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1]) 
finally:
    if con: 
        con.close()

########################################    实例5、获取单个表的字段名和信息的方法
# import MySQLdb as mdb
# import sys 
try:
    con=mdb.connect(host='127.0.0.1',user='root',passwd='pass',db='test',port=3306)
    with con:  
        cur = con.cursor()                                                                     #获取普通的查询cursor
        cur.execute("SELECT * FROM Writers")
        rows = cur.fetchall()
        desc = cur.description                                                                 #获取连接对象的描述信息
        print 'cur.description:',desc                                                       #cur.description: (('Id', 3, 2, 11, 11, 0, 0), ('Name', 253, 17, 25, 25, 0, 1))
        print "%s %3s" % (desc[0][0], desc[1][0])                                           #Id Name
        print cur.rowcount                                                                  #5
except mdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1]) 
finally:
    if con: 
        con.close() 
########################################    实例6、使用Prepared statements执行查询（更安全方便）
# import MySQLdb as mdb
# import sys
try:
    con=mdb.connect(host='127.0.0.1',user='root',passwd='pass',db='test',port=3306)
    with con: 
        cur = con.cursor() 
        cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s", ("Guy de Maupasant", "4"))
        print "Number of rows updated: %d" % cur.rowcount                                       #使用cur.rowcount获取影响了多少行
except mdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1]) 
finally:
    if con: 
        con.close() 
        
########################################    实例7、   批量插入数据，更新数据的
try:
    con=mdb.connect(host='127.0.0.1',user='root',passwd='pass',port=3306)
    with con: 
        cur = con.cursor()  
        cur.execute('create database if not exists python')
        con.select_db('python')
        cur.execute('create table IF NOT EXISTS test(id int,info varchar(20))')
        value=[1,'hi rollen']
        cur.execute('insert into test values(%s,%s)',value)
        
        values=[]
        for i in range(20):
            values.append((i,'hi rollen'+str(i)))
        cur.executemany('insert into test values(%s,%s)',values)
        
        cur.execute('update test set info="I am rollen" where id=3')
        con.commit()
        
        cur.execute("SELECT * FROM Writers")
        rows = cur.fetchall()
        for row in rows: 
            print "%s----%s" % (row["Id"], row["Name"])     
        cur.close()
except mdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1]) 
finally:
    if con: 
        con.close() 
        
