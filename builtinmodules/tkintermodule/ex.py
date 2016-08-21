from tkinter import *

class Window(Frame):
    #inits a Frame - find this in tkinter
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill = BOTH, expand = 1)

        #Button is from tkinter , command is basically event handling 
        quitButton = Button(self, text = 'Quit', command = self.client_exit)
        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit() 

root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()
