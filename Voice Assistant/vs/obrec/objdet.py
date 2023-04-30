
from imageai.Detection import ObjectDetection
import os
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk, Image
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(r"C:\Users\Nickh\Downloads\JARVIS\vs\obrec\retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector.loadModel()
global detections
global text
detections = detector.detectObjectsFromImage(input_image=os.path.join(r"C:\Users\Nickh\Downloads\JARVIS\vs\obrec\image.jpg"), output_image_path=os.path.join(r"C:\Users\Nickh\Downloads\JARVIS\vs\obrec\imagenew.jpg"), minimum_percentage_probability=30)
global lst
lst=[]
for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")
clas = Tk() 

# Define the geometry of the window
clas.geometry("600x900")
text = scrolledtext.ScrolledText(clas, width=40, height=25)
def show_msg():
        for eachObject in detections:
            txt=eachObject["name"] , " : ", eachObject["percentage_probability"],"%", " : ", eachObject["box_points"]
            text.insert('end', txt)
            text.pack()

b=Button(clas, text='show %', width=15, command=show_msg)
frame = Frame(clas, width=1000, height=1000)
frame.pack()
frame.place(anchor='n', relx=0.5, rely=0.5)
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(r"C:\Users\Nickh\Downloads\JARVIS\vs\obrec\imagenew.jpg"))
# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
b.pack()
clas.mainloop()
