
from  tkinter import *

class MWindow:
    def __init__(self):
        self.mwin = Tk()
        self.mwin.title("Python Window")
        self.mwin.geometry("850x450")
        self.mwin.config(bg="black")


        #label
        self.lbl = Label(self.mwin, text="Label")
        self.lbl.place(x=300, y=10, w=200, h= 50)
        self.lbl.config(bg="white", fg="black")


        #input field
        self.inText = Entry(self.mwin)
        self.inText.place(x=300, y=70, w=200, h= 30)
        self.inText.config(bg="white", fg="black")

        #button
        self.btn = Button(self.mwin, text="ADD", command=self.onAddBtnClick)
        self.btn.place(x=300, y=110, w=200, h= 30)
        self.btn.config(bg="white", fg="black")

        self.mwin.mainloop()

    def onAddBtnClick(self):
        self.lbl.config(text=self.inText.get())


MWindow()
