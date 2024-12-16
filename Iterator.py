
from StepValueError import StepValueError


class Iterator:
    """Итератор, который позволяет проходить диапазон чисел с заданным шагом."""

    def __init__(self, start, stop, step=1):
        """Инициализирует итератор с начальной, конечной точками и шагом.

        Args:
            start (int): Начальное значение диапазона.
            stop (int): Конечное значение диапазона (не включается).
            step (int, optional): Шаг итерации. По умолчанию равен 1.

        Raises:
            StepValueError: Если шаг равен 0.
        """
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')

        self.start = start  # Начальное значение диапазона.
        self.stop = stop    # Конечное значение диапазона.
        self.step = step    # Шаг итерации.
        self.pointer = start  # Текущая позиция итератора.

    def __iter__(self):
        """Возвращает итератор (самого себя)."""
        self.pointer = self.start  # Сбрасывает указатель на начало.
        return self

    def __next__(self):
        """Возвращает следующее значение в итерации.

        Raises:
            StopIteration: Если итератор достиг конца диапазона.

        Returns:
            int: Текущее значение итератора.
        """
        # Проверка на окончание диапазона в зависимости от знака шага.
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration

        current = self.pointer  # Сохраняем текущее значение.
        self.pointer += self.step  # Увеличиваем указатель на шаг.
        return current
