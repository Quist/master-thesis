public abstract class DilRouteBuilder {

    private final ArrayList<Processor> preProcessors = new ArrayList<>();
    private final ArrayList<Processor> postProcessors = new ArrayList<>();

    public abstract String getToUri();
    public abstract String getFromUri();

    public void addPreprocessor(Processor processor) {
        preProcessors.add(processor);
    }

    public ArrayList<Processor> getPreProcessors() {
        return preProcessors;
    }

    public void addPostProcessor(Processor processor) {
        postProcessors.add(processor);
    }

    public ArrayList<Processor> getPostProcessors() {
        return postProcessors;
    }
}
