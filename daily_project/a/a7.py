# no.1
import sys
for i in sys.argv:
   print(i)
print('\n\nPython 路径为：', sys.path, '\n')
a=sys.getdefaultencoding()
print (a)


# import playsound
# playsound.playsound('C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3')

# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("Hello, it works!")

import win32com
print (win32com.__file__)