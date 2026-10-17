import matplotlib.pyplot as plt
import numpy as np

from domain.entities import SimulationResult


class SimulationPlotter:
    def plot_inputs(self, results: list[SimulationResult]) -> None:
        hours = [result.observation.hour for result in results]
        humidity = [result.observation.humidity_percent for result in results]
        cloudiness = [result.observation.cloudiness_percent for result in results]
        temperature = [result.observation.temperature_c for result in results]

        x = np.arange(len(hours))

        plt.figure(figsize=(10, 5))
        plt.plot(x, humidity, marker="o", label="Humedad (%)")
        plt.plot(x, cloudiness, marker="o", label="Nubosidad (%)")
        plt.plot(x, temperature, marker="o", label="Temperatura (°C)")
        plt.xticks(x, hours)
        plt.xlabel("Hora")
        plt.ylabel("Valor")
        plt.title("Variables de entrada")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_model(self, results: list[SimulationResult], title: str) -> None:
        hours = [result.observation.hour for result in results]
        index_values = [result.index for result in results]
        x = np.arange(len(hours))

        plt.figure(figsize=(10, 5))
        plt.plot(x, index_values, marker="o", label="Índice I")
        plt.axhline(0.40, linestyle="--", label="0.40")
        plt.axhline(0.60, linestyle="--", label="0.60")
        plt.axhline(0.75, linestyle="--", label="0.75")
        plt.xticks(x, hours)
        plt.ylim(0, 1)
        plt.xlabel("Hora")
        plt.ylabel("Índice")
        plt.title(title)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_comparison(
        self,
        baseline_results: list[SimulationResult],
        adjusted_results: list[SimulationResult],
    ) -> None:
        hours = [result.observation.hour for result in baseline_results]
        baseline = [result.index for result in baseline_results]
        adjusted = [result.index for result in adjusted_results]
        x = np.arange(len(hours))

        width = 0.38
        plt.figure(figsize=(10, 5))
        plt.bar(x - width / 2, baseline, width, label="Modelo base")
        plt.bar(x + width / 2, adjusted, width, label="Modelo ajustado")
        plt.axhline(0.40, linestyle="--")
        plt.axhline(0.60, linestyle="--")
        plt.axhline(0.75, linestyle="--")
        plt.xticks(x, hours)
        plt.ylim(0, 1)
        plt.xlabel("Hora")
        plt.ylabel("Índice")
        plt.title("Comparación del índice")
        plt.grid(True, axis="y", alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()
