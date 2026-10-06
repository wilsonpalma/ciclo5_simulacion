from dataclasses import dataclass


@dataclass(frozen=True)
class WeatherObservation:
    hour: str
    humidity_percent: float
    cloudiness_percent: float
    temperature_c: float

    @property
    def humidity(self) -> float:
        return self.humidity_percent / 100.0

    @property
    def cloudiness(self) -> float:
        return self.cloudiness_percent / 100.0


@dataclass(frozen=True)
class ModelParameters:
    humidity_weight: float = 0.5
    cloudiness_weight: float = 0.3
    temperature_weight: float = 0.2

    @property
    def total_weight(self) -> float:
        return (
            self.humidity_weight
            + self.cloudiness_weight
            + self.temperature_weight
        )


@dataclass(frozen=True)
class SimulationResult:
    observation: WeatherObservation
    temperature_factor: float
    index: float
    state: str
