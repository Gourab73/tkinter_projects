from tkinter import *

root =Tk()

root.geometry("400x520")
root.title("Calculator")

def click(event):
    global screenValue
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if screenValue.get().isdigit():
            value = int(screenValue.get())
        else:
            value = eval(screenEntry.get())
        screenValue.set(value)
        screenEntry.update()
    elif text == "C":
        screenValue.set("")
        screenEntry.update()
    else:
        screenValue.set(screenValue.get() + text)
        screenEntry.update()


screenValue = StringVar()
screenValue.set("")
screenEntry = Entry(root, textvariable=screenValue,font="lucida 25 bold",)
screenEntry.pack(fill=X, ipadx=8, padx=10,pady=10)


frame = Frame(root, bg="grey", padx=18)

button = Button(frame, text="9", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

button = Button(frame, text="8", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

button = Button(frame, text="7", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

frame.pack()

frame = Frame(root, bg="grey", padx=18)

button = Button(frame, text="6", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

button = Button(frame, text="5", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

button = Button(frame, text="4", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

frame.pack()

frame = Frame(root, bg="grey", padx=18)

button = Button(frame, text="3", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

button = Button(frame, text="2", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

button = Button(frame, text="1", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

frame.pack()

frame = Frame(root, bg="grey",padx=18)

button = Button(frame, text="0", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

button = Button(frame, text="*", padx=23, pady=2, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

button = Button(frame, text="/", padx=23.5, pady=2, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

frame.pack()

frame = Frame(root, bg="grey", padx=18)

button = Button(frame, text="%", padx=15.5, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

button = Button(frame, text="+", padx=20, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

button = Button(frame, text="-", padx=22.5, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=2)
button.bind("<Button-1>",click)

frame.pack()

frame = Frame(root, bg="grey")

button = Button(frame, text=".", padx=20, pady=1, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=1)
button.bind("<Button-1>",click)

button = Button(frame, text="C", padx=17, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=1)
button.bind("<Button-1>",click)

button = Button(frame, text="=", padx=16, pady=3, font="lucida 25 bold")
button.pack(side=LEFT, padx=8, pady=1)
button.bind("<Button-1>",click)

frame.pack()



root.mainloop()