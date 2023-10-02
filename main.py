#! /bin/python3

import tkinter as tk


def show(*args):
    for arg in args:
        arg.pack()

window = tk.Tk()
title = tk.Label(
    text="Linux Download Manager",
    background="#d8e3eb",
    fg="black",
    width=150,
    height=1,
)

download_label = tk.Label(text="Enter URL For Download")
download_input = tk.Entry()
download_spacer = tk.Label(text=" ")

title.pack()
download_label.pack(side=tk.LEFT)
download_spacer.pack()
download_spacer.pack()
download_input.pack(side=tk.LEFT)

window.mainloop()
