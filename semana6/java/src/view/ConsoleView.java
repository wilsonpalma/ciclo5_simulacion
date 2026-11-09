package view;

import model.ChiSquareTest;
import model.KolmogorovSmirnovTest;
import java.util.List;
import java.util.Map;

public class ConsoleView {
    public void showWelcome() {
        System.out.println("=".repeat(60));
        System.out.println("  VALIDACION ESTADISTICA DE NUMEROS PSEUDOALEATORIOS");
        System.out.println("  Pruebas Chi-Cuadrado y Kolmogorov-Smirnov");
        System.out.println("=".repeat(60));
        System.out.println();
    }

    public void showLCGParams(long seed, long multiplier, long increment, long modulus, int count) {
        System.out.println("Parametros del Generador Congruencial Lineal (LCG):");
        System.out.printf("  Semilla (X0):     %d%n", seed);
        System.out.printf("  Multiplicador (a): %d%n", multiplier);
        System.out.printf("  Incremento (c):    %d%n", increment);
        System.out.printf("  Modulo (m):        %d%n", modulus);
        System.out.printf("  Cantidad (n):      %d%n%n", count);
    }

    public void showChiSquareResults(Map<String, Object> results) {
        System.out.println("-".repeat(50));
        System.out.println("RESULTADOS PRUEBA CHI-CUADRADO");
        System.out.println("-".repeat(50));
        
        int[] observed = (int[]) results.get("observed_frequencies");
        double expected = (double) results.get("expected_frequency");
        double chi2Stat = (double) results.get("chi2_statistic");
        int dof = (int) results.get("degrees_of_freedom");
        double pValue = (double) results.get("p_value");
        double criticalValue = (double) results.get("critical_value");
        double alpha = (double) results.get("alpha");
        String conclusion = (String) results.get("conclusion");
        
        System.out.printf("Intervalos (k):           %d%n", observed.length);
        System.out.printf("Frecuencia esperada (Ei): %.2f%n%n", expected);
        
        System.out.println("Frecuencias observadas por intervalo:");
        for (int i = 0; i < observed.length; i++) {
            System.out.printf("  Intervalo [%.1f, %.1f): %d%n", i*0.1, (i+1)*0.1, observed[i]);
        }
        System.out.println();
        
        System.out.printf("Estadistico Chi-Cuadrado: %.6f%n", chi2Stat);
        System.out.printf("Grados de libertad:       %d%n", dof);
        System.out.printf("Valor critico (alpha=%.2f): %.6f%n", alpha, criticalValue);
        System.out.printf("Valor p:                  %.6f%n%n", pValue);
        
        System.out.printf("Decision: %s%n%n", conclusion);
    }

    public void showKSResults(Map<String, Object> results) {
        System.out.println("-".repeat(50));
        System.out.println("RESULTADOS PRUEBA KOLMOGOROV-SMIRNOV");
        System.out.println("-".repeat(50));
        
        int n = (int) results.get("n");
        double dPlusMax = (double) results.get("d_plus_max");
        double dMinusMax = (double) results.get("d_minus_max");
        double ksStat = (double) results.get("ks_statistic");
        double pValue = (double) results.get("p_value");
        double alpha = (double) results.get("alpha");
        String conclusion = (String) results.get("conclusion");
        
        System.out.printf("Tamaño de muestra (n):    %d%n", n);
        System.out.printf("D+ maximo:                %.6f%n", dPlusMax);
        System.out.printf("D- maximo:                %.6f%n", dMinusMax);
        System.out.printf("Estadistico KS (D):       %.6f%n", ksStat);
        System.out.printf("Valor p:                  %.6f%n", pValue);
        System.out.printf("Alpha:                    %.2f%n%n", alpha);
        
        System.out.printf("Decision: %s%n%n", conclusion);
    }

    public void showComparisonTable(List<Map<String, Object>> data) {
        System.out.println("=".repeat(80));
        System.out.println("COMPARACION DE RESULTADOS PYTHON VS JAVA");
        System.out.println("=".repeat(80));
        System.out.printf("%-10s | %-10s | %-18s | %-16s%n", "N", "Error", "Tiempo Python (s)", "Tiempo Java (s)");
        System.out.println("-".repeat(80));
        
        for (Map<String, Object> row : data) {
            System.out.printf("%-10d | %-10.6f | %-18.6f | %-16.6f%n",
                (int) row.get("n"),
                (double) row.get("error"),
                (double) row.get("python_time"),
                (double) row.get("java_time"));
        }
        System.out.println();
    }

    public void showControlQuestions() {
        System.out.println("=".repeat(60));
        System.out.println("PREGUNTAS DE CONTROL");
        System.out.println("=".repeat(60));
        
        String[][] qa = {
            {"1. ¿Qué es la hipótesis nula?", 
             "Es la afirmación que se pone a prueba, en este caso H0: los números siguen una distribución uniforme U(0,1)."},
            {"2. ¿Qué representa el valor p?", 
             "Es la probabilidad de obtener resultados al menos tan extremos como los observados, asumiendo que H0 es verdadera. Un p-valor pequeño (< 0.05) sugiere evidencia contra H0."},
            {"3. ¿Qué significa rechazar H0?", 
             "Significa que hay evidencia estadística suficiente para concluir que los números NO siguen una distribución uniforme."},
            {"4. ¿Qué diferencia existe entre Chi-Cuadrado y KS?", 
             "Chi-Cuadrado agrupa datos en intervalos y compara frecuencias; KS compara la función de distribución acumulada empírica con la teórica sin agrupar. KS es más sensible a diferencias en las colas."},
            {"5. ¿Por qué una prueba estadística no demuestra que un generador sea verdaderamente aleatorio?", 
             "Las pruebas solo detectan desviaciones de patrones específicos. Un generador puede pasar ciertas pruebas pero fallar en otras. La aleatoriedad verdadera no puede probarse, solo puede fallarse en detectar no-aleatoriedad."}
        };
        
        for (String[] pair : qa) {
            System.out.printf("%n%s%n   %s%n", pair[0], pair[1]);
        }
        System.out.println();
    }

    public void showError(String message) {
        System.err.println("ERROR: " + message);
        System.out.println();
    }
}