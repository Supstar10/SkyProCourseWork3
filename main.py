from Settings import COUNT
from src.utils import load_json, get_executed_operations, sort_operations, get_last_operations, convert_date, \
    convert_payment_info


def main():
    operations = load_json(path)
    executed_operations = get_executed_operations(operations)
    sorted_operations = sort_operations(executed_operations)
    last_operations = get_last_operations(sorted_operations, COUNT)
    for operation in last_operations:
        converted_date = convert_date(operation["date"])
        converted_payment_from = convert_payment_info(operation["from"])
        converted_payment_to = convert_payment_info(operation["to"])
        result = f"{converted_date} {converted_payment_from} {converted_payment_to}"
        print(result)
