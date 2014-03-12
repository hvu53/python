import tkinter
def change(widget, colors):
	""" Update the foreground color of a widget to show the RGB color value
	stored in a dictionary with keys 'red', 'green', 'blue'
	"""
	new_val = '#'
	for name in ('red','green', 'blue'):
		new_val += colors[name].get()
	widget['bg'] = new_val

# create the application
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

# set up text entry widgets for red, green, blue, storing the associated
# variables in a dictioanry for later use
colors = {}
for (name, col) in (('red','#ff0000'),('green', '#00ff00'),('blue','#0000ff')):
	colors[name] = tkinter.StringVar()
	colors[name].set('00')
	entry = tkinter.Entry(frame, textvariable=colors[name], bg=col, fg='white')
	entry.pack()

# display the current color
current = tkinter.Label(frame, text='		', bg='#ffffff')
current.pack()

# give the user a way to trigger a color update
update = tkinter.Button(frame, text='Update',command=lambda: change(current,colors))
update.pack()
tkinter.mainloop()