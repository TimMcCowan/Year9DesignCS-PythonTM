import tkinter as tk
import math

def submit():
	d1 = int(e1.get())

	d2 = int(e2.get())

	d3 = int(e3.get())

	d4 = int(e4.get())

	d5 = int(e5.get())

	d6 = int(e6.get())

	d7 = int(e7.get())

	ttl =d1 +d2 + d3+d4+d5+d6+d7

	u = str(v.get())
	if u == "Meters" and ttl >1000:
		u = "Kilometers"
		ttl = ttl/1000	

	if u == "Yards" and ttl>1760:
		u = "Miles"
		ttl = ttl/1760

	ttl = round(ttl,2)
	print("You swam " +str(ttl)+" " +str(u)+" this week")



root = tk.Tk()


root.configure(bg='blue')
#radio button options
MODES = [
("Meters", "Meters"),
("Yards", "Yards"),
]

v = tk.StringVar()
v.set("A")

#label 1
t1 = tk.Label(root,text = "Enter distance swam for workout 1",bg = 'blue')
t1.pack()

#text box 1 
e1 = tk.Entry(root)
e1.pack()

# label 2
t2 = tk.Label(root,text = "Enter distance swam for workout 2",bg = 'blue')
t2.pack()

#text box 2 
e2 = tk.Entry(root)
e2.pack()

# label 3
t3 = tk.Label(root,text = "Enter distance swam for workout 3",bg = 'blue')
t3.pack()

#text box 3
e3 = tk.Entry(root)
e3.pack()

# label 4
t4 = tk.Label(root,text = "Enter distance swam for workout 4",bg = 'blue')
t4.pack()

#text box 4
e4 = tk.Entry(root)
e4.pack()

# label 5
t5 = tk.Label(root,text = "Enter distance swam for workout 5",bg = 'blue')
t5.pack()

#text box 5
e5 = tk.Entry(root)
e5.pack()

# label 6
t6 = tk.Label(root,text = "Enter distance swam for workout 6",bg = 'blue')
t6.pack()

#text box 6
e6 = tk.Entry(root)
e6.pack()

# label 7
t7 = tk.Label(root,text = "Enter distance swam for workout 7",bg = 'blue')
t7.pack()

#text box 7
e7 = tk.Entry(root)
e7.pack()



#choose unit
for r in range(0,len(MODES),1):
	rbtn = tk.Radiobutton(root,text = MODES[r][0],variable = v, value=MODES[r][1],bg = 'gray')
	rbtn.pack()

#submit button
btn = tk.Button(root,text = "Submit", command = submit,bg = 'gray',borderwidth = 0.001,)
btn.pack()



root.mainloop()