import controller.SimulationController;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        SimulationController controller = new SimulationController(
            12345,
            1664525,
            1013904223L,
            (1L << 32)
        );
        
        System.out.println("EJECUTANDO SIMULACION PRINCIPAL (n=10000)");
        System.out.println("=".repeat(50));
        controller.runSimulation(10000);
        
        System.out.println("\n\nCOMPARACION DE TIEMPOS DE EJECUCION");
        System.out.println("=".repeat(50));
        
        List<Integer> sizes = new ArrayList<>();
        sizes.add(1000);
        sizes.add(10000);
        sizes.add(100000);
        sizes.add(1000000);
        
        controller.runComparison(sizes);
        
        System.out.println("\nSimulacion completada.");
    }
}