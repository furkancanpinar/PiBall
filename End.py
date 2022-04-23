import tkinter as tk
from tkinter import ttk, font
from datetime import datetime, timedelta
from itertools import cycle

#Changing colour constantly
color = cycle(['red', 'blue', 'green'])

#Modifying the labels
def show_time():
    
    lbl.config(text="GAME OVER ",font =("Tw Cen MT", 150), foreground=next(color))
    lbl2.config(text="Made By FURKAN CANPINAR ",font =("Tw Cen MT", 20), foreground=next(color))
    lbl3.config(text="CLICK ON 'Esc' KEY TO EXIT",font =("Tw Cen MT", 40), foreground=next(color))
    lbl4.config(text="THANK YOU FOR PLAYING PIBALL",font =("Tw Cen MT", 40), foreground=next(color))
    # Trigger the countdown after 1000ms
    root.after(50, show_time)

def quit(event):
    root.destroy()
root = tk.Tk()
#making the gui fullscreen
root.attributes("-fullscreen", True)
root.configure(background='gray9')
#Combining esc key to exit the full screen and kill the game
root.bind('<Escape>', quit)


lbl = ttk.Label(root, foreground="green2", background="gray9")
lbl2 = ttk.Label(root , foreground="red3", background="gray9")
lbl3 = ttk.Label(root , foreground="red3", background="gray9")
lbl4 = ttk.Label(root, foreground="green2", background="gray9")
lbl.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
lbl2.place(relx = 0.91 , rely=0.97, anchor=tk.CENTER)
lbl3.place(relx = 0.5 , rely=0.5, anchor=tk.CENTER)
lbl4.place(relx = 0.5 , rely=0.55, anchor=tk.CENTER)

#starting the timer
show_time() 
root.mainloop()
