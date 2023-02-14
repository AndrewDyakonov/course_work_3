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
    list_from_json.sort(key=lambda d: d['date'], reverse=True)
    for i in list_from_json:
        if 'from' in i.keys():
            list_ex_class.append(Operation(i['date'],
                                           i['description'],
                                           i['from'],
                                           i['to'],
                                           i['operationAmount']['currency']['name'],
                                           i['operationAmount']['amount']))
        else:
            list_ex_class.append(Operation(i['date'],
                                           i['description'],
                                           i['to'],
                                           i['operationAmount']['currency']['name'],
                                           i['operationAmount']['amount']))
    return list_ex_class


q = create_ex_class()
print(*q, sep='\n')