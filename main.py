import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(500, 500)
window.config(padx=20, pady=20)

# Label : text in the window
label_1 = tkinter.Label(text="Convert Miles to Km", font=("Space Mono", 24))
label_1.grid(column=1, row=1)

# # To change the text on screen
# label_1['text'] = "Another text"
# # or
# label_1.config(text="Another text")

# Entry : Receive input
user_input = tkinter.Entry(width=30)
user_input.grid(column=1, row=2)

label_2 = tkinter.Label(text="Km", font=("Space Mono", 24))
label_2.grid(column=2, row=2)

label_3 = tkinter.Label(text="is equal to", font=("Space Mono", 24))
label_3.grid(column=1, row=3)

label_4 = tkinter.Label(text="RESULT", font=("Space Mono", 24))
label_4.grid(column=1, row=4)

label_5 = tkinter.Label(text="Miles", font=("Space Mono", 24))
label_5.grid(column=2, row=4)


# Button

window.mainloop()