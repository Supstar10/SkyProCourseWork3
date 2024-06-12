from Settings import TEST_OPERATION_PATH
from src.utils import load_json, get_executed_operations, sort_operations, get_last_operations, convert_date, \
    convert_payment_info


def test_load_json():
    operation = load_json(TEST_OPERATION_PATH)
    assert len(operation) == 3


def test_get_executed_operations(operations_fixture, canceled_operations_fixture, executed_operations_fixture):
    operation = get_executed_operations(executed_operations_fixture)
    assert len(operation) == 2
    operation = get_executed_operations(canceled_operations_fixture)
    assert len(operation) == 0
    operation = get_executed_operations(operations_fixture)
    assert len(operation) == 1


def test_sort_operations(executed_operations_fixture):
    operation = sort_operations(executed_operations_fixture)
    assert operation[0].get("date") == "2021-07-03T18:35:29.512364"
    assert operation[0].get("date") > operation[1].get("date")


def test_get_last_operations(executed_operations_fixture):
    operation = get_last_operations(executed_operations_fixture, count=1)
    assert operation


def test_convert_date():
    operation = convert_date(date="2019-08-26T10:50:58.294041")
    assert operation == "26.08.2019"


def test_convert_payment_info():
    operations = convert_payment_info(payment="Счет 64686473678894779589")
    assert operations == "Счет **9589"
    operations = convert_payment_info(payment="MasterCard 7158300734726758")
    assert operations == "MasterCard  7158 30** **** 6758"
