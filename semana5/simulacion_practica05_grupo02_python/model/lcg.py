"""Modelo del Generador Congruencial Lineal (LCG)."""

from typing import List, Tuple
import json


class LCG:
    """Generador Congruencial Lineal con parámetros estándar."""

    def __init__(
        self,
        a: int = 1664525,
        c: int = 1013904223,
        m: int = 2**32,
        seed: int = 12345
    ):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed
        self._state = seed

    def next(self) -> int:
        """Genera el siguiente valor entero."""
        self._state = (self.a * self._state + self.c) % self.m
        return self._state

    def next_normalized(self) -> float:
        """Genera el siguiente valor normalizado [0, 1)."""
        return self.next() / self.m

    def generate_sequence(self, n: int) -> List[int]:
        """Genera una secuencia de n valores enteros."""
        return [self.next() for _ in range(n)]

    def generate_normalized_sequence(self, n: int) -> List[float]:
        """Genera una secuencia de n valores normalizados."""
        return [self.next_normalized() for _ in range(n)]

    def reset(self, seed: int = None):
        """Reinicia el generador con una nueva semilla."""
        if seed is not None:
            self.seed = seed
        self._state = self.seed

    def get_parameters(self) -> dict:
        """Retorna los parámetros del generador."""
        return {
            "a": self.a,
            "c": self.c,
            "m": self.m,
            "seed": self.seed
        }

    def analyze_period(self, max_iterations: int = 100000) -> int:
        """
        Analiza el período del generador detectando el primer valor repetido.
        Retorna el período encontrado o -1 si no se detecta en max_iterations.
        """
        seen = {}
        self.reset()
        for i in range(max_iterations):
            val = self.next()
            if val in seen:
                return i - seen[val]
            seen[val] = i
        return -1

    def to_json(self) -> str:
        """Serializa el estado del generador a JSON."""
        return json.dumps({
            "a": self.a,
            "c": self.c,
            "m": self.m,
            "seed": self.seed,
            "current_state": self._state
        })

    @classmethod
    def from_json(cls, json_str: str) -> 'LCG':
        """Crea un generador LCG desde JSON."""
        data = json.loads(json_str)
        lcg = cls(data["a"], data["c"], data["m"], data["seed"])
        lcg._state = data["current_state"]
        return lcg


def compare_sequences(seq1: List[float], seq2: List[float], n: int = 20) -> List[Tuple[int, float, float, bool]]:
    """
    Compara las primeras n observaciones de dos secuencias.
    Retorna lista de tuplas: (índice, valor1, valor2, son_iguales).
    """
    results = []
    for i in range(min(n, len(seq1), len(seq2))):
        equal = abs(seq1[i] - seq2[i]) < 1e-10
        results.append((i, seq1[i], seq2[i], equal))
    return results