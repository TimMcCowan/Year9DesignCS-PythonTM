import tkinter as tk

root = tk.Tk()

def submit ():
	print(v.get())



MODES = [
("why", "why"),
("am","am"),
("I","I"),
("like","like"),
("this","this")]

v = tk.StringVar()

v.set("A")

Gartext =( "┈┈┈┈╱▔╲▂▂╱▔╲┈┈┈┈\n"
"┈┈┈▕╮╱▔╲╱▔╲╭▏┈┈┈\n"
"┈┈┈╱╋▏┊▕┊┊▕╋╲┈┈┈\n"
"┈┈▕╋▕━▅━━▅━▏╋▏┈┈\n"
"┈┈▕╱▔╲▔╭╮▔╱▔╲▏┈┈\n"
"┈┈▕┊┳┊▔╰╯▔┊┳┊▏┈┈\n"
"┈┈┈╲╰━━╯╰━━╯╱┈┈┈\n"
"┈┈┈╱▔╭┈┈┈┈╮▔╲┈┈┈\n"
"┈┈╱▕┊┊┈┈┈┈┊┊▏╲┈┈\n"
"┈┈╲╱┊┊┈┈┈┈┊┊╲╱┈┈\n"
"┈┈┈▏╋┊┈┈┈┈┊╋▕┈┈┈\n"
"┈┈┈╲╋╰┈┈┈┈╯╋╱┈┈┈\n"
"╱▔╲┈╲╋╭▂▂╮╋╱┈┈┈┈\n"
"▏╋▕▂╱▏┊▏▕┊▕┈┈┈┈┈\n"
"╲▂▂▂╱▏┊▏▕┊▕┈┈┈┈┈\n"
"┈┈╱▔▔┈╯╲╱╰┈▔▔╲┈┈\n"
"┈┈╲▂▂▂▂╱╲▂▂▂▂╱\n"
"M O N D A Y S")


Gar = tk.Text(root, width = 30, height = 20, borderwidth = 3, relief = tk.GROOVE, bg = 'yellow')
Gar.insert(tk.INSERT,Gartext)
Gar.config(state ="disabled")
Gar.pack()

for r in range(0,len(MODES),1):
	b = tk.Radiobutton(root, text = MODES[r][0], variable = v, value = MODES[r][1],command = submit)
	b.pack(anchor=tk.W)

root.mainloop()
