import main_ui
from tkinter import *

ui = Tk()

button1 = Button(ui, text= "teste", command= lambda:main_ui.voice_now("teste")).pack()


ui.mainloop()
