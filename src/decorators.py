import datetime
from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

F_Spec = ParamSpec("F_Spec")
F_Return = TypeVar("F_Return")


def log(filename: str | None = None) -> Any:
    """
    Декоратор, который может логировать работу функции
    и ее результат как в файл, так и в консоль
    :param filename: строка с названием файла для логирования
    :return: файл с логом или текст в консоли
    """

    def decorator_log(
        func: Callable[F_Spec, F_Return],  # функция с произвольными входными аргументами
    ) -> Callable[F_Spec, F_Return]:  # функция с теми же входными аргументами
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_datetime = datetime.datetime.now()

            log_text = f"""
{start_datetime.strftime("%Y-%m-%d %H:%M:%S")}:
Function {func.__name__} called with args: {args} and kwargs: {kwargs}.
"""

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_text += f"""Error: {e}
"""
                if filename is None:
                    print(log_text)
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_text + "\n")

            end_datetime = datetime.datetime.now()
            res_execute_time = str(end_datetime - start_datetime)
            log_text += f"""Execution time: {res_execute_time}. Result: {result}
"""

            if filename is None:
                print(log_text)
            else:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_text + "\n")

            return result

        return wrapper

    return decorator_log
