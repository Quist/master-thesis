# Apache Camel
>Apache Camel is a lightweight integration framework which implements all EIPs. Thus, you can easily integrate different applications using the required patterns. You can use Java, Spring XML, Scala or Groovy. Almost every technology you can imagine is available, for example HTTP, FTP, JMS, EJB, JPA, RMI, JMS, JMX, LDAP, Netty, and many, many more (of course most ESBs also offer support for them)

* Rammeverk for å integrere forskjellige applikasjoner. Støtter integrasjon mot Twitter, email, HTTP, FTP og mye annet. Over 200 støttende teknologier.
* JVM-based Routing Engine


#### Fordeler
* Støtter forskjellige protokoller som kan være aktuelle:
    * HTTP
    * A
* I store integrasjonsprosjekter er det kostnad og ressurskrevende og skrive integrasjoner. Apace Camel gjør integrasjonen for deg.
* Gode debuggingsmuligheter for innkommende og utkommende meldinger: hawt.io.

#### Ulemper
* Overhead? Lagd for å understøtte integrasjon i store enterprise systemer. Ikke helt vårt usecase, skal lage en proxy.
* En bloggpost om [use cases for Camel](https://dzone.com/articles/when-use-apache-camel) anbefaler det ikke hvis man bare skal støtte en fåtall av teknologier. Da kan det være bedre å bruke bibloteker for de spesefikke teknologiene direkte.
*


#### Uavklart
* Hvilke muligheter har jeg til å redigere headere, komprimering osv.

#### Konklusjon
Veldig bra valg i store systemer der du må gjøre mange integrasjoner, men jeg ser ikke helt nytten i mitt prosjekt der hovedfokuset er å lage en effektiv proxy.

Eventuelt, hvis jeg skal støtte en rekke forskjellige protokoller kan Apache Camel gjøre det lettere å implementere, men kanskje ikke raskere?
