DescriptiveStatistics stats = new DescriptiveStatistics();

for (int i=0; i<antall; ++i) {
    long ts1 = System.currentTimeMillis();
    NFFIDataResponse response = pullDataOperation(null);
    long ts2 = System.currentTimeMillis();
    stats.addValue(ts2-ts1);
}

System.out.println("Mean: " + stats.getMean());
System.out.println("Standard Deviation: " + stats.getStandardDeviation());
System.out.println("Variance: " + stats.getVariance());
System.out.println("Min: " + stats.getMin());
System.out.println("Max: " + stats.getMax());
System.out.println("Median: " + stats.getPercentile(50));
