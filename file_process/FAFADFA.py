from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


app = Application()
# 设置窗口标题:
# print(dir(app.master))
# print(dir(app))
# app.master.title('Hello Worddddddddddddddld')
# 主消息循环:
app.mainloop()

