from .entities import ModelParameters
from .temperature import TemperatureFactorStrategy


class RainIndexModel:
    def __init__(
        self,
        parameters: ModelParameters,
        temperature_strategy: TemperatureFactorStrategy,
    ) -> None:
        self._parameters = parameters
        self._temperature_strategy = temperature_strategy
        self._validate_parameters()

    @property
    def parameters(self) -> ModelParameters:
        return self._parameters

    def calculate_temperature_factor(self, temperature_c: float) -> float:
        return self._temperature_strategy.calculate(temperature_c)

    def calculate_index(
        self,
        humidity: float,
        cloudiness: float,
        temperature_c: float,
    ) -> tuple[float, float]:
        tf = self.calculate_temperature_factor(temperature_c)
        index = (
            self._parameters.humidity_weight * humidity
            + self._parameters.cloudiness_weight * cloudiness
            + self._parameters.temperature_weight * tf
        )
        return tf, index

    @staticmethod
    def classify(index: float) -> str:
        if index < 0.40:
            return "Sin lluvia"
        if index < 0.60:
            return "Baja posibilidad"
        if index < 0.75:
            return "Lluvia probable"
        return "Lluvia"

    def _validate_parameters(self) -> None:
        if min(
            self._parameters.humidity_weight,
            self._parameters.cloudiness_weight,
            self._parameters.temperature_weight,
        ) < 0:
            raise ValueError("Los pesos no pueden ser negativos.")

        if abs(self._parameters.total_weight - 1.0) > 1e-9:
            raise ValueError("La suma de los pesos debe ser 1.0.")
