import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict, Any
import os


class PlotView:
    def __init__(self, output_dir: str = "plots"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def plot_chi_square(self, results: Dict[str, Any], filename: str = "chi_square.png"):
        observed = results['observed_frequencies']
        expected = results['expected_frequency']
        intervals = len(observed)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        x = np.arange(intervals)
        width = 0.35
        
        ax.bar(x - width/2, observed, width, label='Frecuencia Observada', color='steelblue', alpha=0.8)
        ax.bar(x + width/2, [expected] * intervals, width, label='Frecuencia Esperada', color='coral', alpha=0.8)
        
        ax.set_xlabel('Intervalos')
        ax.set_ylabel('Frecuencia')
        ax.set_title(f"Prueba Chi-Cuadrado (χ² = {results['chi2_statistic']:.4f}, p = {results['p_value']:.6f})")
        ax.set_xticks(x)
        ax.set_xticklabels([f'[{i*0.1:.1f},{(i+1)*0.1:.1f})' for i in range(intervals)])
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, filename), dpi=150)
        plt.close()

    def plot_ks(self, results: Dict[str, Any], filename: str = "kolmogorov_smirnov.png"):
        sorted_nums = results['sorted_numbers']
        ecdf = results['ecdf_values']
        theoretical = results['theoretical_cdf']
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        ax1.plot(sorted_nums, ecdf, 'b-', label='ECDF Empírica', linewidth=1.5)
        ax1.plot(sorted_nums, theoretical, 'r--', label='CDF Teórica U(0,1)', linewidth=1.5)
        ax1.fill_between(sorted_nums, ecdf, theoretical, alpha=0.2, color='gray')
        ax1.set_xlabel('x')
        ax1.set_ylabel('F(x)')
        ax1.set_title('Distribuciones Acumuladas: Empírica vs Teórica')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        n = len(sorted_nums)
        d_plus = np.array(ecdf) - np.array(theoretical)
        d_minus = np.array(theoretical) - np.array([(i) / n for i in range(n)])
        
        ax2.plot(sorted_nums, d_plus, 'g-', label='D+ = F_n(x) - F(x)', linewidth=1)
        ax2.plot(sorted_nums, d_minus, 'm-', label='D- = F(x) - F_n(x-)', linewidth=1)
        ax2.axhline(y=results['d_plus_max'], color='g', linestyle='--', alpha=0.5, label=f'Max D+ = {results["d_plus_max"]:.4f}')
        ax2.axhline(y=results['d_minus_max'], color='m', linestyle='--', alpha=0.5, label=f'Max D- = {results["d_minus_max"]:.4f}')
        ax2.set_xlabel('x')
        ax2.set_ylabel('Diferencia')
        ax2.set_title(f'Diferencias (D = {results["ks_statistic"]:.4f}, p = {results["p_value"]:.6f})')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, filename), dpi=150)
        plt.close()

    def plot_histogram(self, numbers: List[float], filename: str = "histogram.png", bins: int = 20):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(numbers, bins=bins, density=True, alpha=0.7, color='steelblue', edgecolor='black', label='Histograma')
        ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2, label='Uniforme teórica (densidad=1)')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Densidad')
        ax.set_title('Histograma de números pseudoaleatorios generados')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, filename), dpi=150)
        plt.close()