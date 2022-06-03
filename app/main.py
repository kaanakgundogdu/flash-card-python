from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
current_card = NONE
flip_timer = NONE


try:
    data = pandas.read_csv("app/data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("app/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def pressed_correct_buton():
    if len(to_learn) > 0:
        to_learn.remove(current_card)

    new_data = pandas.DataFrame(to_learn)

    new_data.to_csv("app/data/words_to_learn.csv")

    pick_random_french_word()


def pick_random_french_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_image, image=card_front_image)

    if len(to_learn) > 0:
        current_card = random.choice(to_learn)
    else:
        canvas.itemconfig(title_text, text="Congrats", fill="black")
        canvas.itemconfig(
            word_text, text="You know all words", fill="black")

        return

    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


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


wrong_button = Button(
    image=wrong_image, highlightthickness=0, command=pick_random_french_word)
wrong_button.grid(column=0, row=1)
right__button = Button(
    image=right_image, highlightthickness=0, command=pressed_correct_buton)
right__button.grid(column=1, row=1)

pick_random_french_word()

window.mainloop()
