import os
import json
import time

def read_last_number():
    try:
        with open("last_number.json", "r") as file:
            data = json.load(file)
            return data.get("last_number", 0)
    except FileNotFoundError:
        return 0

def write_last_number(number):
    with open("last_number.json", "w") as file:
        json.dump({"last_number": number}, file)

def launch_steam():
    last_number = read_last_number()
    next_number = last_number + 1
    command = f"steam://launch/{next_number}"

    os.system(f"start {command}")

    write_last_number(next_number)

    print(f"Команда выполнена: {command}")

def main():
    print("Консоль: Введите частоту (в секундах):")
    freq = int(input("Консоль: "))
    
    print("Консоль: Введите количество запусков:")
    num_clients = int(input("Консоль: "))
    
    print(f"Консоль: Работа начата с частотой {freq} секунд и количеством {num_clients} запусков.")

    for _ in range(num_clients):
        launch_steam()
        print(f"Консоль: Следующий запуск через {freq} секунд.")
        time.sleep(freq)

if __name__ == "__main__":
    main()
