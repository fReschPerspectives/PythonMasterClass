import os
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

#tkinter._test()

# Create a window!
main_window = tkinter.Tk()
main_window.title("Grid Demo")
main_window.geometry("640x480-8-200")

label = tkinter.Label(main_window, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# Window layout
main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=3)
main_window.rowconfigure(2, weight=0)
main_window.columnconfigure(3, weight=3)
main_window.rowconfigure(3, weight=1)
main_window.columnconfigure(4, weight=3)
main_window.rowconfigure(4, weight=1)
main_window.columnconfigure(5, weight=3)
main_window.rowconfigure(5, weight=2)


# File listbox
file_listbox = tkinter.Listbox(main_window)
file_listbox.grid(row=1, column=1, sticky='nsew', rowspan=2)
file_listbox.config(borderwidth=2, relief='sunken')

for zone in os.listdir('/usr/bin'):
    file_listbox.insert(tkinter.END, zone)

list_scroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL, command=file_listbox.yview)
list_scroll.grid(row=1, column=2, sticky='nsw', rowspan=2)
file_listbox.config(yscrollcommand=list_scroll.set)

# Frame for the button box
option_frame = tkinter.LabelFrame(main_window, text="File Details")
option_frame.grid(row=1, column=3, sticky='new')

rb_value = tkinter.IntVar()
rb_value.set(2)

radiobutton = tkinter.Radiobutton(option_frame, text="File Name", value=1, variable=rb_value)
radiobutton2 = tkinter.Radiobutton(option_frame, text="Path", value=2, variable=rb_value)
radiobutton3 = tkinter.Radiobutton(option_frame, text="Timestamp", value=3, variable=rb_value)

radiobutton.grid(row=0, column=0, sticky='w')
radiobutton2.grid(row=1, column=0, sticky='w')
radiobutton3.grid(row=2, column=0, sticky='w')

# Result window
result_table = tkinter.Label(main_window, text="Result")
result_table.grid(row=2, column=3, sticky='nw')
result = tkinter.Entry(main_window)
result.grid(row=2, column=3, sticky='sew')

# Time frame window
time_frame = tkinter.LabelFrame(main_window, text="Time")
time_frame.grid(row=4, column=1, sticky='new')
time_frame['padx'] = 36

# The time spinners
hour_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=23)
min_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
sec_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)

hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=":").grid(row=0, column=1)
min_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=":").grid(row=0, column=3)
sec_spinner.grid(row=0, column=4)

# Date frame window
date_frame = tkinter.Frame(main_window)
date_frame.grid(row=5, column=1, sticky='new')

# Date labels
day_label = tkinter.Label(date_frame, text="Day")
month_label = tkinter.Label(date_frame, text="Month")
year_label = tkinter.Label(date_frame, text="Year")

day_label.grid(row=0, column=0, sticky='w')
month_label.grid(row=0, column=1, sticky='w')
year_label.grid(row=0, column=2, sticky='w')

day_spinner = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
month_spinner = tkinter.Spinbox(date_frame, width=5, values=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"))
year_spinner = tkinter.Spinbox(date_frame, width=5, from_=2000, to=2024)

day_spinner.grid(column=0, row=1)
month_spinner.grid(column=1, row=1)
year_spinner.grid(column=2, row=1)

# Buttons
ok_button = tkinter.Button(main_window, text="OK")
cancel_button = tkinter.Button(main_window, text="Cancel", command=main_window.quit)

ok_button.grid(row=5, column=4, sticky='e')
cancel_button.grid(row=5, column=5, sticky='w')

main_window.mainloop()