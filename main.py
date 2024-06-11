from Settings import OPERATION_PATH
from src.utils import load_json, get_executed_operations, sort_operations, get_last_operations, convert_date, \
    convert_payment_info


def main():
    operations = load_json(OPERATION_PATH)
    executed_operations = get_executed_operations(operations)
    sorted_operations = sort_operations(executed_operations)
    last_operations = get_last_operations(sorted_operations, 5)
    for operation in last_operations:
        converted_date = convert_date(operation["date"])
        converted_payment_from = convert_payment_info(operation["from"])
        converted_payment_to = convert_payment_info(operation["to"])
        if "открытие" in operation["description"].lower():
            print(f"{converted_date} {operation["description"]}\n"
                  f"{convert_payment_info(converted_payment_to) if converted_payment_to else None}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")
        else:
            print(f"{converted_date} {operation["description"]}\n"
                  f"{convert_payment_info(converted_payment_from) if converted_payment_from else None} -> "
                  f"{convert_payment_info(converted_payment_to) if converted_payment_to else None}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")
