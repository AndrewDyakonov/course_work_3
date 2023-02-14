import json
from classes import Operation


def get_json_to_list():
    """
    Получить список операций из файла operation.json
    :return:
    """
    with open('operation.json', 'r', encoding="UTF-8") as file:
        list_operation = json.load(file)
    return list_operation


def create_ex_class():
    """
    Создать список экземпляров класса
    :return:
    """
    list_ex_class = []
    list_from_json = get_json_to_list()
    for i in list_from_json:
        list_ex_class.append(Operation(i.get('date'),
                                       i.get('description'),
                                       i.get('to'),
                                       i.get('currency'),
                                       i.get('amount')))
    return list_ex_class
