water = 400
milk = 540
beans = 120
cups = 9
money =550

def c_state():
    global money, water, milk, beans, cups
    print(f"""The coffee machine has:
{water} ml of water
{milk} ml of milk
{beans} g of coffee beans
{cups} disposable cups
${money} of money""")

def action():
    c_state()
    print()
    print("Write action (buy, fill, take):")
    mode = input()
    if mode == "buy":
        buy()
    elif mode == "fill":
        fill()
    else:
        take()
    print()
    c_state()

def take():
    global money
    money -= money

def fill():
    global money, water, milk, beans, cups
    print("Write how many ml of water you want to add:")
    water += int(input())
    print("Write how many ml of milk you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans you want to add:")
    beans += int(input())
    print("Write how many disposable cups you want to add:")
    cups += int(input())

def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    menu = int(input())
    if menu == 1:
        buy_espresso()
    elif menu == 2:
        buy_latte()
    else:
        buy_cappuccino()

def buy_latte():
    global water, milk, beans, money, cups
    water -= 350
    milk -= 75
    beans -= 20
    cups -= 1
    money += 7

def buy_espresso():
    global water, beans, cups, money
    water -= 250
    beans -= 16
    money += 4
    cups -= 1

def buy_cappuccino():
    global water, milk, beans, money, cups
    water -= 200
    milk -= 100
    beans -= 12
    cups -= 1
    money += 6

action()
