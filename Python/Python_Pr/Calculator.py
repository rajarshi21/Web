import tkinter as tk

ele = []

# Create the main window.
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

# Create a text box
text_box = tk.Text(root, height=2, width=30)
text_box.tag_configure("center", justify="center")
text_box.pack()


def button_click(button_number):
    """A simple function to be called when a button is clicked."""
    print_text(button_number)

    if button_number == 'AC':
        text_box.delete("1.0", "end")
        ele.clear()
    elif button_number in ['CE', '%']:
        pass
    else:
        if button_number == '=':
            result()
        else:
            ele.append(button_number)


def print_text(s):
    text_box.insert("end", s, "left")


def result():
    # Calculates final result
    s = ''
    for item in ele:
        s += item

    ele.clear()

    # Set result to the text box
    text_box.delete("1.0", "end")
    text_box.insert("end", eval(s), "left")

    # Get the text from the text box
    s = text_box.get("1.0", "end-1c")
    ele.append(s)


# Frame 1
horizontal_frame1 = tk.Frame(root)
horizontal_frame1.pack(pady=10)  # Pack the frame itself

button = tk.Button(horizontal_frame1, text="AC", command=lambda: button_click('AC'))
button.pack(side=tk.LEFT, padx=20)

button = tk.Button(horizontal_frame1, text="CE", command=lambda: button_click('CE'))
button.pack(side=tk.LEFT, padx=20)

button = tk.Button(horizontal_frame1, text="%", command=lambda: button_click('%'))
button.pack(side=tk.LEFT, padx=20)  # Use side=tk.LEFT for horizontal arrangement

button = tk.Button(horizontal_frame1, text="/", command=lambda: button_click('/'))
button.pack(side=tk.LEFT, padx=20)  # Use side=tk.LEFT for horizontal arrangement

# Frame 2
horizontal_frame2 = tk.Frame(root)
horizontal_frame2.pack(pady=10)  # Pack the frame itself

# Create and pack buttons horizontally within the frame
button = tk.Button(horizontal_frame2, text="7", command=lambda: button_click('7'))
button.pack(side=tk.LEFT, padx=20)  # Use side=tk.LEFT for horizontal arrangement

button = tk.Button(horizontal_frame2, text="8", command=lambda: button_click('8'))
button.pack(side=tk.LEFT, padx=20)

button = tk.Button(horizontal_frame2, text="9", command=lambda: button_click('9'))
button.pack(side=tk.LEFT, padx=20)

button = tk.Button(horizontal_frame2, text="x", command=lambda: button_click('*'))
button.pack(side=tk.LEFT, padx=20)

# Frame 3
horizontal_frame3 = tk.Frame(root)
horizontal_frame3.pack(pady=10)  # Pack the frame itself

# Create and pack buttons horizontally within the frame
button = tk.Button(horizontal_frame3, text="4", command=lambda: button_click('4'))
button.pack(side=tk.LEFT, padx=20)  # Use side=tk.LEFT for horizontal arrangement

button = tk.Button(horizontal_frame3, text="5", command=lambda: button_click('5'))
button.pack(side=tk.LEFT, padx=20)

button = tk.Button(horizontal_frame3, text="6", command=lambda: button_click('6'))
button.pack(side=tk.LEFT, padx=20)

button = tk.Button(horizontal_frame3, text="-", command=lambda: button_click('-'))
button.pack(side=tk.LEFT, padx=20)

# Frame 4
horizontal_frame4 = tk.Frame(root)
horizontal_frame4.pack(pady=10)  # Pack the frame itself

# Create and pack buttons horizontally within the frame
button = tk.Button(horizontal_frame4, text="1", command=lambda: button_click('1'))
button.pack(side=tk.LEFT, padx=20)  # Use side=tk.LEFT for horizontal arrangement

button = tk.Button(horizontal_frame4, text="2", command=lambda: button_click('2'))
button.pack(side=tk.LEFT, padx=20)

button = tk.Button(horizontal_frame4, text="3", command=lambda: button_click('3'))
button.pack(side=tk.LEFT, padx=20)

button = tk.Button(horizontal_frame4, text="+", command=lambda: button_click('+'))
button.pack(side=tk.LEFT, padx=20)

# Frame 5
horizontal_frame5 = tk.Frame(root)
horizontal_frame5.pack(pady=10)  # Pack the frame itself

# Create and pack buttons horizontally within the frame
button = tk.Button(horizontal_frame5, text="0", command=lambda: button_click('0'))
button.pack(side=tk.LEFT, padx=20)

button = tk.Button(horizontal_frame5, text=".", command=lambda: button_click('.'))
button.pack(side=tk.LEFT, padx=20)

button = tk.Button(horizontal_frame5, text="(", command=lambda: button_click('('))
button.pack(side=tk.LEFT, padx=20)  # Use side=tk.LEFT for horizontal arrangement
button = tk.Button(horizontal_frame5, text=")", command=lambda: button_click(')'))
button.pack(side=tk.LEFT, padx=20)  # Use side=tk.LEFT for horizontal arrangement

# Frame 6
horizontal_frame6 = tk.Frame(root)
horizontal_frame6.pack(pady=10)  # Pack the frame itself

button = tk.Button(horizontal_frame6, text="=", command=lambda: button_click('='), width=20)
button.pack(side=tk.LEFT, padx=20)



# Start the Tkinter event loop
root.mainloop()
