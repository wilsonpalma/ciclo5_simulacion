package view;

import controller.LCGController;
import controller.LCGController.ComparisonResult;
import controller.LCGController.SimulationResults;
import java.util.List;
import java.util.Scanner;

/**
 * Vista CLI para la simulación LCG.
 * Interfaz de línea de comandos para interactuar con la simulación.
 */
public class LCGView {
    private final LCGController controller;
    private final Scanner scanner;

    public LCGView() {
        this.controller = new LCGController();
        this.scanner = new Scanner(System.in);
    }

    /**
     * Muestra el menú principal.
     */
    public void displayMenu() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println("  SIMULACIÓN LCG - GENERADOR CONGRUENCIAL LINEAL (JAVA)");
        System.out.println("=".repeat(50));
        System.out.println("1. Ejecutar simulación completa (10,000 valores)");
        System.out.println("2. Ver primeras N observaciones");
        System.out.println("3. Cambiar semilla y generar nueva secuencia");
        System.out.println("4. Comparar con secuencia de referencia (Python)");
        System.out.println("5. Exportar resultados a JSON");
        System.out.println("6. Mostrar resumen de resultados");
        System.out.println("7. Graficar secuencia (ASCII)");
        System.out.println("0. Salir");
        System.out.println("-".repeat(50));
    }

    /**
     * Ejecuta la simulación completa.
     */
    public void runSimulation() {
        System.out.println("\nEjecutando simulación completa...");
        SimulationResults results = controller.runFullSimulation(10000);
        System.out.println("Generados " + results.nGenerated + " valores.");
        System.out.println("Período detectado: " + results.period);
        displayFirstN(20);
    }

    /**
     * Muestra las primeras N observaciones.
     */
    public void displayFirstN(int n) {
        double[] values = controller.getFirstNObservations(n);
        System.out.println("\n--- Primeras " + n + " observaciones ---");
        System.out.printf("%6s | %12s%n", "Índice", "Valor");
        System.out.println("-".repeat(22));
        for (int i = 0; i < values.length; i++) {
            System.out.printf("%6d | %.10f%n", i + 1, values[i]);
        }
    }

    /**
     * Permite cambiar la semilla.
     */
    public void changeSeed() {
        try {
            System.out.print("\nIngrese nueva semilla (entero): ");
            String seedInput = scanner.nextLine().trim();
            long newSeed = Long.parseLong(seedInput);

            System.out.print("Cantidad de valores a generar [10000]: ");
            String nInput = scanner.nextLine().trim();
            int n = nInput.isEmpty() ? 10000 : Integer.parseInt(nInput);

            SimulationResults result = controller.changeSeedAndGenerate(newSeed, n);
            System.out.println("\nGenerados " + n + " valores con semilla " + newSeed);
            displayFirstN(20);
        } catch (NumberFormatException e) {
            System.out.println("Error: La semilla debe ser un número entero.");
        }
    }

    /**
     * Compara con una secuencia de referencia (Python).
     */
    public void compareWithReference() {
        System.out.println("\n--- Comparación con Python ---");
        System.out.println("Ingrese los primeros 20 valores de Python (separados por espacio o coma):");
        System.out.print("> ");
        String input = scanner.nextLine().trim();

        try {
            String[] parts = input.replace(',', ' ').split("\\s+");
            double[] refValues = new double[parts.length];
            for (int i = 0; i < parts.length; i++) {
                refValues[i] = Double.parseDouble(parts[i]);
            }
            
            if (refValues.length < 20) {
                System.out.println("Advertencia: Se esperaban 20 valores, recibió " + refValues.length);
            }

            List<ComparisonResult> comparison = controller.compareWithReference(refValues, 20);
            
            System.out.printf("%n%5s | %12s | %12s | %5s%n", "Índice", "Java", "Python", "Igual");
            System.out.println("-".repeat(42));
            boolean allEqual = true;
            for (ComparisonResult cr : comparison) {
                String status = cr.equal ? "Sí" : "No";
                if (!cr.equal) allEqual = false;
                System.out.printf("%5d | %.10f | %.10f | %5s%n", 
                    cr.index + 1, cr.value1, cr.value2, status);
            }

            if (allEqual) {
                System.out.println("\n✓ Las secuencias son IDÉNTICAS (mismo algoritmo, mismos parámetros)");
            } else {
                System.out.println("\n✗ Las secuencias DIFIEREN (revisar implementación o parámetros)");
            }

        } catch (NumberFormatException e) {
            System.out.println("Error: Formato inválido. Use números separados por espacios o comas.");
        }
    }

    /**
     * Exporta resultados a JSON.
     */
    public void exportJson() {
        System.out.print("\nRuta del archivo JSON [resultados_lcg.json]: ");
        String filepath = scanner.nextLine().trim();
        if (filepath.isEmpty()) {
            filepath = "resultados_lcg.json";
        }
        try {
            controller.exportResultsJson(filepath);
            System.out.println("Resultados exportados a: " + filepath);
        } catch (Exception e) {
            System.out.println("Error al exportar: " + e.getMessage());
        }
    }

    /**
     * Muestra el resumen completo.
     */
    public void showSummary() {
        System.out.println(controller.getResultsSummary());
    }

    /**
     * Grafica la secuencia usando ASCII art en consola (compatibles con Windows).
     */
    public void plotSequence() {
        System.out.println("\n--- Grafico de la Secuencia LCG (ASCII) ---");
        System.out.println("Mostrando dispersion de U(n) vs n (submuestra de 500 puntos)");
        System.out.println();
        
        double[] sequence = controller.getSequenceForPlotting(500);
        if (sequence.length == 0) {
            System.out.println("No hay datos para graficar. Ejecute la simulacion primero (opcion 1).");
            return;
        }
        
        // Configuracion del grafico
        int width = 70;
        int height = 20;
        
        // Crear canvas vacio
        char[][] canvas = new char[height][width];
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                canvas[y][x] = ' ';
            }
        }
        
        // Dibujar ejes (usar caracteres ASCII compatibles)
        // Eje Y (vertical) - izquierda
        for (int y = 0; y < height; y++) {
            canvas[y][0] = '|';
        }
        // Eje X (horizontal) - abajo
        for (int x = 0; x < width; x++) {
            canvas[height-1][x] = '-';
        }
        canvas[height-1][0] = '+';
        
        // Escalar y plotear puntos
        int nPoints = sequence.length;
        for (int i = 0; i < nPoints; i++) {
            double val = sequence[i];
            // Mapear indice a coordenada X (1 a width-1)
            int x = 1 + (int) ((i / (double) Math.max(1, nPoints - 1)) * (width - 2));
            // Mapear valor [0,1) a coordenada Y (height-2 a 0)
            int y = height - 2 - (int) (val * (height - 2));
            
            // Asegurar limites
            x = Math.max(1, Math.min(width - 1, x));
            y = Math.max(0, Math.min(height - 2, y));
            
            // Marcar punto (si hay colision, usar '*')
            if (canvas[y][x] == ' ') {
                canvas[y][x] = '*';
            } else if (canvas[y][x] == '*') {
                canvas[y][x] = '+';
            } else {
                canvas[y][x] = '#';
            }
        }
        
        // Etiquetas eje Y
        double[] yLabels = {1.0, 0.75, 0.5, 0.25, 0.0};
        for (double labelVal : yLabels) {
            int yPos = height - 2 - (int) (labelVal * (height - 2));
            if (yPos >= 0 && yPos < height - 1) {
                String label = String.format("%.2f", labelVal);
                // Escribir etiqueta a la izquierda del eje Y
                for (int j = 0; j < label.length(); j++) {
                    int col = 5 - label.length() + j;
                    if (col >= 0 && col < width) {
                        canvas[yPos][col] = label.charAt(j);
                    }
                }
            }
        }
        
        // Imprimir canvas
        for (int y = 0; y < height; y++) {
            StringBuilder line = new StringBuilder();
            for (int x = 0; x < width; x++) {
                line.append(canvas[y][x]);
            }
            // Recortar espacios al final
            System.out.println(line.toString().stripTrailing());
        }
        
        // Etiquetas eje X
        System.out.printf("%-6s%-" + (width-12) + "s%6d%n", "0", "n (indice)", nPoints);
        System.out.printf("%-6s%-" + (width-12) + "s%s%n", "U(n)", "", "[0, 1)");
        System.out.println();
        System.out.println("Puntos graficados: " + nPoints + " (submuestra de " + controller.getFullSequence().length + " totales)");
        System.out.println("Leyenda: * = punto, + = superposicion, # = multiples puntos");
    }

    /**
     * Bucle principal de la aplicación.
     */
    public void run() {
        while (true) {
            displayMenu();
            System.out.print("Seleccione una opción: ");
            String choice = scanner.nextLine().trim();

            switch (choice) {
                case "1":
                    runSimulation();
                    break;
                case "2":
                    try {
                        System.out.print("Cantidad de observaciones [20]: ");
                        String nInput = scanner.nextLine().trim();
                        int n = nInput.isEmpty() ? 20 : Integer.parseInt(nInput);
                        displayFirstN(n);
                    } catch (NumberFormatException e) {
                        System.out.println("Error: Ingrese un número válido.");
                    }
                    break;
                case "3":
                    changeSeed();
                    break;
                case "4":
                    compareWithReference();
                    break;
                case "5":
                    exportJson();
                    break;
                case "6":
                    showSummary();
                    break;
                case "7":
                    plotSequence();
                    break;
                case "0":
                    System.out.println("\n¡Hasta luego!");
                    return;
                default:
                    System.out.println("Opción inválida. Intente de nuevo.");
            }
        }
    }
}