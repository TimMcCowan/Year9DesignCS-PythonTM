#swim Calc
#measuring distance swam in meters or yards 
#Gui with multiples of 20(y) or 25(m) for recording sets with conversions
#Save inputs for weekly reports which contain goals and maybe graphs
#Also possibility of calories
#swim.com smart swim tracking

import tkinter as tk
import math

def submit():
	d = str(e.get())
	u = v.get()
	print("You swam " +d +" "+u)




root = tk.Tk()

#radio button options
MODES = [
("Meters", "Meters"),
("Yards", "Yards"),
]

v = tk.StringVar()
v.set("A")

t = tk.Label(root,text = "Enter distance swam")
t.pack()

#text box
e = tk.Entry(root)
e.pack()


#choose unit
for r in range(0,len(MODES),1):
	rbtn = tk.Radiobutton(root,text = MODES[r][0],variable = v, value=MODES[r][1])
	rbtn.pack()

#submit button
btn = tk.Button(root,text = "Submit", command = submit)
btn.pack()



root.mainloop()