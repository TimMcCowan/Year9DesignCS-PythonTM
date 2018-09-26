import tkinter as tk

def submit():

	print("submit pressed")

root = tk.Tk()
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()
 
enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="submit", command=submit )
btn.pack()

output = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief = tk.GROOVE)
outfit.config(state ="disabled")
output.pack()





root.mainloop()