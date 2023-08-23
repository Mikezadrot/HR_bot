# Створення порожнього словника для збереження інформації про користувачів
user_data_dict = {}

# Додавання інформації про користувачів в словник
user_id = 12345
country = "Україна"
profession = "Лікар"

user_data_dict[user_id] = {"country": country, "profession": profession}

# Отримання інформації про користувача за його ID
if user_id in user_data_dict:
    user_info = user_data_dict[user_id]
    print(f"ID: {user_id}, Країна: {user_info['country']}, Професія: {user_info['profession']}")
else:
    print("Користувача з таким ID не знайдено.")

# Оновлення інформації про користувача
if user_id in user_data_dict:
    user_data_dict[user_id]["country"] = "Польща"
    user_data_dict[user_id]["profession"] = "Вчитель"

# Видалення інформації про користувача
if user_id in user_data_dict:
    del user_data_dict[user_id]
