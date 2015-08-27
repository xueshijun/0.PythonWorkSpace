 最近学习Python网络编程，想实现一些小工具来用用，所以找了相关的模块。这里是win32com的，用来操作word之类的东西。我用的Python2.6 下载了地址：
http://sourceforge.net/projects/pywin32/files/
我选择的 版本是：pywin32-212.win32-py2.6.exe   可以使用。记录一下。
http://blog.csdn.net/qq404766692/article/details/8365542
使用技巧


（3）处理excel

［1］使用PyExcelerator读写EXCEL文件(Platform: Win,Unix-like) 
优点：简单易用      缺点：不可改变已存在的EXCEL文件。 
PyExcelerator是一个开源的MS Excel文件处理python包。它主要是用来写 Excel 文件.URL:  http://sourceforge.net/projects/pyexcelerator/ 
我没有找到关于PyExcelerator的文档。只是看到了limodou的一篇介绍。 
http://blog.donews.com/limodou/archive/2005/07/09/460033.aspx 
这个包使用起来还是比较简单的：）。带了很多小例子，可以参照。 
例mini.py. 
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝ 
#!/usr/bin/env python 
# -*- coding: windows-1251 -*- 
# Copyright (C) 2005 Kiseliov Roman 
__rev_id__ = """$Id: mini.py,v 1.3 2005/03/27 12:47:06 rvk Exp $""" 
"导入模块 
from pyExcelerator import * 
"生成一个工作薄 
w = Workbook() 
"加入一个Sheet 
ws = w.add_sheet('Hey, Dude') 
"保存 
w.save('mini.xls') 
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝ 
[2]使用COM接口，直接操作EXCEL(只能在Win上) 
优点：可以满足绝大数要求。缺点：有些麻烦。:-) 
这方面的例子很多，GOOGLE 看吧:-). 文档也可以参看OFFICE自带的VBA EXCEL 帮助文件(VBAXL.CHM)。这里面讲述了EXCEL VBA的编程概念， 
不错的教程！另外，《Python Programming on Win32》书中也有很详细的介绍。这本书中给出了一个类来操作EXCEL 文件，可以很容易的加以扩展。 
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from win32com.client import Dispatch 
import win32com.client 
class easyExcel: 
    """A utility to make it easier to get at Excel.  Remembering 
    to save the data is your problem, as is  error handling. 
    Operates on one workbook at a time.""" 
    def __init__(self, filename=None): 
        self.xlApp = win32com.client.Dispatch('Excel.Application') 
        if filename: 
            self.filename = filename 
            self.xlBook = self.xlApp.Workbooks.Open(filename) 
        else: 
            self.xlBook = self.xlApp.Workbooks.Add() 
            self.filename = ''  
    def save(self, newfilename=None): 
        if newfilename: 
            self.filename = newfilename 
            self.xlBook.SaveAs(newfilename) 
        else: 
            self.xlBook.Save()    
    def close(self): 
        self.xlBook.Close(SaveChanges=0) 
        del self.xlApp 
    def getCell(self, sheet, row, col): 
        "Get value of one cell" 
        sht = self.xlBook.Worksheets(sheet) 
        return sht.Cells(row, col).Value 
    def setCell(self, sheet, row, col, value): 
        "set value of one cell" 
        sht = self.xlBook.Worksheets(sheet) 
        sht.Cells(row, col).Value = value 
    def getRange(self, sheet, row1, col1, row2, col2): 
        "return a 2d array (i.e. tuple of tuples)" 
        sht = self.xlBook.Worksheets(sheet) 
        return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value 
    def addPicture(self, sheet, pictureName, Left, Top, Width, Height): 
        "Insert a picture in sheet" 
        sht = self.xlBook.Worksheets(sheet) 
        sht.Shapes.AddPicture(pictureName, 1, 1, Left, Top, Width, Height) 
    def cpSheet(self, before): 
        "copy sheet" 
        shts = self.xlBook.Worksheets 
        shts(1).Copy(None,shts(1)) 
"下面是一些测试代码。 
if __name__ == "__main__": 
    PNFILE = r'c:\screenshot.bmp' 
    xls = easyExcel(r'D:\test.xls') 
    xls.addPicture('Sheet1', PNFILE, 20,20,1000,1000) 
    xls.cpSheet('Sheet1') 
    xls.save() 
    xls.close()

（4）python调用短信猫控件，发短信

#! /usr/bin/env python

#coding=gbk
import sys
import win32com.client
ocxname='ShouYan_SmsGate61.Smsgate'
axocx=win32com.client.Dispatch(ocxname)
axocx.CommPort=8#设置COM端口号
axocx.SmsService='+8613800100500'#设置短信服务号码
axocx.Settings='9600,n,8,1'#设置com端口速度
axocx.sn='loyin'
c=axocx.Connect(1)#连接短信猫或手机
 
print '连接情况',axocx.Link()
 
axocx.SendSms('python确实是很好的','15101021000',0)#发送短信