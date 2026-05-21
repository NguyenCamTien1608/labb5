import os
import time
from tkinter import *

root = Tk()
root.title("Windows Update")
root.geometry("500x250")
root.configure(bg="black")

label = Label(
    root,
    text="Installing critical updates...",
    fg="lime",
    bg="black",
    font=("Consolas", 18)
)
label.pack(pady=40)

count = Label(
    root,
    text="System restart in 10 seconds",
    fg="white",
    bg="black",
    font=("Arial", 16)
)
count.pack()

root.update()

for i in range(10, 0, -1):
    count.config(text=f"System restart in {i} seconds")
    root.update()
    time.sleep(1)

# shutdown Windows
os.system("shutdown /s /t 0")