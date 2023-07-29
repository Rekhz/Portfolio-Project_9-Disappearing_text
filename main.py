
from tkinter import *
window = Tk()
window.title("Disappearing Text")
warning_Label=Label(text="Continue writing without interruption. If you halt your text, it will vanish in 5 seconds.",font=("helvetica", 10, "bold"),  fg="green")
warning_Label.pack(padx=10,pady=10,)

text_box = Text( height=10, width=50)
text_box.pack(padx=10, pady=10)
count_down_label=Label(text="Count Down will start once you stop typing",font=("helvetica", 10, "bold"),  fg="red")

count_down_label.pack(padx=10,pady=10)
count_down_count = 5
started_writing=False

def timer_control():
    global count_down_count
    count_down_count=5
    count_down_label.config(text="Count Down will start once you stop typing", font=("helvetica", 10, "bold"),
                            fg="red")

def on_keypress(event):
    global started_writing

    if started_writing:
        timer_control()
    else:
        started_writing= True
        countdown()

def countdown():
    global started_writing,count_down_count

    if started_writing:
        count_down_label.config(text=count_down_count)
        count_down_count -= 1
        if count_down_count <= 0:
            hide_text()
            started_writing = False
        window.after(1000, countdown)

def hide_text():
    global started_writing
    started_writing = False
    count_down_label.config(text="Your time has ended")

    text_box.delete("1.0", END)
    timer_control()

text_box.bind("<Key>", on_keypress)
window.mainloop()



