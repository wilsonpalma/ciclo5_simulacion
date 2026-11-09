"""Controlador para la simulación LCG."""

from typing import List, Tuple, Optional
from model.lcg import LCG, compare_sequences
import json


class LCGController:
    """Controlador que coordina la generación y análisis de secuencias LCG."""

    def __init__(self):
        self.lcg_python = LCG()
        self.results = {}

    def run_full_simulation(self, n: int = 10000) -> dict:
        """
        Ejecuta la simulación completa:
        1. Genera 10,000 valores
        2. Compara primeras 20 observaciones
        3. Analiza período
        4. Cambia semilla y compara
        """
        self.lcg_python.reset(12345)
        sequence = self.lcg_python.generate_normalized_sequence(n)

        first_20 = sequence[:20]

        self.lcg_python.reset(12345)
        period = self.lcg_python.analyze_period(50000)

        self.lcg_python.reset(99999)
        sequence_new_seed = self.lcg_python.generate_normalized_sequence(n)
        first_20_new_seed = sequence_new_seed[:20]

        self.results = {
            "parameters": self.lcg_python.get_parameters(),
            "n_generated": n,
            "first_20_original": first_20,
            "first_20_new_seed": first_20_new_seed,
            "period": period,
            "full_sequence": sequence
        }
        return self.results

    def get_first_n_observations(self, n: int = 20) -> List[float]:
        """Retorna las primeras n observaciones de la secuencia actual."""
        if "first_20_original" in self.results:
            return self.results["first_20_original"][:n]
        self.lcg_python.reset(12345)
        return self.lcg_python.generate_normalized_sequence(n)[:n]

    def compare_with_java_reference(self, java_sequence: List[float], n: int = 20) -> List[Tuple[int, float, float, bool]]:
        """
        Compara la secuencia Python con una secuencia de referencia Java.
        Retorna lista de tuplas: (índice, py_val, java_val, son_iguales).
        """
        py_sequence = self.get_first_n_observations(n)
        return compare_sequences(py_sequence, java_sequence, n)

    def change_seed_and_generate(self, new_seed: int, n: int = 10000) -> dict:
        """Cambia la semilla y genera nueva secuencia."""
        self.lcg_python.reset(new_seed)
        sequence = self.lcg_python.generate_normalized_sequence(n)
        return {
            "seed": new_seed,
            "first_20": sequence[:20],
            "full_sequence": sequence
        }

    def export_results_json(self, filepath: str):
        """Exporta los resultados a JSON."""
        export_data = {
            "parameters": self.results.get("parameters", {}),
            "n_generated": self.results.get("n_generated", 0),
            "first_20_original": self.results.get("first_20_original", []),
            "first_20_new_seed": self.results.get("first_20_new_seed", []),
            "period": self.results.get("period", -1)
        }
        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2)

    def get_results_summary(self) -> str:
        """Genera un resumen textual de los resultados."""
        if not self.results:
            return "No hay resultados. Ejecute run_full_simulation() primero."

        lines = [
            "=== RESUMEN DE RESULTADOS LCG ===",
            f"Parámetros: a={self.results['parameters']['a']}, "
            f"c={self.results['parameters']['c']}, "
            f"m={self.results['parameters']['m']}, "
            f"seed={self.results['parameters']['seed']}",
            f"Valores generados: {self.results['n_generated']}",
            f"Período detectado: {self.results['period']}",
            "",
            "Primeras 20 observaciones (seed=12345):"
        ]
        for i, val in enumerate(self.results['first_20_original']):
            lines.append(f"  U({i+1}) = {val:.10f}")

        lines.append("")
        lines.append("Primeras 20 observaciones (seed=99999):")
        for i, val in enumerate(self.results['first_20_new_seed']):
            lines.append(f"  U({i+1}) = {val:.10f}")

        return "\n".join(lines)

    def get_full_sequence(self) -> List[float]:
        """Retorna la secuencia completa generada."""
        if "full_sequence" in self.results:
            return self.results["full_sequence"]
        return []

    def get_sequence_for_plotting(self, max_points: int = 1000) -> List[float]:
        """
        Retorna una submuestra de la secuencia para graficar.
        Si la secuencia es muy grande, toma puntos espaciados uniformemente.
        """
        seq = self.get_full_sequence()
        if not seq:
            self.lcg_python.reset(12345)
            seq = self.lcg_python.generate_normalized_sequence(10000)
        
        if len(seq) <= max_points:
            return seq
        
        # Submuestreo uniforme
        step = len(seq) // max_points
        return [seq[i] for i in range(0, len(seq), step)][:max_points]