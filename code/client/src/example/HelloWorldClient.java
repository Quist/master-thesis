package example;

import client.HelloWorldService;
import java.rmi.RemoteException;

public class HelloWorldClient {
  public static void main(String[] argv) {
    client.HelloWorld service = new HelloWorldService().getHelloWorldPort();
    //invoke business method
    String result = service.sayHelloWorldFrom("Joakim!");
    System.out.println(result);
  }
}
