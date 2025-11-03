# Проект "Банковское дело"

## Описание:

Проект "Банковское дело" — это веб-приложение на Python, предназначенное для скрытия номеров кредитных карт.
Оно помогает безопасно обрабатывать платежные данные, маскируя номера карт в пользовательском интерфейсе

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Leopold29/PythonProject
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Документация:

Для получения дополнительной информации обратитесь к [документации](PythonProject/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

## Модуль generators:
В рамках модуля generators реализованы следующие функции:

### filter_by_currency(transactions, currency_code) — фильтрует список транзакций по заданной валюте, возвращая итератор.
### transaction_descriptions(transactions) — генератор, возвращающий описание каждой транзакции.
### card_number_generator(start, stop) — генератор номеров карт в диапазоне, формата XXXX XXXX XXXX XXXX.

### Примеры использования:
```
from src import generators

transactions = [...]  # ваш список транзакций
```
### Фильтрация транзакций по валюте USD
```
usd_transactions = generators.filter_by_currency(transactions, "USD")
for t in usd_transactions:
    print(t)
```
### Получение описаний транзакций
```
descriptions = generators.transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)
```
### Генерация номеров карт в диапазоне
```
for card in generators.card_number_generator(1, 3):
    print(card)
```
## Тестирование:

Для запуска тестов используйте следующую команду:
```
coverage run -m pytest
coverage html
```