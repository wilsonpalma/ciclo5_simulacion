from typing import List, Dict, Any
from model.lcg import LCG
from model.chi_square import ChiSquareTest
from model.kolmogorov_smirnov import KolmogorovSmirnovTest
from view.console_view import ConsoleView
from view.plot_view import PlotView


class SimulationController:
    def __init__(self, seed: int = 12345, multiplier: int = 1664525, 
                 increment: int = 1013904223, modulus: int = 2**32):
        self.lcg = LCG(seed, multiplier, increment, modulus)
        self.chi_square = ChiSquareTest(intervals=10, alpha=0.05)
        self.ks_test = KolmogorovSmirnovTest(alpha=0.05)
        self.console = ConsoleView()
        self.plotter = PlotView()

    def run_simulation(self, count: int = 10000) -> Dict[str, Any]:
        self.console.show_welcome()
        self.console.show_lcg_params(
            self.lcg.seed, self.lcg.multiplier, 
            self.lcg.increment, self.lcg.modulus, count
        )
        
        numbers, gen_time = self.lcg.generate(count)
        self.console.show_generation_result(count, gen_time)
        
        chi2_results = self.chi_square.test(numbers)
        self.console.show_chi_square_results(chi2_results)
        
        ks_results = self.ks_test.test(numbers)
        self.console.show_ks_results(ks_results)
        
        self.plotter.plot_chi_square(chi2_results)
        self.plotter.plot_ks(ks_results)
        self.plotter.plot_histogram(numbers)
        
        self.console.show_control_questions()
        
        return {
            "numbers": numbers,
            "generation_time": gen_time,
            "chi_square": chi2_results,
            "kolmogorov_smirnov": ks_results
        }

    def run_comparison(self, sample_sizes: List[int] = None) -> List[Dict]:
        if sample_sizes is None:
            sample_sizes = [1000, 10000, 100000, 1000000]
        
        comparison_data = []
        
        for n in sample_sizes:
            self.lcg.reset()
            numbers, py_time = self.lcg.generate(n)
            
            chi2_results = self.chi_square.test(numbers)
            ks_results = self.ks_test.test(numbers)
            
            error = abs(chi2_results['p_value'] - 0.5)
            
            comparison_data.append({
                "n": n,
                "error": error,
                "python_time": py_time,
                "java_time": 0.0
            })
        
        self.console.show_comparison_table(comparison_data)
        return comparison_data