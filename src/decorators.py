from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

F_Spec = ParamSpec("F_Spec")
F_Return = TypeVar("F_Return")


def log(filename: str | None) -> Any:
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
            result = func(*args, **kwargs)

            if filename is None:
                print(f"Function {func.__name__} called with " f"args: {args} and kwargs: {kwargs}. Result: {result}")

            return result

        return wrapper

    return decorator_log
