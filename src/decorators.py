import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Decorator for logging function calls.
    Logs the function name, input parameters, result or error.
    In case of error, logs the error type and input parameters.
    Logs are written to a file if filename is specified, otherwise printed to the console.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Logging start of call
            start_msg = f"{func.__name__} вызван с args={args} kwargs={kwargs}\n"
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(start_msg)
            else:
                print(start_msg, end="")

            try:
                result = func(*args, **kwargs)
                success_msg = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(success_msg)
                else:
                    print(success_msg, end="")
                return result
            except Exception as e:
                error_type = type(e).__name__
                input_args = args
                input_kwargs = kwargs
                error_msg = (
                    f"{func.__name__} error: {error_type}. Inputs: args={input_args}, kwargs={input_kwargs}\n"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_msg)
                        f.write(f"{func.__name__} error\n")
                else:
                    print(error_msg, end="")
                    print(f"{func.__name__} error")
                raise  # Re-raising the exception
        return wrapper
    return decorator
