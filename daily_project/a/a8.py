# # import sound
# import request
# import docutils
# import pyclts  #pip install pyclts-0.2.0-py2.py3-none-any.whl 

# import beeply
# help(beeply)
# beeply()


# from beeply import notes
# mybeep = notes.beeps()
# mybeep.hear('C_')
# mybeep.hear('D')
# mybeep.hear('E')
# mybeep.hear('F')

import winsound
import time
# winsound.PlaySound('C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3',winsound.SND_ASYNC)
# play()
# winsound.PlaySound('ALARM8', winsound.SND_ASYNC) 
def play():

# print ("播放声音")

#winsound.PlaySound('SystemExit', winsound.SND_ALIAS)

    winsound.PlaySound('C:\\Users\\Public\\Music\\Sample Music\\Mellow.wav', winsound.SND_NOSTOP) #立即返回，支持异步播放

    # while(True):

    # 	time.sleep(0.2)

			# print ("s"),



# if __name__ == '__main__':

play()


# no.2
import pyttsx3
a = pyttsx3.init()
a.say("快说")
a.runAndWait()

