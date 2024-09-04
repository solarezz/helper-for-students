from art import *
from colorama import Fore, Back, Style

Art = text2art("solarezz")
print(Fore.CYAN + Art)
print("            ---from studies---")


def print_menu():
    menu_items = ["1. DHCP", "2. DNS", "3. Other"]
    a = ''
    print("┏━━━━━━━━━━━━━━━━━━━┓")
    for item in menu_items:
        print(f"┃ {item:<15} ┃")
    print("┗━━━━━━━━━━━━━━━━━━━┛")


print_menu()

choice = input("Choice number: ")
