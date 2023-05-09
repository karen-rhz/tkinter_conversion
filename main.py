import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=200)
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

label_4 = tkinter.Label(text="", font=("Space Mono", 24))
label_4.grid(column=2, row=3)


# Button
def convert_km():
    result = round(int(user_input.get()) / 1.609)
    label_4["text"] = f"{result} Miles"


button = tkinter.Button(text="Convert", command=convert_km)
button.grid(column=3, row=2)

window.mainloop()