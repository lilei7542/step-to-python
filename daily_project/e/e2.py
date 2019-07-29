#!/usr/local/Python-3.7.0rc1/bin/python3.7



#!/usr/local/Python-3.7.0rc1/bin/python3.7
#coding=utf-8
import cgi, os
import cgitb; 
cgitb.enable()
form = cgi.FieldStorage()
# print (dir(form))
# Get filename here.
fileitem = form['filename']
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






print """\



print ("Content-type:text/html")
print ()
('<html>')
('<head>')
('<meta charset="utf-8">')
('<title>菜鸟教程(runoob.com)</title>')
('</head>')
('<body>')
('   <p>%s</p>')
('</body>')
('</html>')

print('lalala')