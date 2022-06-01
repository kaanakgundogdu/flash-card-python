from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("FLASH CARD")
window.config(padx=50, pady=50, bg="#b1ddc6")
canvas = Canvas(width=800, height=526)


card_back_image = PhotoImage(file="app/images/card_back.png")
card_front_image = PhotoImage(file="app/images/card_front.png")
right_image = PhotoImage(file="app/images/right.png")
wrong_image = PhotoImage(file="app/images/wrong.png")

canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "italic"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)
right__button = Button(image=right_image, highlightthickness=0)
right__button.grid(column=1, row=1)

window.mainloop()
