from unittest.mock import MagicMock, patch

from src import extractors


@patch("pandas.read_csv")
def test_get_operations_csv(mock_read_csv: MagicMock) -> None:
    """
    Проверка работы функции get_operations_csv,
    которая считывает финансовые операции из CSV
    :param mock_read_csv: Моксированный объект pandas.read_csv
    :return: список словарей с транзакциями
    """

    # Создаем поддельный DataFrame и задаем его поведение
    mock_dataframe = MagicMock()
    mock_dataframe.to_dict.return_value = [{"res": 1}]

    # Настраиваем фиктурный объект read_csv
    mock_read_csv.return_value = mock_dataframe

    # Выполняем тестирование
    result = extractors.get_operations_csv("test.csv")
    expected_result = [{"res": 1}]
    assert result == expected_result


@patch("pandas.read_excel")
def test_get_operations_xlsx(mock_read_xlsx: MagicMock) -> None:
    """
    Проверка работы функции get_operations_xlsx,
    которая считывает финансовые операции из XLSX
    :param mock_read_xlsx: Моксированный объект pandas.read_excel
    :return: список словарей с транзакциями
    """

    # Создаем поддельный DataFrame и задаем его поведение
    mock_dataframe = MagicMock()
    mock_dataframe.to_dict.return_value = [{"res": 1}]

    # Настраиваем фиктурный объект read_csv
    mock_read_xlsx.return_value = mock_dataframe

    # Выполняем тестирование
    result = extractors.get_operations_xlsx("test.xlsx")
    expected_result = [{"res": 1}]
    assert result == expected_result
