from datetime import datetime

from src.search import process_bank_search
from src.utils import read_transactions


def get_valid_status() -> str:
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию:\n"
            "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()
        if status in valid_statuses:
            return status
        else:
            print(f"Статус операции \"{status}\" недоступен.")


def sort_transactions_by_date(transactions: list, ascending: bool = True) -> list:
    """Сортирует список транзакций по дате."""

    def parse_date(date_str: str):
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            return datetime.min  # Для некорректных дат

    return sorted(
        transactions,
        key=lambda t: parse_date(t.get('date', '')),
        reverse=not ascending
    )


def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")

    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    choice = input()

    # Для примера возьмем только JSON
    if choice == '1':
        print("Программа: Для обработки выбран JSON-файл.")
        file_path = input("Введите путь к файлу JSON: ")
        transactions = read_transactions(file_path)
        if not transactions:
            print("Файл пустой или содержит неправильные данные.")
            return

        # Запрос фильтрации по статусу
        status = get_valid_status()

        # Фильтрация по статусу
        filtered_transactions = [t for t in transactions if t.get('status', '').upper() == status]
        print(f"Операции отфильтрованы по статусу \"{status}\".")

        # Сортировка по дате
        sort_order = input("Отсортировать операции по дате? Да/Нет\n").lower()
        if sort_order == 'да':
            order_type = input("Отсортировать по возрастанию или по убыванию?\n").lower()
            ascending = 'убыва' not in order_type
            filtered_transactions = sort_transactions_by_date(filtered_transactions, ascending=ascending)

        # Фильтр по валюте
        currency_filter = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        if currency_filter == 'да':
            filtered_transactions = [t for t in filtered_transactions if t.get('currency', '').upper() == 'RUB']

        # Фильтр по слову в описании
        filter_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
        if filter_word == 'да':
            search_word = input("Введите слово для поиска:\n")
            filtered_transactions = process_bank_search(filtered_transactions, search_word)

        # ВЫВОД итоговых операций
        if not filtered_transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        else:
            print("Распечатываю итоговый список транзакций...")
            print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")
            for t in filtered_transactions:
                date_str = t.get('date', '')
                description = t.get('description', '')
                amount = t.get('amount', '')
                currency = t.get('currency', '')
                print(f"{date_str} {description}")
                print(f"Сумма: {amount} {currency}\n")
    else:
        print("Функциональность для выбранного варианта еще не реализована.")


if __name__ == "__main__":
    main()
