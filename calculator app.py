import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.set(result)
        except:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    else:
        entry.set(entry.get() + text)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.StringVar()
entry_field = tk.Entry(root, textvar=entry, font="Arial 20")
entry_field.pack(fill=tk.BOTH, ipadx=8)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 20", width=4, height=2)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)
    frame.pack()

root.mainloop()
