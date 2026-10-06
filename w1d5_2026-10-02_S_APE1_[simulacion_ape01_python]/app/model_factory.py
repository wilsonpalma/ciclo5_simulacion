from domain.entities import ModelParameters
from domain.rain_model import RainIndexModel
from domain.temperature import LinearInterpolationTemperatureStrategy


class RainModelFactory:
    """Factory para construir distintas configuraciones del modelo."""

    @staticmethod
    def create_baseline() -> RainIndexModel:
        return RainIndexModel(
            parameters=ModelParameters(0.5, 0.3, 0.2),
            temperature_strategy=LinearInterpolationTemperatureStrategy(),
        )

    @staticmethod
    def create_adjusted(
        humidity_weight: float = 0.5,
        cloudiness_weight: float = 0.3,
        temperature_weight: float = 0.2,
    ) -> RainIndexModel:
        return RainIndexModel(
            parameters=ModelParameters(
                humidity_weight,
                cloudiness_weight,
                temperature_weight,
            ),
            temperature_strategy=LinearInterpolationTemperatureStrategy(),
        )
