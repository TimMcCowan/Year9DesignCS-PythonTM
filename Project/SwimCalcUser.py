import tkinter as tk

def user():
	print("User selected: "+var.get())
	

root = tk.Tk() #Constructs our main window

#List of strings 
#My list is called options there are 3 elements with index 0 to 2
#print(OPTIONS[2])
OPTIONS = [
	"Tim",
	"Will",
	"John",
	"Ethan",

]

var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",user)

ttl = tk.Label(root,text="User Select")
ttl.grid(column = 0, row = 0, columnspan = 2)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2],OPTIONS[3])
dropDownMenu.grid(column = 0, row = 1)


goBtn = tk.Button(root, text = "Go!", command = user)
goBtn.grid(column = 1,row = 1)


root.mainloop()
