from struct import pack
import tkinter as tk

r = tk.Tk()
r.title("TO DO LIST")
r.config(bg="blue")
r.geometry("400x500")

up = False

def update():
    outputvar.set("")

def addlistbar():
    global up
    if inputvar.get() == "":
        outputvar.set("Input Bar Is Empty")
    else:
        if up:
            selected = lb.curselection()
            if selected and inputvar.get() not in lb.get(0, "end"):
                lb.delete(selected[0])
                lb.insert(selected[0], inputvar.get())
                up = False
                outputvar.set("Task Updated Successfully")
            else:
                up = False
                addlistbar()
        else:
            l = lb.get(0, "end")
            if inputvar.get() not in l:
                lb.insert("end", inputvar.get())
                outputvar.set("Task Added Successfully")
            else:
                outputvar.set("Task Already Exist")
    inputvar.set("")
    lb.selection_clear(0, "end")
    r.after(1500, update)

def updatelistbar():
    global up
    l = lb.get(0, "end")
    if not l:
        outputvar.set("List Is Empty")
    else:
        selected = lb.curselection()
        if selected:
            inputvar.set(lb.get(selected[0]))
            up = True
        else:
            outputvar.set("No Task Selected")
    r.after(1500, update)

def deletelistitem():
    s = lb.get(0, "end")
    if not s:
        outputvar.set("List Is Empty")
    else:
        selected = lb.curselection()
        if selected:
            lb.delete(selected[0])
            outputvar.set("Deleted Successfully")
        else:
            outputvar.set("No Task Selected")
    r.after(1500, update)

def click(event):
    if event.widget.cget("text") == "CREATE":
        addlistbar()
    elif event.widget.cget("text") == "UPDATE":
        updatelistbar()
    else:
        deletelistitem()

Heading = tk.Label(r, text="TO DO LIST", fg="white", bg="blue", font=("Arial", 20, "italic", "bold"), pady=15)
Heading.pack()

f1 = tk.Frame(r)
f1.pack(fill="x", pady=5)
sb = tk.Scrollbar(f1)
sb.pack(side="right", fill="y")

lb = tk.Listbox(f1, height=5, width=50, yscrollcommand=sb.set)
lb.pack(fill="x")
sb.config(command=lb.yview)

f2 = tk.Frame(r, bg="blue")
f2.pack()

inputvar = tk.StringVar()
inputlabel = tk.Label(f2, text="Input Task", bg="blue", fg="white", font=("Ariel", 13), padx=10)
inputlabel.grid(row=0, column=0)
inputentry = tk.Entry(f2, font=("Ariel", 15, "bold"), textvariable=inputvar)
inputentry.grid(row=0, column=1, pady=5)

outputvar = tk.StringVar()
outputentry = tk.Entry(f2, state="readonly", width=25, justify="center", bg="black", fg="darkgrey", font=("Ariel", 15, "bold"), textvariable=outputvar)
outputentry.grid(row=1, column=1)

f3 = tk.Frame(r, bg="blue")
f3.pack(pady=50)

button = tk.Button(f3, text="CREATE", width=20, fg="white", bg="grey", padx=10)
button.grid(row=0, column=0, pady=10)
button.bind("<Button-1>", click)

button = tk.Button(f3, text="UPDATE", width=20, fg="white", bg="grey", padx=10)
button.grid(row=2, column=0, pady=10)
button.bind("<Button-1>", click)

button = tk.Button(f3, text="DELETE", width=20, fg="white", bg="grey", padx=10)
button.grid(row=3, column=0, pady=10)
button.bind("<Button-1>", click)

button = tk.Button(f3, text="QUIT", width=20, fg="white", bg="grey", padx=10, command=quit)
button.grid(row=4, column=0, pady=10)

r.mainloop()
