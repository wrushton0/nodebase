# This is a sample Python script.

from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

def main():
    window = Tk()

    label = Label(window, bg="red", width=10, height=5)
    label.place(x=0, y=0)

    label1= Label(window, bg="blue", width=10, height=5)
    label1.place(x=10, y=10)

    label.bind("<Button-1>", drag_start)
    label.bind("<B1-Motion>", drag_motion)

    window.mainloop()

if __name__ == '__main__':
    main()