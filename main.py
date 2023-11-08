from tkinter import *
window = Tk()
window.title("Добро пожаловать в игру покер")
window.mainloop()


import random

suits = ["Черви", "Пики", "Бубны", "Крести"]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

player_1 = [random.choice(ranks) + " " + random.choice(suits) for _ in range(5)]
player_2 = [random.choice(ranks) + " " + random.choice(suits) for _ in range(5)]

print("Игрок_1:")
for card in player_1:
    print(card)

print("\nИгрок_2:")
for card in player_2:
    print(card)