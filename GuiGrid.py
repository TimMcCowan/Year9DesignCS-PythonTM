#importing tk toolbox, for GUI

import tkinter as tk

#root is a variable that holds the information
#about the main window. that is the window
# with the close, min ,max buttons in the top left
#tk.Tk is the tool box and use the function Tk()

root = tk.Tk()

ent =tk.Entry(root)
ent.grid(row = 0, column = 0)


# create button
btn = tk.Button(root, text = "press me")
btn.grid(row = 0, column = 1)

root.mainloop()