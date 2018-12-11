import tkinter as tk
import math


#user selected
def user(*args):
	print("user selected:"+var.get())


#average
def submit(*args):
	print("Submit")
	#Step 1: 
	#Take everything from the text box THE USER MUST HIT ENTER AFTER EACH ENTRY
	val = distT.get("1.0",tk.END)

	#Step 2: Remove all of the spaces form val
	print(val)
	list1 = val.split("\n") #Turns it into a list, separating on the \n a new line

	#print(list1)
	
	a = 0
	for i in range(len(list1)-1):
		list1[i] = int(list1[i])
		a += list1[i]
	
	b = a/len(list1)
	print("user selected: " +var.get())
	print("your average distance per workout was: {0} " .format(b) + v.get() )
	outpt.delete("1.0",tk.END)
	outpt.insert(tk.END, "average = "+str(round(b,2)))
	

	outpt1.delete("1.0", tk.END)
	outpt1.insert(tk.END,"total = "+str(a))
	#UPDATE OUR DATA LISTS
	#I have multiple entries per submit
	#Step 3: 
	#Check the last elemet of list to ensure it is NOT a '' - does this as long as it is true
	while list1[len(list1) - 1] == '':
		list1.pop(len(list1) - 1) #removes the last element

	
	#Step 4: Update everything

	for i in range(0, len(list1),1):
		userList.append(var.get())
		unitsList.append(list1[i])
		#distanceList.append()


#Variables that store information
#User
userList = []
unitsList = []
distanceList = [] 

root = tk.Tk()

MODES = [
("Meters", "Meters"),
("Yards", "Yards"),
]


DDM = ["Tim","John","Jack"]

var = tk.StringVar(root)
var.set(DDM[0])
var.trace("w",user)


# workout text
#wrkt = tk.Label(root, text= "Type in number of workouts")
#wrkt.grid(column = 0, row  = 0)

#wrktT = tk.Text(root, bg = 'grey', height = 1, width = 3)
#wrktT.grid(column = 0, row = 1)


#Dropdown menu
user = tk.Label(root,text = "User")
user.grid(column = 1, row = 0,columnspan = 2)

userT = tk.OptionMenu(root,var,DDM[0],DDM[1],DDM[2])
userT.grid(column = 1, row = 1, columnspan = 2)


#Distance text
dist = tk.Label(root, text ="distance")
dist.grid(column = 0, row = 2)

distT = tk.Text(root,bg = 'grey', height = 10, width = 5)
distT.grid(column = 0, row = 3 )




v = tk.StringVar()
v.set(MODES[0][0])


#RADIO BUTTONS
for r in range(0,len(MODES),1):
		rbtn = tk.Radiobutton(root,text = MODES[r][0],variable = v, value=MODES[r][1])
		rbtn.grid(column = 2, row = r+4)
		#rbtn2 = tk.Radiobutton(root,variable = v, value=MODES[r][1], text = "Meters")
		#rbtn2.grid(column = 2,row  = 5)

smbtn = tk.Button(root, text = "Submit!", command = submit)
smbtn.grid(row = 4, column = 1,rowspan = 2)

outpt = tk.Text(root, height = 2, width = 10,background = "light grey")
outpt.grid(column = 0, row = 6)


outpt1 = tk.Text(root, height = 2, width = 10,background = "light grey")
outpt1.grid(column = 1, row = 6)



root.mainloop()