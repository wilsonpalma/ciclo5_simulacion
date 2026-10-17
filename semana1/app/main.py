from app.model_factory import RainModelFactory
from domain.entities import SimulationResult
from infrastructure.data_repository import InMemoryWeatherDataRepository
from services.simulation_service import SimulationService
from visualization.plotter import SimulationPlotter


# Cambia estos tres valores para experimentar con el "modelo ajustado".
# Deben sumar 1.0. La guía no especifica qué nuevos coeficientes utilizar.
ADJUSTED_WEIGHTS = {
    "humidity_weight": 0.4,
    "cloudiness_weight": 0.4,
    "temperature_weight": 0.2,
}


def print_results(title: str, results: list[SimulationResult]) -> None:
    print(f"\n{title}")
    print("-" * 92)
    print(
        f"{'Hora':<8}{'Hum.':>8}{'Nub.':>8}{'Temp.':>9}"
        f"{'H':>9}{'N':>9}{'Tf':>9}{'Índice':>10}{'Estado':>16}"
    )
    print("-" * 92)

    for result in results:
        obs = result.observation
        print(
            f"{obs.hour:<8}"
            f"{obs.humidity_percent:>8.0f}"
            f"{obs.cloudiness_percent:>8.0f}"
            f"{obs.temperature_c:>9.1f}"
            f"{obs.humidity:>9.2f}"
            f"{obs.cloudiness:>9.2f}"
            f"{result.temperature_factor:>9.2f}"
            f"{result.index:>10.2f}"
            f"{result.state:>16}"
        )


def main() -> None:
    repository = InMemoryWeatherDataRepository()
    plotter = SimulationPlotter()

    baseline_model = RainModelFactory.create_baseline()
    baseline_service = SimulationService(repository, baseline_model)
    baseline_results = baseline_service.run()

    adjusted_model = RainModelFactory.create_adjusted(**ADJUSTED_WEIGHTS)
    adjusted_service = SimulationService(repository, adjusted_model)
    adjusted_results = adjusted_service.run()

    print_results("MODELO BASE", baseline_results)
    print_results("MODELO AJUSTADO", adjusted_results)

    plotter.plot_inputs(baseline_results)
    plotter.plot_model(baseline_results, "Índice de lluvia - Modelo base")
    plotter.plot_model(adjusted_results, "Índice de lluvia - Modelo ajustado")
    plotter.plot_comparison(baseline_results, adjusted_results)


if __name__ == "__main__":
    main()
