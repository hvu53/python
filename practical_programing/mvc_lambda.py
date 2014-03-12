import tkinter
window = tkinter.Tk()

# the model
counter = tkinter.IntVar()
counter.set(0)

# two controller
def click(variable, value):
	variable.set(variable.get()+value)
# the views
frame = tkinter.Frame(window)
frame.pack()
button=tkinter.Button(frame, text='Up', command=lambda: click(counter,1))
button.pack()
button=tkinter.Button(frame, text='Down', command=lambda: click(counter,-1))
button.pack()
label = tkinter.Label(frame, textvariable=counter)
label.pack()

window.mainloop()