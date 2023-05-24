import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

device_list={ }
for port in ports:
    device_list[port.name]=port.device


ser = ' '  




from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os


root= Tk()
W_width=900
W_height=500
root.config(bg="#26242f")
root.title("SRM")
root.geometry(f"{W_width}x{W_height}")
root.resizable(0, 0)

f2_bg_color='grey'              # background colour of frame 2
f3_bg_color='#26242f'           # background colour of frame 3
f3_fg_color='white'

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# ---------------------------------------------frame1 (top image)-----------------------------------------------------

f1=Frame(root,bg="black", height=85)  
f1.pack(side=TOP,fill="x")

canvas = Canvas(f1, width= W_width, height= 85,bg="black")
canvas.pack(side=TOP)

pht=Image.open(os.curdir+"/asset/11.png","r")
reimg= pht.resize((W_width,85), Image.LANCZOS)
img=ImageTk.PhotoImage(reimg)

canvas.create_image(10,10,anchor=NW, image=img)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#------------------------------------frame 2 left side--------------------------------------------------------------

f2=Frame(root,width=550,bg=f2_bg_color)
f2.pack(side=LEFT,fill="y") 

x_val=0  
y_val=0       # varibles for containing position value of  x,y,z 
z_val= 0

cut_spd=1       # varibles for containing value of cuting speed
rpm=1           # varibles for containing value of rpm




#                                     Combobox 1 
device = StringVar()
options=[i for i in device_list.keys()]               # combobox option   
combo_box1= ttk.Combobox(f2,state="readonly",values=options,textvariable=device,width=30,height=25)  
combo_box1.set("SELECT DEVICE")
def device_selection(event):
    global ser
    device.set(combo_box1.get())
    print(device.get())
    ser = serial.Serial(device.get(), 115200)
combo_box1.bind('<<ComboboxSelected>>', device_selection)
combo_box1.place(x=20, y=20)



txt1 = StringVar()               # text box for showing the postion  X
txt1.set(str(x_val))
txtbox1 = ttk.Entry(f2, textvariable=txt1,state="readonly",justify="right",)      
txtbox1.place(x=50,y=55)
Label(f2,text="X",bg=f2_bg_color,font=("Arial", 17,"bold")).place(x=20,y=50)
Label(f2,text="mm",bg=f2_bg_color,font=("Arial", 11)).place(x=180,y=55)


txt2 = StringVar()              # text box for showing the postion Y
txt2.set(str(y_val))
txtbox2 = ttk.Entry(f2, textvariable=txt2,state="readonly",justify="right")
txtbox2.place(x=50,y=85)
Label(f2,text="Y",bg=f2_bg_color,font=("Arial", 17,"bold")).place(x=20,y=80)
Label(f2,text="mm",bg=f2_bg_color,font=("Arial", 11)).place(x=180,y=85)


txt3 = StringVar()              # text box for showing the postion Z
txt3.set(str(z_val))
txtbox3 = ttk.Entry(f2, textvariable=txt3,state="readonly",justify="right")
txtbox3.place(x=50,y=115)
Label(f2,text="Z",bg=f2_bg_color,font=("Arial", 17,"bold")).place(x=20,y=110)
Label(f2,text="mm",bg=f2_bg_color,font=("Arial", 10)).place(x=180,y=115)


txt4 = StringVar()             # text box for showing the cuting speed
txt4.set(str(cut_spd))
txtbox4 = ttk.Entry(f2, textvariable=txt4,state="readonly",justify="right")
txtbox4.place(x=50,y=215)
Label(f2,text="Speed",bg=f2_bg_color,font=("Arial", 12)).place(x=20,y=190)
Label(f2,text="mm/min",bg=f2_bg_color,font=("Arial", 10)).place(x=180,y=220)



txt5 = StringVar()              # text box for showing the rpm
txt5.set(str("temp"))       
txtbox5 = ttk.Entry(f2, textvariable=txt5,state="readonly",justify="right")
txtbox5.place(x=50,y=325)
Label(f2,text="Spindle",bg=f2_bg_color,font=("Arial", 12)).place(x=20,y=300)
Label(f2,text="rpm",bg=f2_bg_color,font=("Arial", 10)).place(x=180,y=330)


onn =Button(f2, text = "ON",width=7).place(x=53,y=350)             #  button
off =Button(f2, text = "OFF",width=7).place(x=115,y=350)


# subframe 2.1  for radio button 

f2_1= Frame(f2,bg=f2_bg_color,relief=GROOVE,bd=2)
f2_1.place(x=265,y=215)
s=ttk.Style()
s.configure('w.TRadiobutton',  background=f2_bg_color, foreground='black',font=("Arial", 11)) 
tims_x_shift = StringVar()
tims_x_shift.set(1)

def set_multipler():
    print(tims_x_shift.get())
    print(type(eval(tims_x_shift.get())))

r1 = ttk.Radiobutton(f2_1,text='Continue',style='w.TRadiobutton' , value= 2 , variable=tims_x_shift,command = set_multipler)
r2 = ttk.Radiobutton(f2_1,  text='x100'  ,style='w.TRadiobutton' ,value= 100, variable=tims_x_shift,command = set_multipler)
r3 = ttk.Radiobutton(f2_1,  text='x10'   ,style='w.TRadiobutton' ,value= 10 , variable=tims_x_shift,command = set_multipler)
r4 = ttk.Radiobutton(f2_1,  text='x1'    ,style='w.TRadiobutton' , value=1  , variable=tims_x_shift,command = set_multipler)
r1.grid(row=0,column=0,padx=(10,5),pady=10)
r2.grid(row=0,column=1,padx=5)
r3.grid(row=0,column=2,padx=5)
r4.grid(row=0,column=3,padx=(5,10))

Label(f2,text="Cursur Setup",bg=f2_bg_color,font=("Arial", 10)).place(x=270,y=202)



# subframe 2.0   for control button


Label(f2,text="Cursur Setup",bg=f2_bg_color,font=("Arial", 10)).place(x=285,y=25)
buton_wid=5
buton_hit=2
f2_0= Frame(f2,bg=f2_bg_color,relief=GROOVE,bd=2)
f2_0.place(x=280,y=30)


def move_frnt():
    global y_val 
    y_val = y_val+ eval(tims_x_shift.get())
    txt1.set(y_val)
    if ser!=' ':
        ser.write((f'G0 Y{y_val}\n').encode('latin-1'))



def move_back():
    global y_val
    y_val =y_val- eval(tims_x_shift.get())
    txt1.set(y_val)
    if ser!=' ':
        ser.write((f'G0 Y{y_val}\n').encode('latin-1'))

    
    
def move_right():
    global x_val
    x_val=x_val+ eval(tims_x_shift.get())
    txt2.set(x_val)
    if ser!=' ':
        ser.write((f'G0 X{x_val}\n').encode('latin-1'))
def move_left():
    global x_val
    x_val= x_val- eval(tims_x_shift.get())
    txt2.set(x_val)
    if ser!=' ':
        ser.write((f'G0 X{x_val}\n').encode('latin-1'))
    
def move_up():
    global z_val
    z_val =z_val+ eval(tims_x_shift.get())
    txt3.set(z_val)
    if ser!=' ':
        ser.write((f'G0 Z{z_val}\n').encode('latin-1'))

def move_dwn():
    global z_val
    z_val = z_val - eval(tims_x_shift.get())
    txt3.set(z_val)
    if ser!=' ':
        ser.write((f'G0 Z{z_val}\n').encode('latin-1'))

frn = Button(f2_0, text = "front",width=buton_wid,height=buton_hit,command=move_frnt).grid(row=0,column=1,pady=(15,0))
bak = Button(f2_0, text = "back", width=buton_wid,height=buton_hit,command=move_back).grid(row=2,column=1,pady=(0,15))
rght= Button(f2_0, text = "right",width=buton_wid,height=buton_hit,command=move_right).grid(row=1,column=2,padx=(0,15))
lft = Button(f2_0, text = "left", width=buton_wid,height=buton_hit,command=move_left).grid(row=1,column=0,padx=(15,0))
up  = Button(f2_0, text = "up",   width=buton_wid,height=buton_hit,command=move_up).grid(row=0,column=3,pady=(15,0),padx=15)
dwn = Button(f2_0, text = "down", width=buton_wid,height=buton_hit,command=move_dwn).grid(row=2,column=3,pady=(0,15))






# subframe 2.2  button 

buton_wid1=6
buton_hit1=2

f2_2=Frame(f2,bg=f2_bg_color,relief=GROOVE,bd=2)
f2_2.place(x=270,y=300)

view =Button(f2_2, text = "View",width=buton_wid1,height=buton_hit1)
xy =  Button(f2_2, text = "X/Y", width=buton_wid1,height=buton_hit1)
z =   Button(f2_2, text = "Z",   width=buton_wid1,height=buton_hit1)
stop =Button(f2_2, text = "Stop",width=buton_wid1,height=buton_hit1)

view.grid(row=0,column=0,padx=10,pady=(30,15))
xy.grid(row=0,column=1,padx=(0,2),pady=(30,15))
z.grid(row=0,column=2,pady=(30,15))
stop.grid(row=0,column=3,padx=10,pady=(30,15))

Label(f2,text="Move",bg=f2_bg_color,font=("Arial", 10)).place(x=275,y=288)
Label(f2,text="To Origin",bg=f2_bg_color,font=("Arial", 11)).place(x=370,y=305)



#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#---------------------------------------frame 3--------------------------------------------------------------------------------

f3=Frame(root,width=550,bg=f3_bg_color)
f3.pack(side=LEFT,fill="y")


options=["option 1","option 2","option 3","....and so on ......"]
combo_box2= ttk.Combobox(f3,state="readonly",values=options,width=30,height=25)
combo_box2.place(x=70, y=40)

Label(f3,text="Set Origin Point ",bg=f3_bg_color,font=("Arial", 11),foreground=f3_fg_color).place(x=73,y=15)

xy1 =Button(f3, text = "X/Y",width=6,height=2)
z2 =Button(f3, text = "Z",width=6,height=2)
xy1.place(x=155,y=65)
z2.place(x=210,y=65)

strt =Button(f3, text = "A",width=8,height=2).place(x=40,y=350)
end =  Button(f3, text = "B",width=8,height=2).place(x=100,y=350)
pause =Button(f3, text = "A",width=8,height=2).place(x=160,y=350)
setup =Button(f3, text = "B",width=8,height=2).place(x=220,y=350)

# subframe 3.1

f3_1= Frame(f3,width=200,height=70,bg=f3_bg_color,relief=SUNKEN,bd=2)
f3_1.place(x=75,y=130)
w = Spinbox(f3_1, from_=0, to=10,width=13)
w.place(x=58,y=30)

Label(f3_1,text="Speed",font=("Arial", 11),bg=f3_bg_color,foreground=f3_fg_color).place(x=5,y=28)
Label(f3_1,text=" % ",  font=("Arial", 11),bg=f3_bg_color,foreground=f3_fg_color).place(x=155,y=28)
Label(f3,text="Adjust ",font=("Arial", 11),bg=f3_bg_color,foreground=f3_fg_color).place(x=80,y=117)


# subframe 3.2

f3_2= Frame(f3,width=200,height=80,bg=f3_bg_color,relief=SUNKEN,bd=2)
f3_2.place(x=75,y=250)

h=Scale(f3_2, orient='horizontal',bg=f3_bg_color,foreground='yellow',bd=0)
h.place(x=40,y=20)


root.mainloop()