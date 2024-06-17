from typing import Any, Generator, List, Dict


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[dict[str, Any]]:
    """Функция, принимающая список словарей с банковскими операциями и возвращающая
     итератор, который выдает по очереди операции, в которых указана заданная валюта"""
    return (transaction for transaction in transactions
            if transaction.get('operationAmount', {}).get('currency', {}).get('name') == currency)


usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(next(usd_transactions)["id"])


def transaction_descriptions(transactions: List[Dict[str, Any]], transaction_list) -> Generator[str, None, None]:
    """Генератор, который принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transaction_list:
        yield transaction.get('description', 'Описание операции отсутствует')

    descriptions = transaction_descriptions(transactions):
    for _ in range(5):
        print(next(descriptions)
