package client;

import java.io.IOException;
import java.net.*;
import java.util.ArrayList;
import java.util.List;

public class MyProxySelector extends ProxySelector {
    private final String hostname = "localhost";
    private final int port = 7500;

    private ProxySelector defsel = null;

    MyProxySelector(ProxySelector def) {
        defsel = def;
    }

    @Override
    public List<Proxy> select(URI uri) {
        if (uri == null) {
            throw new IllegalArgumentException("URI can't be null.");
        }

        String protocol = uri.getScheme();
        if ("http".equalsIgnoreCase(protocol) ||
                "https".equalsIgnoreCase(protocol)) {

            ArrayList<Proxy> l = new ArrayList<Proxy>();
            Proxy proxy = new Proxy(Proxy.Type.HTTP, (new InetSocketAddress(hostname, port)));
            l.add(proxy);
            return l;
        }

        if (defsel != null) {
            return defsel.select(uri);
        } else {
            ArrayList<Proxy> l = new ArrayList<Proxy>();
            l.add(Proxy.NO_PROXY);
            return l;
        }
    }

    @Override
    public void connectFailed(URI uri, SocketAddress socketAddress, IOException e) {
        System.out.println("Connection failed");
    }
}
