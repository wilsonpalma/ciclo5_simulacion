"""Vista CLI para la simulación LCG."""

from controller.lcg_controller import LCGController


class LCGView:
    """Interfaz de línea de comandos para interactuar con la simulación."""

    def __init__(self):
        self.controller = LCGController()

    def display_menu(self):
        """Muestra el menú principal."""
        print("\n" + "=" * 50)
        print("  SIMULACIÓN LCG - GENERADOR CONGRUENCIAL LINEAL")
        print("=" * 50)
        print("1. Ejecutar simulación completa (10,000 valores)")
        print("2. Ver primeras N observaciones")
        print("3. Cambiar semilla y generar nueva secuencia")
        print("4. Comparar con secuencia de referencia (Java)")
        print("5. Exportar resultados a JSON")
        print("6. Mostrar resumen de resultados")
        print("7. Graficar secuencia (ASCII)")
        print("0. Salir")
        print("-" * 50)

    def run_simulation(self):
        """Ejecuta la simulación completa."""
        print("\nEjecutando simulación completa...")
        results = self.controller.run_full_simulation(10000)
        print(f"Generados {results['n_generated']} valores.")
        print(f"Período detectado: {results['period']}")
        self.display_first_n(20)

    def display_first_n(self, n: int = 20):
        """Muestra las primeras N observaciones."""
        print(f"\n--- Primeras {n} observaciones ---")
        print(f"{'Índice':>6} | {'Valor':>12}")
        print("-" * 22)
        for i, val in enumerate(self.controller.get_first_n_observations(n)):
            print(f"{i+1:>6} | {val:.10f}")

    def change_seed(self):
        """Permite cambiar la semilla."""
        try:
            seed_input = input("\nIngrese nueva semilla (entero): ").strip()
            new_seed = int(seed_input)
            n_input = input("Cantidad de valores a generar [10000]: ").strip()
            n = int(n_input) if n_input else 10000

            result = self.controller.change_seed_and_generate(new_seed, n)
            print(f"\nGenerados {n} valores con semilla {new_seed}")
            self.display_first_n(20)
        except ValueError:
            print("Error: La semilla debe ser un número entero.")

    def compare_with_java(self):
        """Compara con una secuencia de referencia Java."""
        print("\n--- Comparación con Java ---")
        print("Ingrese los primeros 20 valores de Java (separados por espacio o coma):")
        java_input = input("> ").strip()

        try:
            java_values = [float(x) for x in java_input.replace(',', ' ').split()]
            if len(java_values) < 20:
                print(f"Advertencia: Se esperaban 20 valores, recibió {len(java_values)}")

            comparison = self.controller.compare_with_java_reference(java_values, 20)
            print(f"\n{'Índice':>5} | {'Python':>12} | {'Java':>12} | {'Igual':>5}")
            print("-" * 42)
            all_equal = True
            for idx, py_val, java_val, equal in comparison:
                status = "Sí" if equal else "No"
                if not equal:
                    all_equal = False
                print(f"{idx+1:>5} | {py_val:.10f} | {java_val:.10f} | {status:>5}")

            if all_equal:
                print("\n✓ Las secuencias son IDÉNTICAS (mismo algoritmo, mismos parámetros)")
            else:
                print("\n✗ Las secuencias DIFIEREN (revisar implementación o parámetros)")

        except ValueError:
            print("Error: Formato inválido. Use números separados por espacios o comas.")

    def export_json(self):
        """Exporta resultados a JSON."""
        filepath = input("\nRuta del archivo JSON [resultados_lcg.json]: ").strip()
        if not filepath:
            filepath = "resultados_lcg.json"
        self.controller.export_results_json(filepath)
        print(f"Resultados exportados a: {filepath}")

    def show_summary(self):
        """Muestra el resumen completo."""
        print(self.controller.get_results_summary())

    def plot_sequence(self):
        """Grafica la secuencia usando ASCII art en consola (compatibles con Windows)."""
        print("\n--- Grafico de la Secuencia LCG (ASCII) ---")
        print("Mostrando dispersion de U(n) vs n (submuestra de 500 puntos)")
        print()
        
        sequence = self.controller.get_sequence_for_plotting(500)
        if not sequence:
            print("No hay datos para graficar. Ejecute la simulacion primero (opcion 1).")
            return
        
        # Configuracion del grafico
        width = 70
        height = 20
        
        # Crear canvas vacio
        canvas = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Dibujar ejes (usar caracteres ASCII compatibles)
        # Eje Y (vertical) - izquierda
        for y in range(height):
            canvas[y][0] = '|'
        # Eje X (horizontal) - abajo
        for x in range(width):
            canvas[height-1][x] = '-'
        canvas[height-1][0] = '+'
        
        # Escalar y plotear puntos
        n_points = len(sequence)
        for i, val in enumerate(sequence):
            # Mapear indice a coordenada X (1 a width-1)
            x = 1 + int((i / max(1, n_points - 1)) * (width - 2))
            # Mapear valor [0,1) a coordenada Y (height-2 a 0)
            y = height - 2 - int(val * (height - 2))
            
            # Asegurar limites
            x = max(1, min(width - 1, x))
            y = max(0, min(height - 2, y))
            
            # Marcar punto (si hay colision, usar '*')
            if canvas[y][x] == ' ':
                canvas[y][x] = '*'
            elif canvas[y][x] == '*':
                canvas[y][x] = '+'
            else:
                canvas[y][x] = '#'
        
        # Etiquetas eje Y
        y_labels = [1.0, 0.75, 0.5, 0.25, 0.0]
        for label_val in y_labels:
            y_pos = height - 2 - int(label_val * (height - 2))
            if 0 <= y_pos < height - 1:
                label = f"{label_val:.2f}"
                # Escribir etiqueta a la izquierda del eje Y
                for j, ch in enumerate(label):
                    if 5 - len(label) + j >= 0:
                        canvas[y_pos][5 - len(label) + j] = ch
        
        # Imprimir canvas
        for y in range(height):
            line = ''.join(canvas[y])
            # Recortar espacios al final
            print(line.rstrip())
        
        # Etiquetas eje X
        print(f"{'0':<6}{'n (indice)':<{width-12}}{n_points:>6}")
        print(f"{'U(n)':<6}{'':<{width-12}}[0, 1)")
        print()
        print(f"Puntos graficados: {n_points} (submuestra de {self.controller.results.get('n_generated', 'N/A')} totales)")
        print("Leyenda: * = punto, + = superposicion, # = multiples puntos")

    def run(self):
        """Bucle principal de la aplicación."""
        while True:
            self.display_menu()
            choice = input("Seleccione una opción: ").strip()

            if choice == "1":
                self.run_simulation()
            elif choice == "2":
                try:
                    n = int(input("Cantidad de observaciones [20]: ").strip() or "20")
                    self.display_first_n(n)
                except ValueError:
                    print("Error: Ingrese un número válido.")
            elif choice == "3":
                self.change_seed()
            elif choice == "4":
                self.compare_with_java()
            elif choice == "5":
                self.export_json()
            elif choice == "6":
                self.show_summary()
            elif choice == "7":
                self.plot_sequence()
            elif choice == "0":
                print("\n¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")


def main():
    """Punto de entrada principal."""
    view = LCGView()
    view.run()


if __name__ == "__main__":
    main()