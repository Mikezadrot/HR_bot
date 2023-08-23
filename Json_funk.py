from spreadsheet import get_data_from_spreadsheet
import json
from datetime import datetime
import os


def writing_to_json():
    data = get_data_from_spreadsheet()

    data_list = []
    for row in data:
        number, country, vacancy, salary = row
        data_list.append({
            'Номер вакансії': number,
            'Країна': country,
            'Вакансія': vacancy,
            'Плата': salary
        })

    current_datetime = datetime.now()
    index = current_datetime.strftime("%Y%m%d%H%M%S")
    file_name = f"data_{index}.json"
    main_file_name= 'data.json'
    if os.path.exists("data.json"):

        os.rename("data.json", os.path.join("res", file_name) )
    else:
        print("Creating new json")

    with open(main_file_name, "w") as json_file:
        json.dump(data_list, json_file, ensure_ascii=False, indent=4)


def load_data_from_json(file_path='data.json'):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data


def write_users_dict(user_data_dict):
    with open("user_data.json", "w") as json_file:

        json.dump(user_data_dict, json_file)


def readind_users_dict():
    with open("user_data.json", "r") as json_file:

        user_data_dict = json.load(json_file)
        return user_data_dict

