from tkinter import * #tkinter module

root=Tk()            #Tk() predefined function from tkinter module to create empty window
root.title("Tkinter ")
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File")
filemenu.add_cascade(label="New File")
menu.add_cascade(label="Open")
menu.add_cascade(label="Save")
#Label
l=Label(root,text="Hello world",font=('green',20))  #font -- font color / size
  # l.pack()    # pack() if there is single widgits to launch 
Button(root,text="show",bg="blue",foreground="white",font=('green',20)).grid(row=3,column=0) #bg -- background color of button foreground--font color of button
#b.pack() without grid 
Label(root,text="Enter your name").grid(row=0,column=0) #grid() position
Entry(root).grid(row=0,column=1)         #Entry() -- input box
Radiobutton(root,text='Python').grid(row=1,column=0)     # radiobutton
Checkbutton(root,text='FrontEnd').grid(row=2,column=0) #check box
      

root.mainloop()    # mainloop() function to start window
