import time
from typing import List, Tuple


class LCG:
    def __init__(self, seed: int = 1, multiplier: int = 1664525, increment: int = 1013904223, modulus: int = 2**32):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        self.current = seed

    def generate(self, count: int) -> Tuple[List[float], float]:
        start_time = time.perf_counter()
        numbers = []
        for _ in range(count):
            self.current = (self.multiplier * self.current + self.increment) % self.modulus
            numbers.append(self.current / self.modulus)
        elapsed = time.perf_counter() - start_time
        return numbers, elapsed

    def reset(self, seed: int = None):
        if seed is not None:
            self.seed = seed
        self.current = self.seed