package main.java.proxy;

import org.apache.camel.CamelContext;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.impl.DefaultCamelContext;


public class Proxy {
    public static void main(String args[]) {

        final int listenPort = Integer.parseInt(args[0]);
        final int forwardPort = Integer.parseInt(args[1]);

        final String incomingServiceMessagePath = "jetty:http://localhost:" + listenPort+ "/helloworld?wsdl";
        final String proxyPath = "http://localhost:" + forwardPort + "/proxy/incoming?bridgeEndpoint=true";
        final String incomingProxyMessagePath = "jetty:http://localhost:" + listenPort + "/proxy/incoming";
        final String outgoingServicePath = "jetty:http://localhost:" + listenPort + "/proxy/incoming";

        CamelContext context = new DefaultCamelContext();

        try {
            context.addRoutes(new RouteBuilder() {
                public void configure() {
                    from(incomingServiceMessagePath).process(new IncomingServiceMessageProcessor())
                            .to(proxyPath);
                }
            });
            context.addRoutes(new RouteBuilder() {
                public void configure() {
                    from(incomingProxyMessagePath).process(new IncomingProxyMessageProcessor())
                            .to(outgoingServicePath);
                }
            });

        } catch (Exception e) {
            e.printStackTrace();
        }

        try {
            context.start();
            System.out.println("Proxy listening on port " + listenPort);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
