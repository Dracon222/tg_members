from colorama import Fore
import os
import sys 

def display_menu():
    print()
    print()
    print(f'    {Fore.CYAN}╔════════════════════════════════════════════════════════════════════════╗')
    print(f'    {Fore.CYAN}║                               Main Menu                               ║')
    print(f'    {Fore.CYAN}╠════════════════════════════════════════════════════════════════════════╣')

    bloklar = [
        (
            "Guruhdan Guruhga odam o'tkazuvchi maxsus koʻd Kanal: @TermuXcoderUz",
            [
                "[ 0 ] Foydalanish haqida",
                "[ 1 ] Raqam ulash",
                "[ 2 ] Ulangan raqamlarni tekshirish",
                "[ 3 ] Ban akkauntlarni oʻchirish",
                "[ 4 ] Guruhdan Guruhga odam oʻtkazish",
                "[ 5 ] Dasturdan chiqish",
            ]
        ),
    ]

    for nomi, opsiyalar in bloklar:
        print(f'    {Fore.CYAN}║ {Fore.YELLOW}{nomi:<66} {Fore.CYAN}║')
        print(f'    {Fore.CYAN}╠════════════════════════════════════════════════════════════════════════╣')
        for opsiya in opsiyalar:
            print(f'{Fore.GREEN}        {opsiya}')
        print(f'    {Fore.CYAN}╠════════════════════════════════════════════════════════════════════════╣')

    print(f'    {Fore.CYAN}╚════════════════════════════════════════════════════════════════════════╝')


def enter_code():
    print()
    print()
    choice = input(f'{Fore.YELLOW}Iltimos, variantni tanlang: ')
    print()

    if choice == "5": 
        print(f"{Fore.RED}Dasturdan chiqildi!")
        sys.exit(0)

    coded = choice
    if coded:
        os.system(f"python3 activate.py --code {coded}")
    else:
        print(f"{Fore.RED}Xatolik! Menudan tanlovni kiriting!")

def main():
    while True:
        display_menu()  
        enter_code()

if __name__ == "__main__":
    main()
