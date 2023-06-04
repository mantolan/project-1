
from tkinter import *
def mainmenu():
    root = Tk()
    def close():
        root.destroy()
        root.quit()
    root.geometry("1200x700")
    bg = PhotoImage(file="k.png")
    canvas1 = Canvas(root, width=900, height= 400)
    canvas1.pack(fill="both",expand=True)
    canvas1.create_image(0,0,image = bg, anchor= "nw")
    canvas1.create_text(690, 400, text="MINI CRAFT", font=("Arial", 50), fill="white")
    button =  Button(root, text="start", width=10, height= 3, command = close)
    button_window =canvas1.create_window(630, 440, anchor="nw", window=button )

    root.mainloop()

