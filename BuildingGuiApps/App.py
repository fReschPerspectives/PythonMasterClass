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
main_window.geometry("640x480+80+80")

label = tkinter.Label(main_window, text="Hello World")
label.pack(side='top')

left_frame = tkinter.Frame(main_window)
left_frame.pack(side='left', fill='both', expand=True)

right_frame = tkinter.Frame(main_window)
right_frame.pack(side='right', fill='both', expand=True)

canvas = tkinter.Canvas(right_frame, relief='raised', borderwidth=1, highlightthickness=0)
canvas.pack(side='top', fill=tkinter.BOTH, expand=True)

button1 = tkinter.Button(left_frame, text="Button 1")
button2 = tkinter.Button(left_frame, text="Button 2")
button3 = tkinter.Button(left_frame, text="Button 3")

button1.pack(side="top", anchor="nw", expand=False)
button2.pack(side="top", anchor="sw", expand=False)
button3.pack(side="top", anchor="w", expand=False)

main_window.mainloop()