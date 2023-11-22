from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cof_mak = CoffeeMaker()
menu = Menu()
cashe_machine = MoneyMachine()

def main():
    is_on = True


    while is_on:
        order = input(f"What would you like? ({menu.get_items()}):")
        order_item = menu.find_drink(order)
        if order == 'off':
            is_on = False
        elif order == 'report':
            cof_mak.report()
        else:
            if cof_mak.is_resource_sufficient(order_item):
                if cashe_machine.make_payment(order_item.cost):
                    cof_mak.make_coffee(order_item)




if __name__ == '__main__':
    main()