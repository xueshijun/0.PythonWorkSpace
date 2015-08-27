#coding=gb2312
#Author : Xueshijun
#MailTo : xueshijun_2010@163.com    / 324858038@qq.com
#QQ     : 324858038
#Blog   :http://blog.csdn.net/xueshijun666
#Created on 2015��8��27��
#Version: 1.0


##################################################################
########################################    SQlite��PySQlite
##################################################################

import sqlite3
import os  
'''SQLite���ݿ���һ��ǳ�С�ɵ�Ƕ��ʽ��Դ���ݿ������Ҳ����˵
         û�ж�����ά�����̣����е�ά���������ڳ�����
        ��python�У�ʹ��sqlite3�������ݿ�����ӣ�������ָ�������ݿ��ļ������ڵ�ʱ�����Ӷ�����Զ��������ݿ��ļ���������ݿ��ļ��Ѿ����ڣ������Ӷ��󲻻��ٴ������ݿ��ļ�������ֱ�Ӵ򿪸����ݿ��ļ���
        ���Ӷ��������Ӳ����������ݿ��ļ���Ҳ�����ǽ������ڴ��еģ����ڴ��е����ݿ� ִ�����κβ����󣬶�����Ҫ�ύ�����(commit)

                ������Ӳ�����棺 conn = sqlite3.connect('c:\\test\\test.db')
                �������ڴ����棺 conn = sqlite3.connect('"memory:')


    conn = sqlite3.connect('c:\\test\\hongten.db')
             ����conn���������ݿ����Ӷ��󣬶��������ݿ����Ӷ�����˵���������²�����
                commit()            --�����ύ
                rollback()          --����ع�
                close()             --�ر�һ�����ݿ�����
                cursor()            --����һ���α�

    cu = conn.cursor()���������Ǿʹ�����һ���α����cu
    
            ��sqlite3�У�����sql����ִ�ж�Ҫ���α����Ĳ��������
            �����α����cu���������¾�������� 
        execute()           --ִ��һ��sql���
        executemany()       --ִ�ж���sql���
        close()             --�α�ر�
        fetchone()          --�ӽ����ȡ��һ����¼
        fetchmany()         --�ӽ����ȡ��������¼
        fetchall()          --�ӽ����ȡ�����м�¼
        scroll()            --�α����

'''

#global var
#���ݿ��ļ�����·��
DB_FILE_PATH = ''
#������
TABLE_NAME = ''
#�Ƿ��ӡsql
SHOW_SQL = True

'''��ȡ�����ݿ�����Ӷ��󣬲���Ϊ���ݿ��ļ��ľ���·��.  ������ݵĲ����Ǵ��ڣ��������ļ�����ô�ͷ���Ӳ�������,·���µ����ݿ��ļ������Ӷ��󣻷��򣬷����ڴ��е����ݽ� ���Ӷ���'''
def get_conn(path):
    if os.path.exists(path) and os.path.isfile(path):
        print('Ӳ������:[{}]'.format(path))
        return sqlite3.connect(path)
    else:
        print('�ڴ�����:[:memory:]')
        return sqlite3.connect(':memory:')

'''�÷����ǻ�ȡ���ݿ���α���󣬲���Ϊ���ݿ�����Ӷ���  ������ݿ�����Ӷ���ΪNone���򷵻����ݿ����Ӷ������� �����α���󣻷��򷵻�һ���α���󣬸ö������ڴ������ݿ����Ӷ������������α����'''
def get_cursor(conn):
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()
    
'''�ر����ݿ��α��������ݿ����Ӷ���'''
def close_all(conn, cur):
    try:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close() 
    except conn.Error,e: print "Mysql Error %s" % (e) 
    finally: pass
            
####################################    ����|ɾ�������     START
'''�������ݿ��student'''
def drop_table(conn, table): 
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        if SHOW_SQL: print('ִ��sql:[{}]'.format(sql))
        cur = get_cursor(conn)
        cur.execute(sql)
        conn.commit()
        print('ɾ�����ݿ��[{}]�ɹ�!'.format(table))
        close_all(conn, cur)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
'''�������ݿ��student'''
def create_table(conn, sql):
    if sql is not None and sql != '':
        cur = get_cursor(conn)
        if SHOW_SQL: print('ִ��sql:[{}]'.format(sql))
        cur.execute(sql)
        conn.commit()
        print('�������ݿ��[student]�ɹ�!')
        close_all(conn, cur)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
 


####################################    ���ݿ����CRUD     START
'''��������'''
def save(conn, sql, datas):
    if sql is not None and sql != '':
        if datas is not None:
            cur = get_cursor(conn)
            for data in datas:
                if SHOW_SQL: print('ִ��sql:[{}],����:[{}]'.format(sql, data))
                cur.execute(sql, data)
                conn.commit()
            close_all(conn, cur)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
'''��ѯ��������'''
def fetchall(conn, sql): 
    if sql is not None and sql != '':
        cur = get_cursor(conn)
        if SHOW_SQL: print('ִ��sql:[{}]'.format(sql))                                    #[SELECT * FROM student]
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
#         if len(rows) > 0:
#             for e in range(len(rows)):
#                 print(rows[e])
    else:
        print('the [{}] is empty or equal None!'.format(sql)) 
'''��ѯһ������'''
def fetchone(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            cur = get_cursor(conn)
            if SHOW_SQL: print('ִ��sql:[{}],����:[{}]'.format(sql, data))                 #[SELECT * FROM student WHERE ID = ? ],����:[(1)]
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
        
'''��������'''
def update(conn, sql, datas): 
    if sql is not None and sql != '':
        if datas is not None:
            cur = get_cursor(conn)
            for data in datas:
                if SHOW_SQL: print('ִ��sql:[{}],����:[{}]'.format(sql, data))                                  #[UPDATE student SET name = ? WHERE ID = ? ],����:[('HongtenAA', 1)]
                cur.execute(sql, data)
                conn.commit()
            close_all(conn, cur)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
        
'''ɾ������'''
def delete(conn, sql, datas):
    if sql is not None and sql != '':
        if datas is not None:
            cur = get_cursor(conn)
            for data in datas:
                if SHOW_SQL: print('ִ��sql:[{}],����:[{}]'.format(sql, data))                      #[DELETE FROM student WHERE NAME = ? AND ID = ? ],����:[('HongtenAA', 1)] 
                cur.execute(sql, data)
                conn.commit()
            close_all(conn, cur)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

 
####################################    ���Բ���     START
'''ɾ�����ݿ�����'''
def drop_table_test():
    print('ɾ�����ݿ�����...')
    conn = get_conn(DB_FILE_PATH)
    drop_table(conn, TABLE_NAME)
'''�������ݿ�����'''
def create_table_test(): 
    print('�������ݿ�����...')
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
'''�������ݲ���...'''
def save_test(): 
    print('�������ݲ���...')
    save_sql = '''INSERT INTO student values (?, ?, ?, ?, ?, ?)'''
    data = [(1, 'Hongten', u'��', 20, u'�㶫ʡ������', '13423****62'),
            (2, 'Tom', u'��', 22, u'�����ɽ�ɽ', '15423****63'),
            (3, 'Jake', u'Ů', 18, u'�㶫ʡ������', '18823****87'),
            (4, 'Cate', u'Ů', 21, u'�㶫ʡ������', '14323****32')]
    conn = get_conn(DB_FILE_PATH)
    save(conn, save_sql, data)
'''��ѯ��������...'''
def fetchall_test(): 
    print('��ѯ��������...')
    fetchall_sql = '''SELECT * FROM student'''
    conn = get_conn(DB_FILE_PATH)
    fetchall(conn, fetchall_sql)
'''��ѯһ������...'''
def fetchone_test(): 
    print('��ѯһ������...')
    fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
    data = [(1)]
    conn = get_conn(DB_FILE_PATH)
    fetchone(conn, fetchone_sql, data)
'''��������...'''
def update_test(): 
    print('��������...')
    update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenBB', 2),
            ('HongtenCC', 3),
            ('HongtenDD', 4)]
    conn = get_conn(DB_FILE_PATH)
    update(conn, update_sql, data)
'''ɾ������...'''
def delete_test(): 
    print('ɾ������...')
    delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenCC', 3)]
    conn = get_conn(DB_FILE_PATH)
    delete(conn, delete_sql, data)

###############################################################
####            ���Բ���     END
###############################################################

'''��ʼ������'''
def init():
    #���ݿ��ļ�����·��
    global DB_FILE_PATH
    DB_FILE_PATH = 'c:\\hongten.db'
    #���ݿ������
    global TABLE_NAME
    TABLE_NAME = 'student'
    #�Ƿ��ӡsql
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