import json
from datetime import datetime
from pathlib import Path


def load_json(path):
    """
    Загружает json файл
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_executed_operations(operations):
    """
    Получает Executed операцию
    """
    executed_operations = []
    for operation in operations:
        if operation["state"] == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def sort_operations(operations):
    """
    Сортирует операции по дате
    """

    return sorted(operations, key=lambda operation: operation.get("date"), reverse=True)


def get_last_operations(operations, count):
    return operations[:count]


def convert_date(date):
    '''
    Переводит дату в iso формат
    '''
    datatime_lst = date.split("T")[0]
    data = datetime.strftime(datatime_lst, '%Y-%m-%d').date().strftime('%d-%m-%Y')
    return data


def convert_payment_info(payment):
    if payment.startswith("Счет"):
        return f'{payment[:5]} ** {payment[-4:]}'
    else:
        payment_info = payment.split()[len(payment.split()) - 1]
        card_info = payment.replace(payment_info, "")
        payment_info = payment_info[:-10] + " ** " + payment_info[12:]
        return f'{card_info} {payment_info[:4]} {payment_info[4:]}'
