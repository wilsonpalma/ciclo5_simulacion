from typing import List, Dict, Any


class ConsoleView:
    def show_welcome(self):
        print("=" * 60)
        print("  VALIDACION ESTADISTICA DE NUMEROS PSEUDOALEATORIOS")
        print("  Pruebas Chi-Cuadrado y Kolmogorov-Smirnov")
        print("=" * 60)
        print()

    def show_lcg_params(self, seed: int, multiplier: int, increment: int, modulus: int, count: int):
        print("Parametros del Generador Congruencial Lineal (LCG):")
        print(f"  Semilla (X0):     {seed}")
        print(f"  Multiplicador (a): {multiplier}")
        print(f"  Incremento (c):    {increment}")
        print(f"  Modulo (m):        {modulus}")
        print(f"  Cantidad (n):      {count}")
        print()

    def show_generation_result(self, count: int, elapsed: float):
        print(f"Generados {count} numeros en {elapsed:.6f} segundos")
        print()

    def show_chi_square_results(self, results: Dict[str, Any]):
        print("-" * 50)
        print("RESULTADOS PRUEBA CHI-CUADRADO")
        print("-" * 50)
        print(f"Intervalos (k):           {len(results['observed_frequencies'])}")
        print(f"Frecuencia esperada (Ei): {results['expected_frequency']:.2f}")
        print()
        print("Frecuencias observadas por intervalo:")
        for i, obs in enumerate(results['observed_frequencies']):
            print(f"  Intervalo [{i*0.1:.1f}, {(i+1)*0.1:.1f}): {obs}")
        print()
        print(f"Estadistico Chi-Cuadrado: {results['chi2_statistic']:.6f}")
        print(f"Grados de libertad:       {results['degrees_of_freedom']}")
        print(f"Valor critico (alpha={results['alpha']}): {results['critical_value']:.6f}")
        print(f"Valor p:                  {results['p_value']:.6f}")
        print()
        print(f"Decision: {results['conclusion']}")
        print()

    def show_ks_results(self, results: Dict[str, Any]):
        print("-" * 50)
        print("RESULTADOS PRUEBA KOLMOGOROV-SMIRNOV")
        print("-" * 50)
        print(f"Tamaño de muestra (n):    {results['n']}")
        print(f"D+ maximo:                {results['d_plus_max']:.6f}")
        print(f"D- maximo:                {results['d_minus_max']:.6f}")
        print(f"Estadistico KS (D):       {results['ks_statistic']:.6f}")
        print(f"Valor p:                  {results['p_value']:.6f}")
        print(f"Alpha:                    {results['alpha']}")
        print()
        print(f"Decision: {results['conclusion']}")
        print()

    def show_comparison_table(self, data: List[Dict]):
        print("=" * 80)
        print("COMPARACION DE RESULTADOS PYTHON VS JAVA")
        print("=" * 80)
        print(f"{'N':>10} | {'Error':>10} | {'Tiempo Python (s)':>18} | {'Tiempo Java (s)':>16}")
        print("-" * 80)
        for row in data:
            print(f"{row['n']:>10} | {row['error']:>10.6f} | {row['python_time']:>18.6f} | {row['java_time']:>16.6f}")
        print()

    def show_control_questions(self):
        print("=" * 60)
        print("PREGUNTAS DE CONTROL")
        print("=" * 60)
        questions = [
            ("1. ¿Qué es la hipótesis nula?", 
             "Es la afirmación que se pone a prueba, en este caso H0: los números siguen una distribución uniforme U(0,1)."),
            ("2. ¿Qué representa el valor p?", 
             "Es la probabilidad de obtener resultados al menos tan extremos como los observados, asumiendo que H0 es verdadera. Un p-valor pequeño (< 0.05) sugiere evidencia contra H0."),
            ("3. ¿Qué significa rechazar H0?", 
             "Significa que hay evidencia estadística suficiente para concluir que los números NO siguen una distribución uniforme."),
            ("4. ¿Qué diferencia existe entre Chi-Cuadrado y KS?", 
             "Chi-Cuadrado agrupa datos en intervalos y compara frecuencias; KS compara la función de distribución acumulada empírica con la teórica sin agrupar. KS es más sensible a diferencias en las colas."),
            ("5. ¿Por qué una prueba estadística no demuestra que un generador sea verdaderamente aleatorio?", 
             "Las pruebas solo detectan desviaciones de patrones específicos. Un generador puede pasar ciertas pruebas pero fallar en otras. La aleatoriedad verdadera no puede probarse, solo puede fallarse en detectar no-aleatoriedad.")
        ]
        for q, a in questions:
            print(f"\n{q}\n   {a}")
        print()


    def show_error(self, message: str):
        print(f"ERROR: {message}")
        print()