from tkinter import *
from PIL import Image,ImageTk
import os

class display :
    gui_root = Tk()
    W_width=900
    W_height=450

    def __init__(self) -> None:

        self.gui_root.config(bg="#26242f")
        
        self.gui_root.title("SRM")
        self.gui_root.geometry(f"{self.W_width}x{self.W_height}")
        self.gui_root.resizable(0, 0)


    def top_img(self):
        print("check")
        f1=Frame(self.gui_root,bg="black", height=85)
        f1.pack(side=TOP,fill="x")
        global canvas
        canvas = Canvas(f1, width= self.W_width, height= 85,bg="black")
        canvas.pack(side=TOP)
        pht=Image.open(os.curdir+"/asset/11.png","r")
        reimg= pht.resize((self.W_width,90), Image.LANCZOS)
        img=ImageTk.PhotoImage(reimg)
        canvas.create_image(10,10,anchor=NW, image=img)

        f2=Frame(self.gui_root,bg="#26242f",width=self.W_width)
        f2.pack(side=LEFT,anchor=NW,fill="y")
        
    

    def run(self):

        self.top_img()
        self.gui_root.mainloop()
    

def __main__():
    mydis=display()
    mydis.run()

if __main__:

    __main__()

