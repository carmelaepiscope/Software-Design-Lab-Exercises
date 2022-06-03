import tkinter as tk
from datetime import datetime
from contextlib import contextmanager

@contextmanager
def preserve_insert_cursor(text):

    saved_insert = text.index("insert")
    yield
    text.mark_set("insert", saved_insert)

def change_age():

    with preserve_insert_cursor(text):
        text.delete("3.5", "3.0 lineend")
        text.insert("3.5", "30")

def update_time():
    with preserve_insert_cursor(text):

        now = datetime.now()
        timestring = now.strftime("%H:%M:%S")

        ranges = list(text.tag_ranges("time"))
        while ranges:
            start = ranges.pop(0)
            end = ranges.pop(0)
            text.delete(start, end)
            text.insert(start, timestring, "time")

    text.after(1000, update_time)

root  = tk.Tk()
header = tk.Frame(root, bd=1, relief="raised")
text = tk.Text(root)
header.pack(side="top", fill="x")
text.pack(fill="both", expand=True)

button = tk.Button(header, text="Button", command=change_age)
button.pack(side="right", padx=10)

text.insert("end", "Time: ", "", "<time>", "time", "\n")

text.insert("end", "Name: Ma. Carmela P. Episcope \n")
text.insert("end", "Age: 20\n")
text.insert("end", "Gender: Female\n")
text.insert("end", "Course: BS Computer Engineering\n")

update_time()

root.mainloop()