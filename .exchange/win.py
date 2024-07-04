#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# import tkinter
# top = tkinter.Tk()
# # 进入消息循环
# top.mainloop()

from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("全屏图像")
image = Image.open("image.jpg")
root.attributes("-fullscreen",True)
def toggle_fullscreen(event):
    state = root.attributes("-fullscreen")
    root.attributes("-fullscreen", not state)
def exit_full(event):
    root.destroy()

root.bind("<Double-Button-1>", exit_full)
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.pack()
root.mainloop()
