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
	b =0
	for i in range(len(list1)-1):
		list1[i] = int(list1[i])
		a += list1[i]
	
	
	u = v.get()

	if u == "Meters" and a >=1000:
		u = "Kilometers"
		a = a/1000	

	if u == "Yards" and a>=1760:
		u = "Miles"
		a = a/1760
	b = a/(len(list1)-1)
	print("user selected: " +var.get())
	print("your average distance per workout was: {0} " .format(b) +" "+ u )
	outpt.delete("1.0",tk.END)
	outpt.insert(tk.END, "average = \n {0} " .format(b)+" "+u)
	

	outpt1.delete("1.0", tk.END)
	outpt1.insert(tk.END,"total = \n"+str(a) +" "+ u)
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
#font
f = 1

def fontup(*args):
	global f
	f = f+1
	a = f
	fontsize3.configure(text=f)

	user.configure(font=f)
	dist.configure(font=f)
	rbtn.configure(font=f)
	smbtn.configure(font=f)
	outpt.configure(font=f)
	fontsize1.configure(font=f)
	fontsize2.configure(font=f)
	fontsize3.configure(font=f)

def fontdown(*args):
	global f
	f = f-1
	fontsize3.configure(text=f)

	user.configure(font=f)
	dist.configure(font=f)
	rbtn.configure(font=f)
	smbtn.configure(font=f)
	outpt.configure(font=f)
	fontsize1.configure(font=f)
	fontsize2.configure(font=f)
	fontsize3.configure(font=f)



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

outpt = tk.Text(root, height = 2, width = 15,background = "light grey",font = f)
outpt.grid(column = 0, row = 6)


outpt1 = tk.Text(root, height = 2, width = 15,background = "light grey")
outpt1.grid(column = 1, row = 6)

fontsizeL = tk.Label(root, text = "Accesibility: Font size")
fontsize1 = tk.Button(root, command=lambda: fontdown(),background = "light grey", text = "-") 
fontsize3 = tk.Label(root, text=str(f))
fontsize2 = tk.Button(root, command =lambda: fontup(),background = "light grey", text = "+")


fontsizeL.grid(column = 1, row = 7)
fontsize1.grid(column = 0, row  =8)
fontsize3.grid(column = 1,row = 8)
fontsize2.grid(column = 2, row =8) 



root.mainloop()