import json

# Базовий словник даних про багаж
luggage_db = {
    "P1": {"count": 3, "weight": 45.0},
    "P2": {"count": 1, "weight": 18.5},
    "P3": {"count": 2, "weight": 22.0},
    "P4": {"count": 4, "weight": 50.0},
    "P5": {"count": 1, "weight": 30.0},
    "P6": {"count": 3, "weight": 36.0},
    "P7": {"count": 2, "weight": 15.0},
    "P8": {"count": 5, "weight": 60.0},
    "P9": {"count": 1, "weight": 12.0},
    "P10": {"count": 2, "weight": 28.0}
}

def print_all(db):
    if not db:
        print("Словник порожній.")
        return
    print("\n--- Вміст словника багажу ---")
    for key, data in db.items():
        print(f"Пасажир (№ багажу): {key:5} | Кількість речей: {data['count']:2} | Загальна вага: {data['weight']:5.1f} кг")

def add_entry(db):
    key = input("Введіть номер багажу (ключ): ").strip()
    if key in db:
        print("Помилка: Запис існує!")
        return
    try:
        count = int(input("Введіть кількість речей: "))
        weight = float(input("Введіть загальну вагу (кг): "))
        if count <= 0 or weight <= 0:
            raise ValueError("Значення мають бути більше 0")
        db[key] = {"count": count, "weight": weight}
        print(f"Запис '{key}' успішно додано.")
    except ValueError as e:
        print(f"Помилка введення: {e}")

def delete_entry(db):
    key = input("Введіть номер багажу для видалення: ").strip()
    try:
        del db[key]
        print(f"Запис '{key}' видалено.")
    except KeyError:
        print(f"Помилка: Багаж '{key}' не знайдено!")

def print_sorted(db):
    if not db:
        print("Словник порожній.")
        return
    print("\n--- Словник (відсортований) ---")
    for key in sorted(db.keys()):
        data = db[key]
        print(f"Пасажир (№ багажу): {key:5} | Кількість речей: {data['count']:2} | Загальна вага: {data['weight']:5.1f} кг")

def task_a(db):
    count = sum(1 for data in db.values() if data['count'] > 2)
    print(f"\n[а] Пасажирів із понад 2 речами: {count}")

def task_b(db):
    found = any(data['count'] == 1 and data['weight'] < 25.0 for data in db.values())
    print(f"\n[б] Наявність пасажира (1 річ < 25 кг): {'ТАК' if found else 'НІ'}")

def task_c(db):
    total_items = sum(data['count'] for data in db.values())
    total_weight = sum(data['weight'] for data in db.values())
    if total_items == 0:
        return
    avg_item_weight = total_weight / total_items
    print(f"\nСередня вага однієї речі по загалу: {avg_item_weight:.2f} кг")
    for key, data in db.items():
        p_avg = data['weight'] / data['count']
        if abs(p_avg - avg_item_weight) <= 0.5:
            print(f"  - Номер: {key} (сер. вага речі: {p_avg:.2f} кг)")

# --- Додатковий розширений функціонал ---
def find_min_max_luggage(db):
    """Визначення найважчого та найлегшого багажу"""
    if not db:
        print("Словник порожній.")
        return
    max_k = max(db, key=lambda k: db[k]['weight'])
    min_k = min(db, key=lambda k: db[k]['weight'])
    print(f"\n[Аналітика багажу]:")
    print(f"  - Найважчий багаж: {max_k} ({db[max_k]['weight']} кг)")
    print(f"  - Найлегший багаж: {min_k} ({db[min_k]['weight']} кг)")

def save_to_json(db, filename="luggage_data.json"):
    """Збереження словника у JSON файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=4)
        print(f"\n[Експорт]: Дані успішно збережено у файл '{filename}'.")
    except Exception as e:
        print(f"Помилка при збереженні файлу: {e}")

def main():
    while True:
        print("\n" + "="*50)
        print(" МЕНЮ КЕРУВАННЯ ПРОЄКТОМ (Шкуро Анна)")
        print("="*50)
        print("1 - Вивести всі записи")
        print("2 - Додати новий запис")
        print("3 - Видалити запис за ключем")
        print("4 - Перегляд за відсортованими ключами")
        print("5 - [Завдання А] Кількість пасажирів з > 2 речами")
        print("6 - [Завдання Б] Перевірка (1 річ < 25 кг)")
        print("7 - [Завдання В] Пошук за середньою вагою речі")
        print("8 - [Розширено] Аналітика (Мін/Макс вага багажу)")
        print("9 - [Розширено] Експорт словника у JSON")
        print("0 - Вихід")
        
        choice = input("Оберіть пункт меню: ").strip()
        if choice == '1': print_all(luggage_db)
        elif choice == '2': add_entry(luggage_db)
        elif choice == '3': delete_entry(luggage_db)
        elif choice == '4': print_sorted(luggage_db)
        elif choice == '5': task_a(luggage_db)
        elif choice == '6': task_b(luggage_db)
        elif choice == '7': task_c(luggage_db)
        elif choice == '8': find_min_max_luggage(luggage_db)
        elif choice == '9': save_to_json(luggage_db)
        elif choice == '0':
            print("Завершення роботи.")
            break

if __name__ == "__main__":
    main()
