from tkinter import *

count = 10
colours = ['black', 'red', 'yellow', 'green']
action = ['STOP', 'READY', 'GO']

r = 0
Sec = 0


def countdown(count):
    # change text in label
    label_time['text'] = count
    if count == 0:
        count += 15

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count - 1)

    if -1 < count < 6 or -6 < count < 0:
        label_stop_text["bg"] = "red"
        label_ready_text["bg"] = "grey"
        label_go_text["bg"] = "grey"
    if 5 < count < 10 or -11 < count < -5:
        label_ready_text["bg"] = "yellow"
        label_go_text["bg"] = "grey"
        label_stop_text["bg"] = "grey"
    if count > 10 or -16 < count < -10:
        label_go_text["bg"] = "green"
        label_stop_text["bg"] = "grey"
        label_ready_text["bg"] = "grey"


root = Tk()
# Time lable and text
label = Label(root)
label.grid(row=0, column=0)
label["text"] = "Time"
label["relief"] = "ridge"
label["width"] = 15

label_time = Label(root)
label_time.grid(row=0, column=1)
label_time["relief"] = "ridge"
label_time["width"] = 15
label_time["bg"] = "grey"

# Go lable and text
label_go = Label(root)
label_go.grid(row=1, column=0)
label_go["text"] = "GO"
label_go["relief"] = "ridge"
label_go["width"] = 15

label_go_text = Label(root)
label_go_text.grid(row=1, column=1)
label_go_text["relief"] = "ridge"
label_go_text["width"] = 15
label_go_text["bg"] = "grey"

# Ready lable and text
label_ready = Label(root)
label_ready.grid(row=2, column=0)
label_ready["text"] = "READY"
label_ready["relief"] = "ridge"
label_ready["width"] = 15

label_ready_text = Label(root)
label_ready_text.grid(row=2, column=1)
label_ready_text["relief"] = "ridge"
label_ready_text["width"] = 15
label_ready_text["bg"] = "grey"

# Stop lable and text
label_stop = Label(root)
label_stop.grid(row=3, column=0)
label_stop["text"] = "STOP"
label_stop["relief"] = "ridge"
label_stop["width"] = 15

label_stop_text = Label(root)
label_stop_text.grid(row=3, column=1)
label_stop_text["relief"] = "ridge"
label_stop_text["width"] = 15
label_stop_text["bg"] = "grey"

countdown(15)


# for i in range(0,3):
#     Label(text=action[r], relief=RIDGE,width=15).grid(row=r,column=0)
#     Entry(bg=colours[r], relief=SUNKEN,width=10).grid(row=r,column=1)
#     r += 1

mainloop()
