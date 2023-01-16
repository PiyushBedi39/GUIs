import os
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import cv2
import random

class Window():

    def __init__(self,window):
        
        self.window=window
        self.window.wm_title("Frame Generator")
        self.window.geometry("700x500")
        self.window.configure(background="light Blue")
        

        self.l1_frame=LabelFrame(window,text="Open Video File Location",padx=40,pady=30,background="Light Blue")
        self.l1_frame.grid(padx=20,pady=20)
        self.l2_frame=LabelFrame(window,text="Save File Location",padx=40,pady=30,background="Light Blue")
        self.l2_frame.grid(padx=20,pady=20)

        b1=Button(self.l1_frame,text="Open File",background="Light Green",command=self.videoFileDialog)
        b1.grid(row=0,column=0,ipadx=10,ipady=10)

        self.b2=Button(self.l2_frame,text="Save Folder",background="Light Green",command=self.savFileDialog)
        self.b2.grid(row=1,column=0,ipadx=10,ipady=10)

        self.b3=Button(window,text="Generate",background="Gold",command=self.generate)
        self.b3.grid(row=2,column=0,columnspan=2,ipadx=40,ipady=20,pady=20,padx=20)
        self.b3['state']=DISABLED
        self.b2['state']=DISABLED


    def videoFileDialog(self):
        self.videofilename=filedialog.askopenfilename(initialdir='/',title="Select a video file",filetypes=(("mp4","*.mp4"),("mkv","*.mkv"),("avi","*.avi"),("mov","*.mov")))
        self.label1=Label(self.l1_frame,text="")
        self.label1.grid(row=1,column=0)
        self.label1.configure(text=self.videofilename, background="Light Blue")
        self.b2['state']=NORMAL

    def savFileDialog(self):
        self.savfilename=filedialog.askdirectory(initialdir='/',title="Select a Folder")
        self.label2=Label(self.l2_frame,text="")
        self.label2.grid(row=2,column=0)
        self.label2.configure(text=self.savfilename, background="Light Blue")
        self.b3['state']=NORMAL

   
    def generate_img(self):   
        self.my_label=Label(self.window,text="")
        self.my_label.grid(row=0,column=2)

        #Create list of all file and choose at random
        files=os.listdir(self.savfilename)
        rd=random.choice(files)

        #resize img
        my_pic=Image.open(f"{self.savfilename}/{rd}")
        resized=my_pic.resize((400,400),Image.ANTIALIAS)
        self.my_image=ImageTk.PhotoImage(resized)

        #display img
        self.my_image_label=Label(image=self.my_image).grid(row=1,column=2,rowspan=3)
        self.my_label.configure(text="Preview",bg="light blue", fg="blue", font="none 20 bold italic underline")
        self.window.geometry("1000x700")
            
    def generate_frames(self):

        cap=cv2.VideoCapture(self.videofilename)
        idx=0

        while True:
            ret, frame= cap.read()
            if ret== False:
                cap.release()
                break
            cv2.imwrite(f"{self.savfilename}/{idx}.png",frame)
            idx+=1

    def generate(self):
        #self.b3.grid_forget()
        
        self.generate_frames()
        self.generate_img()

   
    
    

window=Tk()
Window(window)
window.mainloop()