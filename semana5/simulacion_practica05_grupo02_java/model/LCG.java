package model;

/**
 * Modelo del Generador Congruencial Lineal (LCG).
 * Implementa la relación recursiva: X(n+1) = (a * X(n) + c) mod m
 * Valores normalizados: U(n) = X(n) / m
 */
public class LCG {
    private final long a;
    private final long c;
    private final long m;
    private long seed;
    private long state;

    /**
     * Constructor con parámetros estándar.
     * a = 1664525, c = 1013904223, m = 2^32, seed = 12345
     */
    public LCG() {
        this(1664525L, 1013904223L, 1L << 32, 12345L);
    }

    /**
     * Constructor con parámetros personalizados.
     */
    public LCG(long a, long c, long m, long seed) {
        this.a = a;
        this.c = c;
        this.m = m;
        this.seed = seed;
        this.state = seed;
    }

    /**
     * Genera el siguiente valor entero.
     */
    public long next() {
        state = (a * state + c) % m;
        return state;
    }

    /**
     * Genera el siguiente valor normalizado [0, 1).
     */
    public double nextNormalized() {
        return (double) next() / (double) m;
    }

    /**
     * Genera una secuencia de n valores enteros.
     */
    public long[] generateSequence(int n) {
        long[] sequence = new long[n];
        for (int i = 0; i < n; i++) {
            sequence[i] = next();
        }
        return sequence;
    }

    /**
     * Genera una secuencia de n valores normalizados.
     */
    public double[] generateNormalizedSequence(int n) {
        double[] sequence = new double[n];
        for (int i = 0; i < n; i++) {
            sequence[i] = nextNormalized();
        }
        return sequence;
    }

    /**
     * Reinicia el generador con una nueva semilla.
     */
    public void reset(long seed) {
        this.seed = seed;
        this.state = seed;
    }

    /**
     * Reinicia el generador con la semilla original.
     */
    public void reset() {
        this.state = this.seed;
    }

    /**
     * Obtiene los parámetros del generador.
     */
    public String getParameters() {
        return String.format("a=%d, c=%d, m=%d, seed=%d", a, c, m, seed);
    }

    /**
     * Analiza el período del generador detectando el primer valor repetido.
     * @param maxIterations máximo de iteraciones a revisar
     * @return período encontrado o -1 si no se detecta
     */
    public int analyzePeriod(int maxIterations) {
        java.util.Map<Long, Integer> seen = new java.util.HashMap<>();
        reset();
        for (int i = 0; i < maxIterations; i++) {
            long val = next();
            if (seen.containsKey(val)) {
                return i - seen.get(val);
            }
            seen.put(val, i);
        }
        return -1;
    }

    // Getters
    public long getA() { return a; }
    public long getC() { return c; }
    public long getM() { return m; }
    public long getSeed() { return seed; }
    public long getState() { return state; }
}