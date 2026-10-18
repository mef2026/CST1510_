'''''
Password Generator

**Uses:** lists, `random.choice()`, `random.shuffle()`, `for` loops,
string building

1. At the top of your file, write `import random`.
2. Create a list called `letters` containing every letter `a`–`z` and
   `A`–`Z` as separate strings, for example `["a", "b", "c", ...]`.
3. Create a list called `numbers` containing the strings `"0"` to `"9"`.
4. Create a list called `symbols` containing some symbols, for example
   `["!", "#", "$", "%", "&", "(", ")", "*", "+"]`.
5. Use `input()` to ask how many letters the user wants. Convert it with
   `int()` and store it in `nr_letters`.
6. Do the same for symbols, storing the answer in `nr_symbols`.
7. Do the same for numbers, storing the answer in `nr_numbers`.

**Easy version — letters, then symbols, then numbers**

8. Create a variable `password` and set it to an empty string `""`.
9. Write a `for` loop using `range(nr_letters)`. Inside it, add
   `random.choice(letters)` to the end of `password` using `+=`.
10. Write a second `for` loop using `range(nr_symbols)` that does the
    same with `symbols`.
11. Write a third `for` loop using `range(nr_numbers)` that does the
    same with `numbers`.
12. Print `password`.

**Hard version — shuffled order**

13. Create a variable `password_list` and set it to an empty list `[]`.
14. Repeat steps 9–11, but this time use `.append()` to add each random
    character to `password_list` instead of adding it to a string.
15. Call `random.shuffle(password_list)` to mix up the order.
    (Note: `shuffle()` changes the list in place and returns `None`, so
    don't write `password_list = random.shuffle(password_list)`.)
16. Create a variable `password` and set it to `""`.
17. Write a `for char in password_list:` loop that adds each `char` to
    `password`.
18. Print `password`. Run it a few times with the same inputs and check
    the order changes each time.

**Extension:** replace steps 16–17 with one line:
`password = "".join(password_list)`.
'''




import random




letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", ":", "?", "|", "^"]

nr_letters = int(input("Numbers of letters "))
nr_symbols = int(input("Numbers of symbols "))
nr_numbers = int(input("Numbers of numbers "))



password = ""

for i in range(nr_letters):
    password += random.choice(letters)

for i in range(nr_symbols):
    password += random.choice(symbols)
for i in range(nr_numbers):
    password += random.choice(numbers)

print(" The password is:", password)
