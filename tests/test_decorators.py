import os

import pytest

from src.decorators import log


def test_successful_call(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "add вызван" in captured.out
    assert "add ok" in captured.out


def test_successful_call_to_file():
    filename = "test_log.txt"

    # Удаляем файл перед тестом, если есть
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def multiply(x, y):
        return x * y

    result = multiply(4, 5)
    assert result == 20
    # Проверка, что файл создан
    assert os.path.exists(filename)

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        assert "multiply вызван" in content
        assert "multiply ok" in content

    os.remove(filename)


def test_exception_in_function(capsys):
    @log()
    def div(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    assert "div вызван" in captured.out
    assert "div error" in captured.out
    assert "ZeroDivisionError" in captured.out


def test_exception_in_function_to_file():
    filename = "error_log.txt"

    # Удаляем файл перед тестом, если есть
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def error_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        error_func()

    # Проверяем, что лог-файл создан
    assert os.path.exists(filename)

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        assert "error_func" in content
        assert "ValueError" in content

    os.remove(filename)
