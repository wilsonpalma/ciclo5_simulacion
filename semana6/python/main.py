from controller.simulation_controller import SimulationController


def main():
    controller = SimulationController(
        seed=12345,
        multiplier=1664525,
        increment=1013904223,
        modulus=2**32
    )
    
    print("EJECUTANDO SIMULACION PRINCIPAL (n=10000)")
    print("=" * 50)
    controller.run_simulation(10000)
    
    print("\n\nCOMPARACION DE TIEMPOS DE EJECUCION")
    print("=" * 50)
    controller.run_comparison([1000, 10000, 100000, 1000000])
    
    print("\nSimulacion completada. Graficos guardados en carpeta 'plots/'.")


if __name__ == "__main__":
    main()