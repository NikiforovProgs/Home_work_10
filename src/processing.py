from typing import Any


def filter_by_state(key_list: list[dict[str, Any]], def_state: bool = True) -> list[dict[str, Any]]:
    """Принимает список словарей и значение для 'state', возвращает
    новый список со словарями у которых ключ 'state'
    содержит переданное в функцию значение"""
    new_key_list = []
    for dict_list_key in key_list:
        if dict_list_key.get('state') == def_state:
            new_key_list.append(dict_list_key)
    return new_key_list


def sort_by_date(date_list: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Принимает список словарей, возвращает список
    отсортированных исходных словарей по убыванию даты"""
    sort_date_list = sorted(date_list, key=lambda date_dict: date_dict.get('date'), reverse=reverse_list)
    return sort_date_list
