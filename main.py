# This is a
number = int(input("Enter a number:"))


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)


def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)


if number > 0:
    countdown(number)
else:
    countup(number)