##############################
# Author Caleb Fahlgren
# Date   12/7/2017
# QR Code Generator GUI
###############################
import pyqrcode,png
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import tkinter.messagebox
from pyqrcode import *

#Build the form
root = Tk()
root.title("QR Code Generator")
root.geometry("600x450")
root.resizable(0,0)

#Create Text area
TextArea = Text(width=60, pady=0)
TextArea.insert(END, "Type url here.")

#Create Title Label
titleLabel = Label(text="QR Code", font=("Helvetica", 16))

def create():
    submit = tkinter.messagebox.askquestion("Submit Entry", "Are you sure you want to submit?")
    if submit == "yes":
        try:
            path = tkinter.filedialog.asksaveasfilename()
        except Exception:
            return
        generateQR(TextArea.get("1.0", END), path)

#Create Button
createButton = Button(fg="white", bg="green", text="Create", width=50, command=create, activebackground="yellow")

#Take a parameter and generate the QR Code
def generateQR(url,path):
    url = pyqrcode.create(url)
    url.png(path + ".png", scale=5)
    tkinter.messagebox.showinfo("Created","Created QR Code Successfully!")

#Start GUI
titleLabel.pack()
TextArea.pack()
createButton.pack()
mainloop()