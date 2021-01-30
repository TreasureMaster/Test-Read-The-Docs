"""
main.py
====================================
Основной модуль моего примера проекта
"""


def about_me(your_name: str) -> str:
    """
    Возвращает самое главное о персоне.

    Расширенное описание и очень подробное функции.

    Parameters
    ----------
    your_name : str
        Строка, показывающая имя персоны.
    """
    return "The wise {} loves Python.".format(your_name)


class ExampleClass:
    """Пример строки документации для определения класса."""

    def __init__(self, name: str, age: int):
        """
        Конструктор класса.

        Parameters
        ---------
        name : str
            Строка, назначаемая атрибуту экземпляра `name`.
        age : int
            Возраст персоны.
        """
        self.name = name
        self.age = age

    def about_self(self) -> str:
        """
        Возвращает информацию об экземпляре, созданном из ExampleClass.

        Расширенное описание и очень подробное метода класса.

        See Also
        --------
        average : Weighted average.

        Note
        -----
        The FFT is a fast implementation of the discrete Fourier transform:

        Returns
        -------
        str
            Возвращает информацию об экземпляре.
        """
        date = 'mock_date'
        time = 'mock_time'
        """
        Note
        -----
        Простой тест документации внутри кода. Документирование здесь не поддерживается.
        """
        return "I am a very smart {} object.".format(self.name)
