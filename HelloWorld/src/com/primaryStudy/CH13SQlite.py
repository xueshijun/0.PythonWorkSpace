#coding=gb2312
#Author : Xueshijun
#MailTo : xueshijun_2010@163.com    / 324858038@qq.com
#QQ     : 324858038
#Blog   :http://blog.csdn.net/xueshijun666
#Created on 2015年8月27日
#Version: 1.0


##################################################################
########################################    SQlite和PySQlite
##################################################################

import sqlite3
import os  
'''SQLite数据库是一款非常小巧的嵌入式开源数据库软件，也就是说
         没有独立的维护进程，所有的维护都来自于程序本身。
        在python中，使用sqlite3创建数据库的连接，当我们指定的数据库文件不存在的时候，连接对象会自动创建数据库文件；如果数据库文件已经存在，则连接对象不会再创建数据库文件，而是直接打开该数据库文件。
        连接对象可以是硬盘上面的数据库文件，也可以是建立在内存中的，在内存中的数据库 执行完任何操作后，都不需要提交事务的(commit)

                创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
                创建在内存上面： conn = sqlite3.connect('"memory:')


    conn = sqlite3.connect('c:\\test\\hongten.db')
             其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：
                commit()            --事务提交
                rollback()          --事务回滚
                close()             --关闭一个数据库链接
                cursor()            --创建一个游标

    cu = conn.cursor()，这样我们就创建了一个游标对象：cu
    
            在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
            对于游标对象cu，具有以下具体操作： 
        execute()           --执行一条sql语句
        executemany()       --执行多条sql语句
        close()             --游标关闭
        fetchone()          --从结果中取出一条记录
        fetchmany()         --从结果中取出多条记录
        fetchall()          --从结果中取出所有记录
        scroll()            --游标滚动

'''

#global var
#数据库文件绝句路径
DB_FILE_PATH = ''
#表名称
TABLE_NAME = ''
#是否打印sql
SHOW_SQL = True

'''获取到数据库的连接对象，参数为数据库文件的绝对路径.  如果传递的参数是存在，并且是文件，那么就返回硬盘上面改,路径下的数据库文件的连接对象；否则，返回内存中的数据接 连接对象'''
def get_conn(path):
    if os.path.exists(path) and os.path.isfile(path):
        print('硬盘上面:[{}]'.format(path))
        return sqlite3.connect(path)
    else:
        print('内存上面:[:memory:]')
        return sqlite3.connect(':memory:')

'''该方法是获取数据库的游标对象，参数为数据库的连接对象。  如果数据库的连接对象不为None，则返回数据库连接对象所创 建的游标对象；否则返回一个游标对象，该对象是内存中数据库连接对象所创建的游标对象'''
def get_cursor(conn):
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()
    
'''关闭数据库游标对象和数据库连接对象'''
def close_all(conn, cur):
    try:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close() 
    except conn.Error,e: print "Mysql Error %s" % (e) 
    finally: pass
            
####################################    创建|删除表操作     START
'''创建数据库表：student'''
def drop_table(conn, table): 
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        if SHOW_SQL: print('执行sql:[{}]'.format(sql))
        cur = get_cursor(conn)
        cur.execute(sql)
        conn.commit()
        print('删除数据库表[{}]成功!'.format(table))
        close_all(conn, cur)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
'''创建数据库表：student'''
def create_table(conn, sql):
    if sql is not None and sql != '':
        cur = get_cursor(conn)
        if SHOW_SQL: print('执行sql:[{}]'.format(sql))
        cur.execute(sql)
        conn.commit()
        print('创建数据库表[student]成功!')
        close_all(conn, cur)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
 


####################################    数据库操作CRUD     START
'''插入数据'''
def save(conn, sql, datas):
    if sql is not None and sql != '':
        if datas is not None:
            cur = get_cursor(conn)
            for data in datas:
                if SHOW_SQL: print('执行sql:[{}],参数:[{}]'.format(sql, data))
                cur.execute(sql, data)
                conn.commit()
            close_all(conn, cur)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
'''查询所有数据'''
def fetchall(conn, sql): 
    if sql is not None and sql != '':
        cur = get_cursor(conn)
        if SHOW_SQL: print('执行sql:[{}]'.format(sql))                                    #[SELECT * FROM student]
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
#         if len(rows) > 0:
#             for e in range(len(rows)):
#                 print(rows[e])
    else:
        print('the [{}] is empty or equal None!'.format(sql)) 
'''查询一条数据'''
def fetchone(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            cur = get_cursor(conn)
            if SHOW_SQL: print('执行sql:[{}],参数:[{}]'.format(sql, data))                 #[SELECT * FROM student WHERE ID = ? ],参数:[(1)]
#             cur.execute(sql, d)
#             rows = cur.fetchall()
#             if len(rows) > 0:
#                 for e in range(len(rows)):
#                     print(rows[e])
            cur.execute(sql, data)
            row=cur.fetchone()
            print(row)
        else:
            print('the [{}] equal None!'.format(data))
    else:
        print('the [{}] is empty or equal None!'.format(sql))
        
'''更新数据'''
def update(conn, sql, datas): 
    if sql is not None and sql != '':
        if datas is not None:
            cur = get_cursor(conn)
            for data in datas:
                if SHOW_SQL: print('执行sql:[{}],参数:[{}]'.format(sql, data))                                  #[UPDATE student SET name = ? WHERE ID = ? ],参数:[('HongtenAA', 1)]
                cur.execute(sql, data)
                conn.commit()
            close_all(conn, cur)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
        
'''删除数据'''
def delete(conn, sql, datas):
    if sql is not None and sql != '':
        if datas is not None:
            cur = get_cursor(conn)
            for data in datas:
                if SHOW_SQL: print('执行sql:[{}],参数:[{}]'.format(sql, data))                      #[DELETE FROM student WHERE NAME = ? AND ID = ? ],参数:[('HongtenAA', 1)] 
                cur.execute(sql, data)
                conn.commit()
            close_all(conn, cur)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

 
####################################    测试操作     START
'''删除数据库表测试'''
def drop_table_test():
    print('删除数据库表测试...')
    conn = get_conn(DB_FILE_PATH)
    drop_table(conn, TABLE_NAME)
'''创建数据库表测试'''
def create_table_test(): 
    print('创建数据库表测试...')
    create_table_sql = '''CREATE TABLE `student` (
                          `id` int(11) NOT NULL,
                          `name` varchar(20) NOT NULL,
                          `gender` varchar(4) DEFAULT NULL,
                          `age` int(11) DEFAULT NULL,
                          `address` varchar(200) DEFAULT NULL,
                          `phone` varchar(20) DEFAULT NULL,
                           PRIMARY KEY (`id`)
                        )'''
    conn = get_conn(DB_FILE_PATH)
    create_table(conn, create_table_sql)
'''保存数据测试...'''
def save_test(): 
    print('保存数据测试...')
    save_sql = '''INSERT INTO student values (?, ?, ?, ?, ?, ?)'''
    data = [(1, 'Hongten', u'男', 20, u'广东省广州市', '13423****62'),
            (2, 'Tom', u'男', 22, u'美国旧金山', '15423****63'),
            (3, 'Jake', u'女', 18, u'广东省广州市', '18823****87'),
            (4, 'Cate', u'女', 21, u'广东省广州市', '14323****32')]
    conn = get_conn(DB_FILE_PATH)
    save(conn, save_sql, data)
'''查询所有数据...'''
def fetchall_test(): 
    print('查询所有数据...')
    fetchall_sql = '''SELECT * FROM student'''
    conn = get_conn(DB_FILE_PATH)
    fetchall(conn, fetchall_sql)
'''查询一条数据...'''
def fetchone_test(): 
    print('查询一条数据...')
    fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
    data = [(1)]
    conn = get_conn(DB_FILE_PATH)
    fetchone(conn, fetchone_sql, data)
'''更新数据...'''
def update_test(): 
    print('更新数据...')
    update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenBB', 2),
            ('HongtenCC', 3),
            ('HongtenDD', 4)]
    conn = get_conn(DB_FILE_PATH)
    update(conn, update_sql, data)
'''删除数据...'''
def delete_test(): 
    print('删除数据...')
    delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenCC', 3)]
    conn = get_conn(DB_FILE_PATH)
    delete(conn, delete_sql, data)

###############################################################
####            测试操作     END
###############################################################

'''初始化方法'''
def init():
    #数据库文件绝句路径
    global DB_FILE_PATH
    DB_FILE_PATH = 'c:\\hongten.db'
    #数据库表名称
    global TABLE_NAME
    TABLE_NAME = 'student'
    #是否打印sql
    global SHOW_SQL
    SHOW_SQL = True
    print('show_sql : {}'.format(SHOW_SQL))
    drop_table_test()
    create_table_test()
    save_test()
    

def main():
    init()
    fetchall_test()
    print('-' * 50)
    fetchone_test()
    print('-' * 50)
    update_test()
    fetchall_test()
    print('-' * 50)
    delete_test()
    print('-' * 50)
    fetchall_test()



if __name__ == '__main__':
    main()