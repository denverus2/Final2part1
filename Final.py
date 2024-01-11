import json
import csv
import datetime
import sys

# Функция для сохранения заметок в файле формата json или csv
def save_notes(notes, format):
    if format == "json":
        with open("notes.json", "w") as f:
            json.dump(notes, f, indent=4)
    elif format == "csv":
        with open("notes.csv", "w") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["id", "title", "body", "date"])
            for note in notes:
                writer.writerow([note["id"], note["title"], note["body"], note["date"]])
    else:
        print("Неверный формат файла")

# Функция для загрузки заметок из файла формата json или csv
def load_notes(format):
    notes = []
    if format == "json":
        with open("notes.json", "r") as f:
            notes = json.load(f)
    elif format == "csv":
        with open("notes.csv", "r") as f:
            reader = csv.reader(f, delimiter=";")
            next(reader) # Пропускаем заголовок
            for row in reader:
                note = {"id": row[0], "title": row[1], "body": row[2], "date": row[3]}
                notes.append(note)
    else:
        print("Неверный формат файла")
    return notes

# Функция для генерации уникального идентификатора заметки
def generate_id(notes):
    ids = [int(note["id"]) for note in notes]
    if ids:
        return str(max(ids) + 1)
    else:
        return "1"

# Функция для добавления новой заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    id = generate_id(notes)
    note = {"id": id, "title": title, "body": body, "date": date}
    notes.append(note)
    print("Заметка успешно добавлена")

# Функция для чтения списка заметок с фильтрацией по дате
def read_notes():
    date = input("Введите дату в формате дд.мм.гггг или нажмите Enter для вывода всех заметок: ")
    filtered_notes = []
    for note in notes:
        if date in note["date"] or date == "":
            filtered_notes.append(note)
    if filtered_notes:
        print("Список заметок:")
        for note in filtered_notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['date']}")
    else:
        print("Нет заметок с заданной датой")

# Функция для редактирования заметки по идентификатору
def edit_note():
    id = input("Введите идентификатор заметки для редактирования: ")
    for note in notes:
        if note["id"] == id:
            title = input("Введите новый заголовок заметки или нажмите Enter, чтобы оставить прежний: ")
            body = input("Введите новое тело заметки или нажмите Enter, чтобы оставить прежнее: ")
            date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            if title != "":
                note["title"] = title
            if body != "":
                note["body"] = body
            note["date"] = date
            print("Заметка успешно отредактирована")
            break
    else:
        print("Нет заметки с таким идентификатором")

# Функция для удаления заметки по идентификатору
def delete_note():
    id = input("Введите идентификатор заметки для удаления: ")
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            print("Заметка успешно удалена")
            break
    else:
        print("Нет заметки с таким идентификатором")

# Функция для вывода справки по командам
def help():
    print("Доступные команды:")
    print("add - добавить новую заметку")
    print("read - прочитать список заметок")
    print("edit - отредактировать заметку по идентификатору")
    print("delete - удалить заметку по идентификатору")
    print("save - сохранить заметки в файл")
    print("load - загрузить заметки из файла")
    print("help - вывести справку по командам")
    print("exit - выйти из программы")

# Список заметок
notes = []

# Формат файла для сохранения и загрузки заметок
format = "json"

# Основной цикл программы
while True:
    command = input("Введите команду (help для списка): ")
    if command == "add":
        add_note()
    elif command == "read":
        read_notes()
    elif command == "edit":
        edit_note()
    elif command == "delete":
        delete_note()
    elif command == "save":
        save_notes(notes, format)
        print("Заметки успешно сохранены в файл")
    elif command == "load":
        notes = load_notes(format)
        print("Заметки успешно загружены из файла")
    elif command == "help":
        help()
    elif command == "exit":
        print("До свидания!")
        break
    else:
        print("Неверная команда, введите help для справки")
