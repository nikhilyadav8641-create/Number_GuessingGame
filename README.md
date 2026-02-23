
# 🎯 Number Guessing Game (Python)

## 📌 Description

This is a simple **number guessing game** built using Python.
The program randomly generates a number between **1 and 100**, and the player tries to guess it.

After each guess, the program gives feedback:

* If the guess is **too low**
* If the guess is **too high**
* If the guess is **correct**

It also counts how many attempts the player makes before guessing the correct number.

---

## 🚀 Features

* Random number generation between 1 and 100
* Continuous guessing using a loop
* Hints for high or low guesses
* Attempt counter
* Stops when the correct number is guessed

---

## 🧰 Requirements

* Python 3.x installed on your system

---

## ▶️ How to Run

1. Copy the code into a Python file (for example: `guess_game.py`)
2. Open terminal or command prompt
3. Run the file:

 python guess_game.py

4. Enter your guesses when prompted.

---

## 💻 Code

```python
import random

randomNumber = random.randint(1, 100)
count = 0

while True:
    number = int(input("Enter the number in between 1 to 100 : "))
    count += 1

    if number < randomNumber:
        print("The Guess number is low")
    elif number > randomNumber:
        print("The Guess number is High")
    else:
        print("The Guess number is correct")
        break

print(f"The number of attempts you made while playing the game {count}")
```

---

## 🧠 How It Works

1. A random number is generated.
2. The program repeatedly asks the user to guess.
3. The counter increases with each guess.
4. The loop stops when the correct number is guessed.
5. Total attempts are displayed.

---

## 📝 Example Output

```
Enter the number in between 1 to 100 : 50
The Guess number is low
Enter the number in between 1 to 100 : 75
The Guess number is High
Enter the number in between 1 to 100 : 63
The Guess number is correct
The number of attempts you made while playing the game 3
```

---

## ⭐ Possible Improvements  bv  bv                             

* Limit number of attempts
* Difficulty levels (easy, medium, hard)
* Input validation
* Play again option
* Score tracking

---

## 👨‍💻 Author

Number Guessing Game — Beginner Python Project
