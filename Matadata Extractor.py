from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image , ImageTk
from PIL import Image
from PIL.ExifTags import TAGS
import cv2 as cv
win = Tk()
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.geometry('{}x{}'.format(w,h))
def addpic():
    f_types = [('Jpg files','*jpg'),('PNG','*.png')]
    filename = tk.filedialog.askopenfilename(filetypes = f_types)
    #img = cv.imread("{}".format(filename))
    #cv.imshow("check",img)
    img = Image.open(filename)
    width, height = img.size
    print(width, height)
    if width >1000:
        img = img.resize((int(width/8), int(height/8)))
    elif width >600:
        img = img.resize((int(width/2), int(height/2)))
    img = ImageTk.PhotoImage(img)

    lab = Label(win)
    lab.image = img
    lab['image'] = img
    lab.place(relx = 0.45,rely = 0.20)
    # open the image
    image = Image.open("{}".format(filename))

    #Extracting the exif metadata
    exifdata = image.getexif()
    tagname = []
    value = []
    #Looping through all the tags present in exifdata
    for tagid in exifdata:
            
            # getting the tag name instead of tag id
            
            tagname.append(TAGS.get(tagid, tagid))

            # passing the tagid to get its respective value
            
            value.append(exifdata.get(tagid))
    y = 20
    for e in (tagname):
        Label(text = e).place(x = 30,y = y)
        y = y+50
    z = 20
    for e in (value):
        Label(text = e).place(x = 150,y = z )
        z = z+50
b1 = Button(win,text = 'Select',command = addpic)
b1.place(relx = 0.90,rely = 0.10)


