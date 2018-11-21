#swim Calc
#measuring distance swam in meters or yards 
#Gui with multiples of 20(y) or 25(m) for recording sets with conversions
#Save inputs for weekly reports which contain goals and maybe graphs
#Also possibility of calories
#swim.com smart swim tracking

import tkinter as tk
import math

def submit():
	d1 = e1.get()
	

	d2 = e2.get()
	

	d3 = e3.get()
	

	d4 = e4.get()
	d4 = int(d4)

	d5 = e5.get()
	d5 = int(d5)

	d6 = e6.get()
	d6 = int(d6)

	d7 = e7.get()
	d7 = int(d7)

	ttl = d1+d2+d3+d4+d5+d6+d7
	u = v.get()
	print("You swam " +ttl+" "+u)




root = tk.Tk()

#radio button options
MODES = [
("Meters", "Meters"),
("Yards", "Yards"),
]

v = tk.StringVar()
v.set("A")

#label 1
t1 = tk.Label(root,text = "Enter distance swam for workout 1")
t1.pack()

#text box 1 
e1 = tk.Entry(root)
e1.pack()

# label 2
t2 = tk.Label(root,text = "Enter distance swam for workout 2")
t2.pack()

#text box 2 
e2 = tk.Entry(root)
e2.pack()

# label 3
t3 = tk.Label(root,text = "Enter distance swam for workout 3")
t3.pack()

#text box 3
e3 = tk.Entry(root)
e3.pack()

# label 4
t4 = tk.Label(root,text = "Enter distance swam for workout 4")
t4.pack()

#text box 4
e4 = tk.Entry(root)
e4.pack()

# label 5
t5 = tk.Label(root,text = "Enter distance swam for workout 5")
t5.pack()

#text box 3
e5 = tk.Entry(root)
e5.pack()

# label 6
t6 = tk.Label(root,text = "Enter distance swam for workout 6")
t6.pack()

#text box 6
e6 = tk.Entry(root)
e6.pack()

# label 7
t7 = tk.Label(root,text = "Enter distance swam for workout 7")
t7.pack()

#text box 3
e7 = tk.Entry(root)
e7.pack()



#choose unit
for r in range(0,len(MODES),1):
	rbtn = tk.Radiobutton(root,text = MODES[r][0],variable = v, value=MODES[r][1])
	rbtn.pack()

#submit button
btn = tk.Button(root,text = "Submit", command = submit)
btn.pack()



root.mainloop()