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
    for operation in operations:
        if operation["state"] == "EXECUTED":
            return operation


def data_from_iso(executed_operations):
    return datetime.fromisoformat(executed_operations["data"])


def sort_operations(executed_operations):
    """
    Сортирует операции по дате 
    """

    for operation in operations:
        if operation["date"] >


def get_last_operations(sorted_operations, COUNT):
    return operation[:COUNT]


def convert_date(date):
    datetime.fromisoformat(last_operations['date'])


def convert_payment_info(payment_info):
    if payment_info.startswith("Счет"):
