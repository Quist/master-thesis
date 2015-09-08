package main.java.proxy;

import org.apache.camel.CamelContext;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.impl.DefaultCamelContext;

public class Proxy {
    public static void main(String args[]) throws Exception {
        CamelContext context = new DefaultCamelContext();
        context.addRoutes(new RouteBuilder() {
            public void configure() {
                from("jetty:http://localhost:7592/myapp/myservice").process(new HttpProcessor());
            }
        });

        context.start();

        System.out.println("Hei :)");
    }
}
