import logging
import os

# Создаем папку logs, если ее еще нет
logs_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(logs_dir, exist_ok=True)


def setup_logger(name):
    """
    Создает и настраивает логер с указанным именем.

    Parameters:
        name (str): Имя логгера, обычно __name__ модуля.

    Returns:
        logging.Logger: Настроенный логер, который пишет логи в файл
                        в папке 'logs' с именем {name}.log.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    log_file = os.path.join(logs_dir, f"{name}.log")
    # Обработчик для записи логов в файл, перезаписывающий файл при каждом запуске
    file_handler = logging.FileHandler(log_file, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
