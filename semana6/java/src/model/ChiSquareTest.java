package model;

import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class ChiSquareTest {
    private final int intervals;
    private final double alpha;

    public ChiSquareTest(int intervals, double alpha) {
        this.intervals = intervals;
        this.alpha = alpha;
    }

    public ChiSquareTest() {
        this(10, 0.05);
    }

    public Map<String, Object> test(List<Double> numbers) {
        int n = numbers.size();
        double expectedFreq = (double) n / intervals;
        
        int[] observed = new int[intervals];
        for (double num : numbers) {
            int idx = Math.min((int) (num * intervals), intervals - 1);
            observed[idx]++;
        }
        
        double chi2Stat = 0.0;
        for (int o : observed) {
            double diff = o - expectedFreq;
            chi2Stat += (diff * diff) / expectedFreq;
        }
        
        int dof = intervals - 1;
        double pValue = 1 - chiSquareCDF(chi2Stat, dof);
        double criticalValue = chiSquareInverseCDF(1 - alpha, dof);
        boolean rejectH0 = pValue < alpha;
        
        Map<String, Object> results = new HashMap<>();
        results.put("observed_frequencies", observed);
        results.put("expected_frequency", expectedFreq);
        results.put("chi2_statistic", chi2Stat);
        results.put("degrees_of_freedom", dof);
        results.put("p_value", pValue);
        results.put("critical_value", criticalValue);
        results.put("alpha", alpha);
        results.put("reject_h0", rejectH0);
        results.put("conclusion", rejectH0 
            ? "Se rechaza H0: Los numeros no siguen distribucion uniforme"
            : "No se rechaza H0: Los numeros siguen distribucion uniforme");
        
        return results;
    }

    private double chiSquareCDF(double x, int k) {
        if (x <= 0) return 0.0;
        if (k <= 0) return 1.0;
        
        double a = k / 2.0;
        return regularizedGammaP(a, x / 2.0);
    }

    private double regularizedGammaP(double a, double x) {
        if (x < 0) return 0.0;
        if (x == 0) return 0.0;
        
        double gamma_a = gamma(a);
        if (x < a + 1) {
            return lowerGammaSeries(a, x) / gamma_a;
        } else {
            return 1.0 - upperGammaContinuedFraction(a, x) / gamma_a;
        }
    }

    private double lowerGammaSeries(double a, double x) {
        double sum = 1.0 / a;
        double term = 1.0 / a;
        
        for (int n = 1; n < 200; n++) {
            term *= x / (a + n);
            sum += term;
            if (Math.abs(term) < 1e-15) break;
        }
        
        return Math.exp(-x + a * Math.log(x)) * sum;
    }

    private double upperGammaContinuedFraction(double a, double x) {
        double b = x + 1.0 - a;
        double c = 1.0 / 1e-30;
        double d = 1.0 / b;
        double h = d;
        
        for (int i = 1; i < 200; i++) {
            int i2 = 2 * i;
            double aa = i * (a - i);
            b += 2.0;
            d = 1.0 / (aa * d + b);
            c = b + aa / c;
            double del = c * d;
            h *= del;
            if (Math.abs(del - 1.0) < 1e-14) break;
        }
        
        return Math.exp(-x + a * Math.log(x)) * h;
    }

    private double chiSquareInverseCDF(double p, int k) {
        double low = 0.0;
        double high = k + 10 * Math.sqrt(2 * k);
        
        for (int i = 0; i < 60; i++) {
            double mid = (low + high) / 2;
            if (chiSquareCDF(mid, k) < p) {
                low = mid;
            } else {
                high = mid;
            }
            if (high - low < 1e-8) break;
        }
        return (low + high) / 2;
    }

    private double gamma(double x) {
        if (x <= 0) return Double.NaN;
        
        double[] coef = {
            76.18009172947146, -86.50532032941677,
            24.01409824083091, -1.231739572450155,
            0.1208650973866179e-2, -0.5395239384953e-5
        };
        
        double y = x;
        double tmp = x + 5.5;
        tmp -= (x + 0.5) * Math.log(tmp);
        double ser = 1.000000000190015;
        
        for (int i = 0; i < 6; i++) {
            ser += coef[i] / ++y;
        }
        
        return Math.exp(-tmp + Math.log(2.5066282746310005 * ser / x));
    }
}