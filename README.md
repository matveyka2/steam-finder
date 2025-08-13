
# Steam finder

This Python script allows you to launch Steam games or applications in sequence by incrementing a number each time. The script reads and updates the last launched game number, providing a way to automatically launch multiple games/applications with a defined interval.

## Features
- Launches Steam games or apps using a numbered format (`steam://launch/{number}`).
- Automatically increments the number of the last launched game.
- Allows you to configure the frequency (in seconds) and the number of launches.
- Saves the last used number in a `last_number.json` file for continuity between script runs.

---

## Requirements
- Python 3.x
- Steam client installed on your machine.

---

## Usage

1. **Clone the repository** (or download the script file).
2. **Run the script** in your terminal:
   ```bash
   python steam_launcher.py
   ```
3. The script will prompt you for:
   - **Frequency** (in seconds): The time interval between each launch.
   - **Number of launches**: How many times you want to launch the Steam game/application.

4. **The script will:**
   - Launch the next game in the sequence.
   - Update the last used number after each launch.
   - Wait for the specified interval before the next launch.

---

## How it works
1. **Read last used number**: The script reads the last used game number from the `last_number.json` file.
2. **Launches Steam game**: It constructs a `steam://launch/{next_number}` command and executes it.
3. **Updates the number**: After each launch, the script updates the `last_number.json` file to track the current number.

---

## Example
If the current game number is 3, the script will launch `steam://launch/4`, and so on.


# Steam finder

Этот скрипт на Python позволяет запускать игры или приложения Steam поочередно, увеличивая номер с каждым запуском. Скрипт читает и обновляет последний использованный номер игры, что позволяет автоматически запускать несколько игр/программ с заданным интервалом.

## Особенности
- Запуск игр или приложений Steam с использованием нумерованного формата (`steam://launch/{number}`).
- Автоматическое увеличение номера последней запущенной игры.
- Возможность настройки частоты (в секундах) и количества запусков.
- Сохранение последнего использованного номера в файле `last_number.json` для продолжения работы скрипта между запусками.

---

## Требования
- Python 3.x
- Установленный клиент Steam на вашем компьютере.

---

## Использование

1. **Клонируйте репозиторий** (или скачайте файл скрипта).
2. **Запустите скрипт** в терминале:
   ```bash
   python steam_launcher.py
   ```
3. Скрипт запросит у вас:
   - **Частоту** (в секундах): Интервал времени между каждым запуском.
   - **Количество запусков**: Сколько раз вы хотите запустить игру/программу Steam.

4. **Что сделает скрипт:**
   - Запустит следующую игру в последовательности.
   - Обновит последний использованный номер после каждого запуска.
   - Подождет указанный интервал перед следующим запуском.

---

## Как это работает
1. **Чтение последнего использованного номера**: Скрипт читает последний использованный номер игры из файла `last_number.json`.
2. **Запуск игры Steam**: Он формирует команду `steam://launch/{next_number}` и выполняет её.
3. **Обновление номера**: После каждого запуска скрипт обновляет файл `last_number.json`, чтобы отслеживать текущий номер.

---

## Пример
Если текущий номер игры 3, скрипт запустит `steam://launch/4`, и так далее.
