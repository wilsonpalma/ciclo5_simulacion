package controller;

import model.LCG;
import model.ChiSquareTest;
import model.KolmogorovSmirnovTest;
import view.ConsoleView;
import view.PlotView;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SimulationController {
    private final LCG lcg;
    private final ChiSquareTest chiSquare;
    private final KolmogorovSmirnovTest ksTest;
    private final ConsoleView console;
    private final PlotView plotter;

    public SimulationController(long seed, long multiplier, long increment, long modulus) {
        this.lcg = new LCG(seed, multiplier, increment, modulus);
        this.chiSquare = new ChiSquareTest(10, 0.05);
        this.ksTest = new KolmogorovSmirnovTest(0.05);
        this.console = new ConsoleView();
        this.plotter = new PlotView();
    }

    public SimulationController() {
        this(12345, 1664525, 1013904223L, (1L << 32));
    }

    public Map<String, Object> runSimulation(int count) {
        console.showWelcome();
        console.showLCGParams(
            lcg.getSeed(), lcg.getMultiplier(),
            lcg.getIncrement(), lcg.getModulus(), count
        );
        
        List<Double> numbers = lcg.generate(count);
        
        Map<String, Object> chi2Results = chiSquare.test(numbers);
        console.showChiSquareResults(chi2Results);
        plotter.plotChiSquareText(chi2Results);
        
        Map<String, Object> ksResults = ksTest.test(numbers);
        console.showKSResults(ksResults);
        plotter.plotKSText(ksResults);
        
        plotter.plotHistogramText(numbers, 20);
        
        console.showControlQuestions();
        
        Map<String, Object> results = new HashMap<>();
        results.put("numbers", numbers);
        results.put("chi_square", chi2Results);
        results.put("kolmogorov_smirnov", ksResults);
        
        return results;
    }

    public List<Map<String, Object>> runComparison(List<Integer> sampleSizes) {
        if (sampleSizes == null) {
            sampleSizes = List.of(1000, 10000, 100000, 1000000);
        }
        
        List<Map<String, Object>> comparisonData = new ArrayList<>();
        
        for (int n : sampleSizes) {
            lcg.reset();
            double pyTime = lcg.generateAndTime(n);
            List<Double> numbers = lcg.generate(n);
            
            Map<String, Object> chi2Results = chiSquare.test(numbers);
            Map<String, Object> ksResults = ksTest.test(numbers);
            
            double error = Math.abs((double) chi2Results.get("p_value") - 0.5);
            
            Map<String, Object> row = new HashMap<>();
            row.put("n", n);
            row.put("error", error);
            row.put("python_time", 0.0);
            row.put("java_time", pyTime);
            
            comparisonData.add(row);
        }
        
        console.showComparisonTable(comparisonData);
        return comparisonData;
    }
}