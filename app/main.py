from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("app/data/french_words.csv")
to_learn = data.to_dict(orient="records")
card = NONE
flip_timer = NONE
words_to_learn_dict = NONE
words_known = NONE


def pick_random_french_word():
    global card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_image, image=card_front_image)

    card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(word_text, text=card["English"], fill="white")


window = Tk()
window.title("FLASH CARD")
window.config(padx=50, pady=50, bg="#b1ddc6")


card_back_image = PhotoImage(file="app/images/card_back.png")
card_front_image = PhotoImage(file="app/images/card_front.png")
right_image = PhotoImage(file="app/images/right.png")
wrong_image = PhotoImage(file="app/images/wrong.png")

canvas = Canvas(width=800, height=526)

card_image = canvas.create_image(400, 263, image=card_front_image)

title_text = canvas.create_text(
    400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(
    400, 263, text="Word", font=("Arial", 60, "italic"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_button = Button(image=wrong_image, highlightthickness=0,
                      command=pick_random_french_word)
wrong_button.grid(column=0, row=1)
right__button = Button(
    image=right_image, highlightthickness=0, command=pick_random_french_word)
right__button.grid(column=1, row=1)

pick_random_french_word()

window.mainloop()
