package main.java.proxy;

import org.apache.camel.Exchange;

public class IncomingProxyMessageProcessor implements org.apache.camel.Processor {

    @Override
    public void process(Exchange exchange) throws Exception {
        System.out.println("Received incoming proxy message");
    }
}
