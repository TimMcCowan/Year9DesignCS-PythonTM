import tkinter as tk
import math



root = tk.Tk()

MODES = [
("Meters", "Meters"),
("Yards", "Yards"),
]


DDM = ["Tim","John","Jack"]

def user(*args):
	print("user selected:"+var.get())

def submit(*args):
	print(distT.get("1.0",tk.END))	

var = tk.StringVar(root)
var.set(DDM[0])
var.trace("w",user)


# workout text
wrkt = tk.Label(root, text= "Type in number of workouts")
wrkt.grid(column = 0, row  = 0)

wrktT = tk.Text(root, bg = 'grey')
wrktT.grid(column = 0, row = 1)


#Dropdown menu
user = tk.Label(root,text = "User")
user.grid(column = 1, row = 0,columnspan = 2)

userT = tk.OptionMenu(root,var,DDM[0],DDM[1],DDM[2])
userT.grid(column = 1, row = 1, columnspan = 2)


#Distance text
dist = tk.Label(root, text ="distance")
dist.grid(column = 0, row = 2,)

distT = tk.Text(root,bg = 'grey', height = 10)
distT.grid(column = 0, row = 3 )




v = tk.StringVar()



#RADIO BUTTONS
for r in range(0,len(MODES),1):
		rbtn = tk.Radiobutton(root,text = MODES[r][0],variable = v, value=MODES[r][1])
		rbtn.grid(column = 2, row = r+4)
		#rbtn2 = tk.Radiobutton(root,variable = v, value=MODES[r][1], text = "Meters")
		#rbtn2.grid(column = 2,row  = 5)

smbtn = tk.Button(root, text = "Submit!", command = submit)
smbtn.grid(row = 4, column = 1,rowspan = 2)





root.mainloop()