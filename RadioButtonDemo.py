import tkinter as tk

def change():
	print("change")
	print(v.get()) #Accesses element associated with MODES

root = tk.Tk()

#The below variable is called a 2D list.  This is a DATA STRUCTURE
#A DATA STRUCTURE is a way to group data in a logical way so the 
#programmer can access information.  
MODES = [
("Monochrome", "1"),
("Grayscale", "L"),
("True color", "RGB"),
("Color separation", "CMYK"),
]
#We access 2D lists using a [row][col] notation.  You can visualize teh
#MODES as

#		0				1		
# 0	Monochrome			1
# 1 Grayscale			L
# 2 True color 	   		RGB
# 3 Color separation	CMYK
v = tk.StringVar() #v keeps track of which button is selected. 
v.set("L") # initialize

#We need to add each of the elements in the MODES data structure
#to the radio button b.  We use a for loop to do this. 

# We have used a short hand to loop through Modes
# for text, mode in MODES:
#	b = tk.Radiobutton(root, text=text, variable=v, value=mode, command = change)
#	b.pack(anchor=tk.W)

# For now I prefer to understand the long format to appreciate the 2D
# structure
for r in range(0,len(MODES),1):
	b = tk.Radiobutton(root, text=MODES[r][0], variable=v, value=MODES[r][1], command = change)
	b.pack(anchor=tk.W)


root.mainloop()