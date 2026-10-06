from abc import ABC, abstractmethod
from bisect import bisect_left


class TemperatureFactorStrategy(ABC):
    """Strategy para transformar temperatura en factor Tf."""

    @abstractmethod
    def calculate(self, temperature_c: float) -> float:
        raise NotImplementedError


class LinearInterpolationTemperatureStrategy(TemperatureFactorStrategy):
    """Usa la tabla de la guía e interpola temperaturas intermedias."""

    _TABLE = (
        (10.0, 1.00),
        (12.0, 0.90),
        (14.0, 0.80),
        (16.0, 0.70),
        (18.0, 0.60),
        (20.0, 0.50),
        (22.0, 0.40),
        (24.0, 0.30),
        (26.0, 0.20),
        (28.0, 0.10),
    )

    def calculate(self, temperature_c: float) -> float:
        if temperature_c <= self._TABLE[0][0]:
            return self._TABLE[0][1]
        if temperature_c >= self._TABLE[-1][0]:
            return self._TABLE[-1][1]

        temperatures = [point[0] for point in self._TABLE]
        position = bisect_left(temperatures, temperature_c)

        if temperatures[position] == temperature_c:
            return self._TABLE[position][1]

        t1, f1 = self._TABLE[position - 1]
        t2, f2 = self._TABLE[position]
        ratio = (temperature_c - t1) / (t2 - t1)
        return f1 + ratio * (f2 - f1)
