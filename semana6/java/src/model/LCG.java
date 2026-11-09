package model;

import java.util.ArrayList;
import java.util.List;

public class LCG {
    private long seed;
    private final long multiplier;
    private final long increment;
    private final long modulus;
    private long current;

    public LCG(long seed, long multiplier, long increment, long modulus) {
        this.seed = seed;
        this.multiplier = multiplier;
        this.increment = increment;
        this.modulus = modulus;
        this.current = seed;
    }

    public LCG() {
        this(12345, 1664525, 1013904223L, (1L << 32));
    }

    public List<Double> generate(int count) {
        long startTime = System.nanoTime();
        List<Double> numbers = new ArrayList<>(count);
        
        for (int i = 0; i < count; i++) {
            current = (multiplier * current + increment) % modulus;
            numbers.add((double) current / (double) modulus);
        }
        
        long endTime = System.nanoTime();
        double elapsedSeconds = (endTime - startTime) / 1_000_000_000.0;
        System.out.printf("Generados %d numeros en %.6f segundos%n%n", count, elapsedSeconds);
        
        return numbers;
    }

    public double generateAndTime(int count) {
        long startTime = System.nanoTime();
        List<Double> numbers = new ArrayList<>(count);
        
        for (int i = 0; i < count; i++) {
            current = (multiplier * current + increment) % modulus;
            numbers.add((double) current / (double) modulus);
        }
        
        long endTime = System.nanoTime();
        return (endTime - startTime) / 1_000_000_000.0;
    }

    public void reset(long seed) {
        this.seed = seed;
        this.current = seed;
    }

    public void reset() {
        this.current = this.seed;
    }

    public long getSeed() { return seed; }
    public long getMultiplier() { return multiplier; }
    public long getIncrement() { return increment; }
    public long getModulus() { return modulus; }
}