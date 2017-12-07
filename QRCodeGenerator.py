##############################
# Author Caleb Fahlgren
# Date   12/7/2017
# QR Code Generator GUI
###############################
import pyqrcode,png
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from pyqrcode import *

#Build the form
root = Tk()
root.title("QR Code Generator")
root.geometry("600x600")

#Create Text area
TextArea = Text(width=60, pady=0)
TextArea.insert(END, "Type url here.")

#Create Title Label
titleLabel = Label(text="QR Code", font=("Helvetica", 16))

#Take a parameter and generate the QR Code
def generateQR(url):
    url = pyqrcode.create("test")
    url.png('url.png', scale=5)

#Start GUI
titleLabel.pack()
TextArea.pack()
mainloop()