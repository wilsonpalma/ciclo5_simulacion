package model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class KolmogorovSmirnovTest {
    private final double alpha;

    public KolmogorovSmirnovTest(double alpha) {
        this.alpha = alpha;
    }

    public KolmogorovSmirnovTest() {
        this(0.05);
    }

    public Map<String, Object> test(List<Double> numbers) {
        int n = numbers.size();
        List<Double> sorted = new ArrayList<>(numbers);
        Collections.sort(sorted);
        
        double dPlusMax = 0.0;
        double dMinusMax = 0.0;
        
        List<Double> dPlusList = new ArrayList<>(n);
        List<Double> dMinusList = new ArrayList<>(n);
        List<Double> fnList = new ArrayList<>(n);
        List<Double> foList = new ArrayList<>(n);
        
        for (int i = 0; i < n; i++) {
            double x = sorted.get(i);
            double fn = (double) (i + 1) / n;
            double fo = x;
            
            double dPlus = fn - fo;
            double dMinus = fo - (double) i / n;
            
            dPlusMax = Math.max(dPlusMax, dPlus);
            dMinusMax = Math.max(dMinusMax, dMinus);
            
            dPlusList.add(dPlus);
            dMinusList.add(dMinus);
            fnList.add(fn);
            foList.add(fo);
        }
        
        double dStat = Math.max(dPlusMax, dMinusMax);
        double pValue = approximatePValue(dStat, n);
        boolean rejectH0 = pValue < alpha;
        
        Map<String, Object> results = new HashMap<>();
        results.put("n", n);
        results.put("d_plus_max", dPlusMax);
        results.put("d_minus_max", dMinusMax);
        results.put("ks_statistic", dStat);
        results.put("p_value", pValue);
        results.put("alpha", alpha);
        results.put("reject_h0", rejectH0);
        results.put("conclusion", rejectH0
            ? "Se rechaza H0: Los numeros no siguen distribucion uniforme"
            : "No se rechaza H0: Los numeros siguen distribucion uniforme");
        results.put("ecdf_values", fnList);
        results.put("theoretical_cdf", foList);
        results.put("sorted_numbers", sorted);
        
        return results;
    }

    private double approximatePValue(double d, int n) {
        double lambda = d * Math.sqrt(n);
        if (lambda <= 0) return 1.0;
        
        double sum = 0.0;
        for (int k = 1; k < 100; k++) {
            double term = 2 * Math.pow(-1, k - 1) * Math.exp(-2 * k * k * lambda * lambda);
            sum += term;
            if (Math.abs(term) < 1e-10) break;
        }
        return Math.max(0.0, Math.min(1.0, sum));
    }
}