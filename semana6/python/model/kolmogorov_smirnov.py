import math
from scipy import stats
from typing import List, Tuple


class KolmogorovSmirnovTest:
    def __init__(self, alpha: float = 0.05):
        self.alpha = alpha

    def test(self, numbers: List[float]) -> dict:
        n = len(numbers)
        sorted_numbers = sorted(numbers)
        
        d_plus_max = 0.0
        d_minus_max = 0.0
        
        d_plus_list = []
        d_minus_list = []
        fn_list = []
        fo_list = []
        
        for i, x in enumerate(sorted_numbers, 1):
            fn = i / n
            fo = x
            
            d_plus = fn - fo
            d_minus = fo - (i - 1) / n
            
            d_plus_max = max(d_plus_max, d_plus)
            d_minus_max = max(d_minus_max, d_minus)
            
            d_plus_list.append(d_plus)
            d_minus_list.append(d_minus)
            fn_list.append(fn)
            fo_list.append(fo)
        
        d_stat = max(d_plus_max, d_minus_max)
        
        try:
            p_value = 1 - stats.kstest(sorted_numbers, 'uniform').pvalue
        except:
            p_value = self._approx_p_value(d_stat, n)
        
        reject_h0 = p_value < self.alpha
        
        return {
            "n": n,
            "d_plus_max": d_plus_max,
            "d_minus_max": d_minus_max,
            "ks_statistic": d_stat,
            "p_value": p_value,
            "alpha": self.alpha,
            "reject_h0": reject_h0,
            "conclusion": "Se rechaza H0: Los numeros no siguen distribucion uniforme" if reject_h0
                         else "No se rechaza H0: Los numeros siguen distribucion uniforme",
            "ecdf_values": fn_list,
            "theoretical_cdf": fo_list,
            "sorted_numbers": sorted_numbers
        }
    
    def _approx_p_value(self, d: float, n: int) -> float:
        lambda_ks = d * math.sqrt(n)
        if lambda_ks <= 0:
            return 1.0
        sum_term = 0.0
        for k in range(1, 100):
            term = 2 * (-1) ** (k - 1) * math.exp(-2 * k * k * lambda_ks * lambda_ks)
            sum_term += term
            if abs(term) < 1e-10:
                break
        return sum_term