import tkinter as tk

def Window():
    window = tk.Tk()
    return window

def Window_title(window,x):
    window.title(x)

def Window_background(window,x):
    window.config(bg=x)

def Window_geometry(window,w,h):
    window.geometry(f"{str(w)}x{str(h)}")

def Window_icon(window,x):
    window.iconbitmap(x)

def Window_mainloop(window):
    window.mainloop()

win = Window()
Window_title(win,"Test")
Window_background(win,"#009688")
Window_geometry(win,500,500)
Window_mainloop(win)