import tkinter as tk
import math

def startup():

	ctr1 = wkt.get()
	ctr1 = int(ctr1) #cast that to an int
	
	#This is a list that can hold many label
	tlist = [] 
	
	#Create a list of entry box
	
	for i in range(0,ctr1,1):
 
 		#creating a lable object and we adding it to the list
		tlist.append(tk.Label(root,text = "Enter distance swam for workout "+str(i + 1),bg = 'blue'))
				
		tlist[i].pack()

		#When you create an entry box append it to the list. 
		e1 = tk.Entry(root)
		e1.pack()
	for r in range(0,len(MODES),1):
		rbtn = tk.Radiobutton(root,text = MODES[r][0],variable = v, value=MODES[r][1],bg = 'gray')
		rbtn.pack()
	#submit button
	btn = tk.Button(root,text = "Submit", command = submit,bg = 'gray',borderwidth = 0.001,)
	btn.pack()




def submit():


	
	
	d1 = int(e1.get())

	d2 = int(e1.get())

	d3 = int(e1.get())

	d4 = int(e1.get())

	d5 = int(e1.get())

	d6 = int(e1.get())

	d7 = int(e1.get())

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

ctr = 1

#workout numbers (IN PROGRESS)
wktn = tk.Label(root, text = "Enter Number of workouts")
wktn.pack()

wkt = tk.Entry(root)
wkt.pack()

#submit button
btn = tk.Button(root,text = "Submit", command = startup,bg = 'gray',borderwidth = 0.001,)
btn.pack()

v = tk.StringVar()
v.set("A")

# workout numbers (WIP)




#choose unit




root.mainloop()