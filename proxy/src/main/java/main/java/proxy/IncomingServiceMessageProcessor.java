package main.java.proxy;

import org.apache.camel.Exchange;

public class IncomingServiceMessageProcessor implements org.apache.camel.Processor {

    @Override
    public void process(Exchange exchange) throws Exception {
        System.out.println("Received incoming message from Web Service");
    }
}
