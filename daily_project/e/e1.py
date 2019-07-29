print ("Content-type:text/html")
print ()                             # 空行，告诉服务器结束头部
print ('<html>')
print ('<head>')
print ('<meta charset="utf-8">')
print ('<title>Hello Word - 我的第一个 CGI 程序！</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
print ('</body>')
print ('</html>')









#!/usr/bin/python
#coding=utf-8
# Import modules for CGI handling 
import cgi, os
import cgitb; 
cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['upload']
# Test if the file was uploaded
if fileitem.filename:
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   # get store path  and save it 
   open(os.getcwd()+'/files/' + fn,'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'

print('Content-type:text/html \n\n')
print('file %s' % message)
