import random
import tkinter as tk

root = tk.Tk()


def getDigits(num):
    return [int(i) for i in str(num)]


def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


def randomNums():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num


def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i, j in zip(num_li, guess_li):

        # common digit present
        if j in num_li:

            # common digit exact match
            if j == i:
                bull_cow[0] += 1

            # common digit match but in wrong position
            else:
                bull_cow[1] += 1

    return bull_cow


def canvas(letter):
    label = tk.Label(root, text=letter, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label)


def main():
    userInput = entry1.get()
    bull_cow = numOfBullsCows(computerGuess, userInput)
    a = "Invalid input"
    b = f"{bull_cow[0]} bulls, {bull_cow[1]} cows"
    c = "You guessed right!"
    if noDuplicates(userInput) is False:
        canvas(a)
    else:
        canvas(b)

    if bull_cow[0] == 4:
        canvas(c)


computerGuess = randomNums()


# Creating the canvas
canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

# Creating the bigger title
label1 = tk.Label(root, text='Guess My 4 Digit Number')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

# Creating a text over the input box
label2 = tk.Label(root, text='Type your Number:')
label2.config(font=('helvetica', 12))
canvas1.create_window(200, 100, window=label2)

# Creating the input box
entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

# Creating a button
button1 = tk.Button(text='Guess', command=main)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
