import tkinter
from tkinter import filedialog


root = tkinter.Tk()
file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
if file != None:
       data = file.read()
       file.close()
       print ("I got %d bytes from this file." % len(data))
       print(data)
