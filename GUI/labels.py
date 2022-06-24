from tkinter import *
root=Tk()
miFrame=Frame(width="500", height="400")
miFrame.pack() 
miLabel= Label(miFrame, text="nuevo label", fg="red", font=("Comic Sans MS", 18))
miLabel.place(x=100, y=200) #Ubica el label (pixeles)
miImagen=PhotoImage(file=r"C:\Users\guill\Documents\Python\GUI\mouse.png") #r converts normal string to raw string, where backlashes aren't treated as a scape character.
miLabel2=Label(miFrame,image=miImagen).place(x=100,y=300)
#tkinter trabaja con imagenes .png, .gif y .ico nada más.

root.mainloop()