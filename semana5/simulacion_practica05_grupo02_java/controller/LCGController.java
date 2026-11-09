package controller;

import model.LCG;
import java.util.ArrayList;
import java.util.List;

/**
 * Controlador para la simulación LCG.
 * Coordina la generación y análisis de secuencias.
 */
public class LCGController {
    private LCG lcg;
    private SimulationResults results;

    public LCGController() {
        this.lcg = new LCG();
        this.results = null;
    }

    /**
     * Retorna la secuencia completa generada.
     */
    public double[] getFullSequence() {
        if (results != null && results.fullSequence != null) {
            return results.fullSequence;
        }
        return new double[0];
    }

    /**
     * Retorna una submuestra de la secuencia para graficar.
     * Si la secuencia es muy grande, toma puntos espaciados uniformemente.
     */
    public double[] getSequenceForPlotting(int maxPoints) {
        double[] seq = getFullSequence();
        if (seq.length == 0) {
            lcg.reset(12345);
            seq = lcg.generateNormalizedSequence(10000);
        }
        
        if (seq.length <= maxPoints) {
            return seq;
        }
        
        // Submuestreo uniforme
        double[] sampled = new double[maxPoints];
        int step = Math.max(1, seq.length / maxPoints);
        int idx = 0;
        for (int i = 0; i < seq.length && idx < maxPoints; i += step) {
            sampled[idx++] = seq[i];
        }
        return sampled;
    }

    /**
     * Ejecuta la simulación completa:
     * 1. Genera 10,000 valores con seed=12345
     * 2. Guarda primeras 20 observaciones
     * 3. Analiza período
     * 4. Cambia semilla a 99999 y genera nueva secuencia
     * 5. Guarda primeras 20 observaciones con nueva semilla
     */
    public SimulationResults runFullSimulation(int n) {
        // Secuencia original (seed=12345)
        lcg.reset(12345);
        double[] sequence = lcg.generateNormalizedSequence(n);
        
        double[] first20Original = new double[Math.min(20, n)];
        System.arraycopy(sequence, 0, first20Original, 0, first20Original.length);

        // Analizar período
        lcg.reset(12345);
        int period = lcg.analyzePeriod(50000);

        // Nueva semilla (seed=99999)
        lcg.reset(99999);
        double[] sequenceNewSeed = lcg.generateNormalizedSequence(n);
        
        double[] first20NewSeed = new double[Math.min(20, n)];
        System.arraycopy(sequenceNewSeed, 0, first20NewSeed, 0, first20NewSeed.length);

        // Guardar resultados
        results = new SimulationResults(
            lcg.getA(), lcg.getC(), lcg.getM(), 12345L,
            n, first20Original, first20NewSeed, period,
            sequence, sequenceNewSeed
        );

        return results;
    }

    /**
     * Obtiene las primeras n observaciones de la secuencia actual.
     */
    public double[] getFirstNObservations(int n) {
        if (results != null && results.first20Original != null) {
            int len = Math.min(n, results.first20Original.length);
            double[] arr = new double[len];
            System.arraycopy(results.first20Original, 0, arr, 0, len);
            return arr;
        }
        lcg.reset(12345);
        return lcg.generateNormalizedSequence(n);
    }

    /**
     * Compara la secuencia Python/Java con una secuencia de referencia.
     * @param referenceSequence secuencia de referencia (ej. de Java)
     * @param n número de observaciones a comparar
     * @return lista de ComparisonResult
     */
    public List<ComparisonResult> compareWithReference(double[] referenceSequence, int n) {
        double[] current = getFirstNObservations(n);
        List<ComparisonResult> comparisons = new ArrayList<>();
        
        int limit = Math.min(n, Math.min(current.length, referenceSequence.length));
        for (int i = 0; i < limit; i++) {
            boolean equal = Math.abs(current[i] - referenceSequence[i]) < 1e-10;
            comparisons.add(new ComparisonResult(i, current[i], referenceSequence[i], equal));
        }
        return comparisons;
    }

    /**
     * Cambia la semilla y genera nueva secuencia.
     */
    public SimulationResults changeSeedAndGenerate(long newSeed, int n) {
        lcg.reset(newSeed);
        double[] sequence = lcg.generateNormalizedSequence(n);
        double[] first20 = new double[Math.min(20, n)];
        System.arraycopy(sequence, 0, first20, 0, first20.length);
        
        return new SimulationResults(
            lcg.getA(), lcg.getC(), lcg.getM(), newSeed,
            n, first20, null, -1, sequence, null
        );
    }

    /**
     * Genera un resumen textual de los resultados.
     */
    public String getResultsSummary() {
        if (results == null) {
            return "No hay resultados. Ejecute runFullSimulation() primero.";
        }
        return results.toString();
    }

    /**
     * Exporta resultados a JSON.
     */
    public void exportResultsJson(String filepath) throws java.io.IOException {
        if (results == null) {
            throw new IllegalStateException("No hay resultados para exportar");
        }
        
        String json = results.toJson();
        java.nio.file.Files.writeString(java.nio.file.Paths.get(filepath), json);
    }

    // Clases internas para resultados
    public static class SimulationResults {
        public final long a, c, m, seed;
        public final int nGenerated;
        public final double[] first20Original;
        public final double[] first20NewSeed;
        public final int period;
        public final double[] fullSequence;
        public final double[] fullSequenceNewSeed;

        public SimulationResults(long a, long c, long m, long seed, int nGenerated,
                                 double[] first20Original, double[] first20NewSeed,
                                 int period, double[] fullSequence, double[] fullSequenceNewSeed) {
            this.a = a; this.c = c; this.m = m; this.seed = seed;
            this.nGenerated = nGenerated;
            this.first20Original = first20Original;
            this.first20NewSeed = first20NewSeed;
            this.period = period;
            this.fullSequence = fullSequence;
            this.fullSequenceNewSeed = fullSequenceNewSeed;
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("=== RESUMEN DE RESULTADOS LCG ===\n");
            sb.append(String.format("Parámetros: a=%d, c=%d, m=%d, seed=%d\n", a, c, m, seed));
            sb.append(String.format("Valores generados: %d\n", nGenerated));
            sb.append(String.format("Período detectado: %d\n\n", period));
            
            sb.append("Primeras 20 observaciones (seed=12345):\n");
            if (first20Original != null) {
                for (int i = 0; i < first20Original.length; i++) {
                    sb.append(String.format("  U(%d) = %.10f\n", i + 1, first20Original[i]));
                }
            }
            
            sb.append("\nPrimeras 20 observaciones (seed=99999):\n");
            if (first20NewSeed != null) {
                for (int i = 0; i < first20NewSeed.length; i++) {
                    sb.append(String.format("  U(%d) = %.10f\n", i + 1, first20NewSeed[i]));
                }
            }
            return sb.toString();
        }

        public String toJson() {
            StringBuilder sb = new StringBuilder();
            sb.append("{\n");
            sb.append(String.format("  \"parameters\": {\"a\":%d,\"c\":%d,\"m\":%d,\"seed\":%d},\n", a, c, m, seed));
            sb.append(String.format("  \"n_generated\": %d,\n", nGenerated));
            sb.append("  \"first_20_original\": [");
            if (first20Original != null) {
                for (int i = 0; i < first20Original.length; i++) {
                    if (i > 0) sb.append(",");
                    sb.append(String.format("%.15f", first20Original[i]));
                }
            }
            sb.append("],\n");
            sb.append("  \"first_20_new_seed\": [");
            if (first20NewSeed != null) {
                for (int i = 0; i < first20NewSeed.length; i++) {
                    if (i > 0) sb.append(",");
                    sb.append(String.format("%.15f", first20NewSeed[i]));
                }
            }
            sb.append("],\n");
            sb.append(String.format("  \"period\": %d\n", period));
            sb.append("}");
            return sb.toString();
        }
    }

    public static class ComparisonResult {
        public final int index;
        public final double value1;
        public final double value2;
        public final boolean equal;

        public ComparisonResult(int index, double value1, double value2, boolean equal) {
            this.index = index;
            this.value1 = value1;
            this.value2 = value2;
            this.equal = equal;
        }
    }
}