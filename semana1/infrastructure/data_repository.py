from abc import ABC, abstractmethod

from domain.entities import WeatherObservation


class WeatherDataRepository(ABC):
    @abstractmethod
    def get_observations(self) -> list[WeatherObservation]:
        raise NotImplementedError


class InMemoryWeatherDataRepository(WeatherDataRepository):
    """Repositorio simple con los datos entregados en la guía."""

    def get_observations(self) -> list[WeatherObservation]:
        return [
            WeatherObservation("06:00", 65, 40, 14),
            WeatherObservation("08:00", 70, 50, 16),
            WeatherObservation("10:00", 68, 45, 18),
            WeatherObservation("12:00", 60, 30, 22),
            WeatherObservation("14:00", 75, 70, 20),
            WeatherObservation("16:00", 85, 85, 18),
            WeatherObservation("18:00", 92, 95, 16),
            WeatherObservation("20:00", 88, 90, 17),
            WeatherObservation("22:00", 80, 75, 15),
        ]
