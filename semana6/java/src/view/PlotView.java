package view;

import model.ChiSquareTest;
import model.KolmogorovSmirnovTest;
import java.util.List;
import java.util.Map;

public class PlotView {
    public void plotChiSquareText(Map<String, Object> results) {
        int[] observed = (int[]) results.get("observed_frequencies");
        double expected = (double) results.get("expected_frequency");
        double chi2Stat = (double) results.get("chi2_statistic");
        double pValue = (double) results.get("p_value");
        
        System.out.println("GRAFICO CHI-CUADRADO (representacion textual)");
        System.out.println("Observado (O) vs Esperado (E)");
        System.out.println("Chi2 = " + String.format("%.4f", chi2Stat) + ", p = " + String.format("%.6f", pValue));
        System.out.println();
        
        int maxObs = 0;
        for (int o : observed) maxObs = Math.max(maxObs, o);
        int maxVal = Math.max(maxObs, (int)Math.ceil(expected));
        int scale = Math.max(1, maxVal / 40);
        
        for (int i = 0; i < observed.length; i++) {
            int o = observed[i];
            int oBars = Math.max(1, o / scale);
            int eBars = Math.max(1, (int)Math.round(expected) / scale);
            
            System.out.printf("[%d] O:%s (%d)  E:%s (%.1f)%n",
                i,
                "*".repeat(oBars), o,
                "=".repeat(eBars), expected);
        }
        System.out.println();
    }

    public void plotKSText(Map<String, Object> results) {
        List<Double> sorted = (List<Double>) results.get("sorted_numbers");
        List<Double> ecdf = (List<Double>) results.get("ecdf_values");
        List<Double> theoretical = (List<Double>) results.get("theoretical_cdf");
        double dStat = (double) results.get("ks_statistic");
        double pValue = (double) results.get("p_value");
        
        System.out.println("GRAFICO KOLMOGOROV-SMIRNOV (representacion textual)");
        System.out.println("D = " + String.format("%.4f", dStat) + ", p = " + String.format("%.6f", pValue));
        System.out.println();
        
        int n = sorted.size();
        int step = Math.max(1, n / 20);
        
        System.out.println("x        | ECDF     | Teorica  | Diff");
        System.out.println("---------|----------|----------|-------");
        for (int i = 0; i < n; i += step) {
            double x = sorted.get(i);
            double fn = ecdf.get(i);
            double fo = theoretical.get(i);
            double diff = Math.abs(fn - fo);
            System.out.printf("%.4f | %.6f | %.6f | %.6f%n", x, fn, fo, diff);
        }
        System.out.println();
    }

    public void plotHistogramText(List<Double> numbers, int bins) {
        int[] counts = new int[bins];
        for (double num : numbers) {
            int idx = Math.min((int) (num * bins), bins - 1);
            counts[idx]++;
        }
        
        int maxCount = 0;
        for (int c : counts) maxCount = Math.max(maxCount, c);
        int scale = Math.max(1, maxCount / 40);
        
        System.out.println("HISTOGRAMA (representacion textual)");
        System.out.println("Uniforme teorica: densidad = 1.0");
        System.out.println();
        
        for (int i = 0; i < bins; i++) {
            double rangeStart = (double) i / bins;
            double rangeEnd = (double) (i + 1) / bins;
            int bars = Math.max(1, counts[i] / scale);
            System.out.printf("[%.2f, %.2f): %s (%d)%n", 
                rangeStart, rangeEnd, "*".repeat(bars), counts[i]);
        }
        System.out.println();
    }
}