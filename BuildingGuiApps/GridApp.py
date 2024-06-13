try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

#tkinter._test()

# Create a window!
main_window = tkinter.Tk()
main_window.title("Hello World")
main_window.geometry("640x480-8-200")

label = tkinter.Label(main_window, text="Hello World")
label.grid(row=0, column=0)

left_frame = tkinter.Frame(main_window)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=1, highlightthickness=0)
canvas.grid(row=1, column=0)

right_frame = tkinter.Frame(main_window)
right_frame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(right_frame, text="Button 1")
button2 = tkinter.Button(right_frame, text="Button 2")
button3 = tkinter.Button(right_frame, text="Button 3")

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# Configure the columns
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)

main_window.mainloop()