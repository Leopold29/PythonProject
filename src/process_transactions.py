from typing import Dict, List

import pandas as pd


def read_transactions_csv(file_path: str) -> List[Dict]:
    """
    Читает транзакции из CSV-файла и возвращает их в виде списка словарей.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        List[Dict]: Список транзакций, каждая в виде словаря.
    """
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')


def read_transactions_excel(file_path: str) -> List[Dict]:
    """
    Читает транзакции из Excel-файла и возвращает их в виде списка словарей.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        List[Dict]: Список транзакций, каждая в виде словаря.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
