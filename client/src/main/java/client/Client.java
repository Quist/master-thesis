package client;

import helloworld.HelloWorld;
import helloworld.HelloWorldService;

import java.net.ProxySelector;

public class Client {

    public static void main(String args[]) {
        MyProxySelector ps = new MyProxySelector(ProxySelector.getDefault());
        ProxySelector.setDefault(ps);

        HelloWorld helloWorld = new HelloWorldService().getHelloWorldPort();
        String response = helloWorld.sayHelloWorldFrom("Joakimx");

        System.out.println(response);
    }
}
