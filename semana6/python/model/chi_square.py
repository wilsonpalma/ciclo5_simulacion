import math
from scipy import stats
from typing import List, Tuple


class ChiSquareTest:
    def __init__(self, intervals: int = 10, alpha: float = 0.05):
        self.intervals = intervals
        self.alpha = alpha

    def test(self, numbers: List[float]) -> dict:
        n = len(numbers)
        expected_freq = n / self.intervals
        
        observed = [0] * self.intervals
        for num in numbers:
            idx = min(int(num * self.intervals), self.intervals - 1)
            observed[idx] += 1
        
        chi2_stat = sum((o - expected_freq) ** 2 / expected_freq for o in observed)
        dof = self.intervals - 1
        p_value = 1 - stats.chi2.cdf(chi2_stat, dof)
        
        critical_value = stats.chi2.ppf(1 - self.alpha, dof)
        reject_h0 = p_value < self.alpha
        
        return {
            "observed_frequencies": observed,
            "expected_frequency": expected_freq,
            "chi2_statistic": chi2_stat,
            "degrees_of_freedom": dof,
            "p_value": p_value,
            "critical_value": critical_value,
            "alpha": self.alpha,
            "reject_h0": reject_h0,
            "conclusion": "Se rechaza H0: Los numeros no siguen distribucion uniforme" if reject_h0 
                         else "No se rechaza H0: Los numeros siguen distribucion uniforme"
        }