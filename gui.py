from tkinter import StringVar
from tkinter import *
from tkinter import ttk



class FeetToMeters:

  def __init__(self,root):
    root.title('Feet to Meters')

    #creating the frame to hold the gui
    mainframe = ttk.Frame(root, padding=(3,3,12,12))
    mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

    #Initializing feet variable to hold the text
    self.feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
    feet_entry.grid(column=2, row=1, sticky=(W,E))

    #Initilazing meter variable 
    self.meters = StringVar()

    ttk.Label(mainframe, textvariable=self.meters).grid(column=2,row=2, sticky=(W,E))
    ttk.Button(mainframe, text='Calculate', command=self.calculate).grid(column=3,row=3,sticky=W)

    ttk.Label(mainframe, text='feet').grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text='is equivalent to').grid(column=1, row=2,sticky=E)
    ttk.Label(mainframe, text='meters').grid(column=3,row=2,sticky=W)

    #configure column & row properties, weight is used to make the column expand
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    mainframe.columnconfigure(2,weight=1)

    for child in mainframe.winfo_children():
      child.grid_configure(padx=5, pady=5)

    feet_entry.focus()
    root.bind('<Return>', self.calculate)

  def calculate(self, *args):
    try:
      value = float(self.feet.get())
      self.meters.set(round(0.3048 * value, 4))
    except ValueError:
      self.meters.set('Error')

root = Tk()
FeetToMeters(root)
root.mainloop()