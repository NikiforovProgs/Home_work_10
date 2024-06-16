from typing import Any, Generator, List, Dict


def transaction_descriptions(transactions: List[Dict[str, Any]], transaction_list=None) -> Generator[str, None, None]:
    for transaction in transaction_list:
        yield transaction.get('description', 'Описание операции отсутствует')
