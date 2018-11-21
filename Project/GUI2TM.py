#importing tkinter tool box which includes GUI elements

import tkinter as tk



root = tk.Tk()


titleLabel = tk.Label(root, text = "L I F E  I S  M E A N I  N G L E S S", font = ("Comic Sans MS",16))
titleLabel.pack()

titleLabel.grid(row = 0, column = 0, columnspan = 2)

output = tk.Text(root,height = 10, width  = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)

word1Label = tk.Label(root,text = "Word 1", background = 'red', foreground = 'blue')
word1Label.grid(row =2,column = 0)

word2Label = tk.Label(root,text = "Word 2", background = 'red', foreground = 'blue')
word2Label.grid(row =3,column = 0)

word3Label = tk.Label(root,text = "Word 3", background = 'red', foreground = 'blue')
word3Label.grid(row =4,column = 0)


word1Entry = tk.Entry(root)
word1Entry.grid(row = 2, column = 1)

word2Entry = tk.Entry(root)
word2Entry.grid(row = 3, column = 1)

word3Entry = tk.Entry(root)
word3Entry.grid(row = 4, column = 1)

GoBtn = tk.Button(root, text = "GO!")
GoBtn.grid(row = 5, column = 1)
# this is an event driven program
#build GUI
#start the program
#waiting for event
root.mainloop()