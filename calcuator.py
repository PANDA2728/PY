def add(a, b):
    sum = a + b
    print(sum)


def sub(a, b):
    sum = a - b
    print(sum)


def mul(a, b):
    sum = a * b
    print(sum)


def div(a, b):
    sum = a / b
    print(int(sum))


a = int(input("Enter the number:"))
b = int(input("Enter the number:"))

while 1:
    print("\n 1.ADDITION \n 2. SUBTRACTION \n 3. MULTIPLICATION \n 4.DIVISION \n5. EXIT")
    ch = int(input("enter the choice"))
    if ch == 1:
        add(a, b)

    elif ch == 2:
        sub(a, b)
    elif (ch == 3):
        mul(a, b)
    elif (ch == 4):
        div(a, b)
