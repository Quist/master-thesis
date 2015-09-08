package main.java.proxy;

import org.apache.camel.Exchange;
import org.apache.camel.Processor;

public class HttpProcessor implements Processor {
    @Override
    public void process(Exchange exchange) throws Exception {
        System.out.println("Nå fikk jeg en melding.");
    }
}
