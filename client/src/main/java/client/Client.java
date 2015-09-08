package client;

import helloworld.HelloWorld;
import helloworld.HelloWorldService;
import helloworld.ObjectFactory;

public class Client {

    public static void main(String args[]) {
        HelloWorld helloWorld = new HelloWorldService().getHelloWorldPort();
        String response = helloWorld.sayHelloWorldFrom("Joakimx");

        System.out.println(response);
    }
}
