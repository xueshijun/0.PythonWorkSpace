'''
Created on 2015年8月27日

@author: Administrator
'''

from win32com.client import DispatchEx
import time
ie=DispatchEx("InternetExplorer.Application")  
ie.Navigate("http://hi.baidu.com/mirguest/creat/blog/")
ie.Visible=1
while ie.Busy:
    time.sleep(1) 
body=ie.Document.body
# header
for i in body.getElementsByTagName("input"):
    if str(i.getAttribute("id"))=="spBlogTitle":
        print "Find title"
        i.value="AutoCreatedByPython"
        break 
 # editor
for i in body.getElementsByTagName("iframe"):
    print "Find iframe"
    if str(i.getAttribute("id"))=="tangram_editor_iframe_TANGRAM__1":
        print "Find"
        break
iframe=i
iframe.click()
sondoc=iframe.contentWindow.Document;
print sondoc
sonbody=sondoc.body
print sonbody
for ii in sonbody.getElementsByTagName("p"):
    print "Find p"
    ii.innerHTML="hello,my first try"
tmp=sondoc.createElement("div")
tmp.innerHTML="bye"
sonbody.insertBefore(tmp,ii) 
tmpHTML="<div>hello 2</div>"
sonbody.insertAdjacentHTML("beforeEnd",tmpHTML)
'''
editor.getContentHTML
''' 
# submit
for i in body.getElementsByTagName("div"):
    if str(i.getAttribute("id"))=="btn-box":
        print "Find button"
        break 
btnbox=i
j=btnbox.childNodes(0)
j.click()