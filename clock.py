from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    current_time = strftime('%I:%M:%S %p')  
    current_date = strftime('%d-%m-%Y')  
    
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    time_label.after(1000, time)
    

time_label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
time_label.pack(anchor='center')


date_label = Label(root, font=("CASTELLAR", 40), background="black", foreground="cyan")
date_label.pack(anchor='center')

time()
mainloop()
