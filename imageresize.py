from tkinter import *
import tkinter as tk
from tkinter import messagebox,filedialog
import os,cv2

img=''

def imgbrowse():
    global img
    fd=filedialog.askopenfilename(initialdir=os.getcwd(),title="Browse Image File",filetypes=(("JPG Image","*.jpg"),("PNG Image","*.png"),("All Files","*.*")))
    t1.set(fd)
    img = cv2.imread(fd,cv2.IMREAD_UNCHANGED)   
    height.set(img.shape[0])
    width.set(img.shape[1])

def imgpreview():
    cv2.imshow("SOURCE IMAGE",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def recalculate():
    newwidth=int(int(width.get()) * int(percentage.get()) / 100)  
    newheight=int(int(height.get()) * int(percentage.get()) / 100)    
    width.set(newwidth)
    height.set(newheight)     
 
def img2preview():
    newwidth=int(width.get())
    newheight=int(height.get())
    img2=cv2.resize(img,(newwidth,newheight),interpolation=cv2.INTER_AREA)
    cv2.imshow("RESIZED IMAGE",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def save():
    fd=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save Image File",filetypes=(("JPG Image","*.jpg"),("PNG Image","*.png"),("All Files","*.*")))
    newwidth=int(width.get())
    newheight=int(height.get())
    img2=cv2.resize(img,(newwidth,newheight),interpolation=cv2.INTER_AREA) 
    cv2.imwrite(fd,img2)   
    messagebox.showinfo("MESSAGE","IMAGE SAVED SUCCESSFULLY") 
        
root=Tk() 

root.title("IMAGE RESIZE APPLICATION")
root.geometry("1000x700")
root.configure(bg="light blue")

t1=StringVar()
width=StringVar()
height=StringVar()
percentage=StringVar()

frame1 = LabelFrame(root,highlightbackground="royalblue", highlightthickness=10,text="Source File",font=('courier', 20,"bold"))
frame1.pack(fill="both",expand="yes",padx=20,pady=20)

frame2 = LabelFrame(root,highlightbackground="royalblue", highlightthickness=10,text="Image Details",font=('courier', 20,"bold"))
frame2.pack(fill="both",expand="yes",padx=20,pady=20)

frame3 = LabelFrame(root,highlightbackground="royalblue", highlightthickness=10,text="Pixel Safe",font=('courier', 20,"bold"))
frame3.pack(fill="both",expand="yes",padx=20,pady=20)

frame4 = LabelFrame(root,highlightbackground="royalblue", highlightthickness=10,text="Actions",font=('courier', 20,"bold"))
frame4.pack(fill="both",expand="yes",padx=20,pady=20)

frame1.config(bg="skyblue")

frame2.config(bg="skyblue")

frame3.config(bg="skyblue")

frame4.config(bg="skyblue")

label1=Label(frame1,text="Source File :",bg="skyblue",font=('courier', 13))
label1.pack(side=tk.LEFT,padx=10,pady=10)

entry1=Entry(frame1,textvariable=t1,font=('courier', 13), justify=CENTER)
entry1.pack(side=tk.LEFT,padx=10,pady=10)

button1=Button(frame1,text="Browse",command=imgbrowse,bg="steelblue2",font=('courier', 13))
button1.pack(side=tk.LEFT,padx=10,pady=10)

button2=Button(frame1,text="Preview",command=imgpreview,bg="steelblue2",font=('courier', 13))
button2.pack(side=tk.LEFT,padx=10,pady=10)

label2=Label(frame2,text="Dimension (Width X Height) :",bg="skyblue",font=('courier', 13))
label2.pack(side=tk.LEFT,padx=10,pady=10)

entry2=Entry(frame2,textvariable=width,font=('courier', 13), justify=CENTER)
entry2.pack(side=tk.LEFT,padx=10,pady=10)

label3=Label(frame2,text="X",bg="skyblue",font=('courier', 13))
label3.pack(side=tk.LEFT,padx=10,pady=10)

entry3=Entry(frame2,textvariable=height,font=('courier', 13), justify=CENTER)
entry3.pack(side=tk.LEFT,padx=10,pady=10)

label4=Label(frame3,text="Percentage :",bg="skyblue",font=('courier', 13))
label4.pack(side=tk.LEFT,padx=10,pady=10)

entry4=Entry(frame3,textvariable=percentage,font=('courier', 13), justify=CENTER)
entry4.pack(side=tk.LEFT,padx=10,pady=10)

button3=Button(frame3,text="Recalculate Dimension",command=recalculate,bg="steelblue2",font=('courier', 13))
button3.pack(side=tk.LEFT,padx=10,pady=10)

button4=Button(frame4,text="Preview",command=img2preview,bg="steelblue2",font=('courier', 13))
button4.pack(side=tk.LEFT,padx=10,pady=10)

button5=Button(frame4,text="Save",command=save,bg="steelblue2",font=('courier', 13))
button5.pack(side=tk.LEFT,padx=10,pady=10)

root.mainloop()