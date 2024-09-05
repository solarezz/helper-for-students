import subprocess


print(r"             _                              ")
print(r" ___   ___  | |  __ _  _ __   ___  ____ ____")
print(r"/ __| / _ \ | | / _` || '__| / _ \|_  /|_  /")
print(r"\__ \| (_) || || (_| || |   |  __/ / /  / / ")
print(r"|___/ \___/ |_| \__,_||_|    \___|/___|/___|")
print(r"----------------from studies----------------")


def print_menu():
    menu_items = ["1. DHCP", "2. DNS", "3. Other"]
    a = ''
    print("┏━━━━━━━━━━━━━━━━━━━┓")
    for item in menu_items:
        print(f"┃ {item:<15} ┃")
    print("┗━━━━━━━━━━━━━━━━━━━┛")


print_menu()

choice = input("Choice number: ")

while True:
    if choice == 1:
        try:
            script_path = r'./bash_scripts/dhcp-helper-lite'

            result = subprocess.run(['bash', script_path], capture_output=True, text=True, check=True)

            print("Вывод скрипта:")
            print(result.stdout)

        except subprocess.CalledProcessError as e:
            print(f'Ошибка выполнения скрипта: {e}')
            print(f'Код возврата: {e.returncode}')
            print(f'Сообщение об ошибке: {e.stderr}')

