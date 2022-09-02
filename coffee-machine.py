#!/usr/bin/env python3
"""
A digital coffee machine
"""

__version__ = "0.1"
__author__ = "Krit Jitpungtham"

# Machine class Encapsule data และ method ที่เกี่ยวข้องกับ Machine
class Machine:
    def __init__(self, water, milk, coffee_pow, money, coffee_menu):

        self.water = water
        self.milk = milk
        self.coffee_pow = coffee_pow
        self.money = money
        self.coffee_menu = coffee_menu

        self.command_list = {"report": self.report, "off": self.off}

    # โปรแกรมหลักในการรับคำสั่งจาก user
    # ในตัวอย่างใช้ loop while true ไม่แน่ใจแบบไหนดีกว่ากัน
    def prompt(self):

        command = input("​What would you like? (espresso/ latte/ cappuccino): ")

        # เช็ค command ใน list และเรียกใช้
        if command in self.command_list.keys():
            self.command_list[command]()

        elif command in self.coffee_menu.get_menu().keys():
            self.coffee_obj = self.coffee_menu.get_menu()[command]
            self.check(self.coffee_obj)

        else:
            print("Command not found. Try again")
            self.prompt()

    def report(self):
        print(
            f"""
                  Water \t: {self.water} \tml,
                  Milk  \t: {self.milk} \tml,
                  Coffee \t: {self.coffee_pow} \tg,
                  Money \t: ${self.money}
                  """
        )
        self.prompt()

    def off(self):
        del self

    def check(self, coffee_obj):

        if self.water < coffee_obj.water:
            print("Sorry there is not enough water.")

        elif self.milk < coffee_obj.milk:
            print("Sorry there is not enough milk.")

        elif self.coffee_pow < coffee_obj.coffee:
            print("Sorry there is not enough coffee.")

        else:
            self.check_money(coffee_obj)

    def check_money(self, coffee_obj):

        self.coin = Coin()
        self.coin.insert_coin()

        if self.coin.value < self.coffee_obj.cost:
            print("Sorry that's not enough money. Money refunded.")
            self.prompt()

        else:
            change = self.coin.value - coffee_obj.cost
            print(f"Here is ${change} dollars in change.")
            self.make(self.coffee_obj)

    def make(self, coffee_obj):

        self.water -= coffee_obj.water
        self.milk -= coffee_obj.milk
        self.coffee_pow -= coffee_obj.coffee
        self.money += coffee_obj.cost

        print(f"Here is your {coffee_obj.name}. Enjoy!")
        self.prompt()


# Class Coffee สำหรับ ข้อมูลของกาแฟแต่ละชนิด
class Coffee:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


# ใช้จัดการ class Coffee
class Coffee_menu:
    def __init__(self):

        espresso = Coffee("espresso", 50, 0, 18, 1.50)
        latte = Coffee("latte", 200, 150, 24, 2.50)
        cappuccino = Coffee("cappuccino", 250, 100, 24, 3.00)
        self.menu_list = {
            "espresso": espresso,
            "latte": latte,
            "cappuccino": cappuccino,
        }

    def add_menu(self, name, water, milk, coffee, cost):

        new_coffee = Coffee(water, milk, coffee, cost)
        Coffee.menu_list.append(new_coffee)

    def get_menu(self):
        return self.menu_list


# class Coin จัดการเรื่องเงิน
class Coin:
    def __init__(self):
        self.value = 0

    def insert_coin(self):
        quarter = int(input("How many quaters?: ")) * 0.25
        dime = int(input("How many dimes?: ")) * 0.10
        nickle = int(input("How many nickles?: ")) * 0.05
        penny = int(input("How many pennies?: ")) * 0.01
        self.value += penny + nickle + dime + quarter


def main():
    """Main entry point of the app"""
    coffee_menu = Coffee_menu()
    machine = Machine(300, 200, 100, 0, coffee_menu)
    machine.prompt()


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
