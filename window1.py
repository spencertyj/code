import tkinter as tk

root = tk.Tk()
root.title("Buttons & Display")
title_label = tk.Label(root, text="Hello, Tkinter!", font=("Ariel", 18))
title_label.pack(pady=10)
name_label = tk.Label(root, text="Your name:")
name_label.pack()
name_entry = tk.Entry(root, width=25)
name_entry.pack(pady=5)
def say_hello():
    name = name_entry.get().strip()
    if name:
        title_label.config(text=f"Hello, {name}!")
    else:
        title_label.config(text="Hello, Tkinter!")
hello_btn = tk.Button(root, text="Say Hello", command=say_hello)
hello_btn.pack(pady=5)
clicks = tk.IntVar(value=0)

def count_click():
    clicks.set(clicks.get() + 1)
    counter_label.config(text=f"Clicks: {clicks.get()}")

click_btn = tk.Button(root, text="+1 Click", command=count_click)
click_btn.pack(pady=5)
counter_label = tk.Label(root,text= " Clicks: 0")
counter_label.pack()

def reset_all():
    name_entry.delete(0, tk.END)
    title_label.config(text="Hello, Tkinter")
    clicks.set(0)
    counter_label.config(text="Clicks : 0")

reset_btn = tk.Button(root, text="Reset", command=reset_all)
reset_btn.pack(pady=5)
root.mainloop()