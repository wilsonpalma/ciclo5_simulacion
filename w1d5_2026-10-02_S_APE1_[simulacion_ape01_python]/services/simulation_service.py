from domain.entities import SimulationResult
from domain.rain_model import RainIndexModel
from infrastructure.data_repository import WeatherDataRepository


class SimulationService:
    def __init__(self, repository: WeatherDataRepository, model: RainIndexModel) -> None:
        self._repository = repository
        self._model = model

    def run(self) -> list[SimulationResult]:
        results: list[SimulationResult] = []

        for observation in self._repository.get_observations():
            tf, index = self._model.calculate_index(
                observation.humidity,
                observation.cloudiness,
                observation.temperature_c,
            )
            results.append(
                SimulationResult(
                    observation=observation,
                    temperature_factor=tf,
                    index=index,
                    state=self._model.classify(index),
                )
            )

        return results
