from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/german words.csv")

data_list = df.to_dict(orient="records")


def gen_new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_list)
    canvas.itemconfig(title, text="German", fill="black")
    canvas.itemconfig(word, text=current_card["German"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def remove_word():
    data_list.remove(current_card)
    dataframe = pandas.DataFrame(data_list)
    dataframe.to_csv("data/words_to_learn.csv", index=False)
    gen_new_word()


window = Tk()
window.title("FLASHY")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")


canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 143, text="German", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


r_button = Button(image=right, highlightthickness=0, command=remove_word)
r_button.grid(column=1, row=1)

w_button = Button(image=wrong, highlightthickness=0, command=gen_new_word)
w_button.grid(column=0, row=1)

gen_new_word()

window.mainloop()
