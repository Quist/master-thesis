Møte med veiledere 3. september 2015
====================
FFI

#### Tilstede:

Trude & Frank

Joakim


#### Gjort siden sist.
Begynt å lære/sette opp WebServices og se på applikasjonservere. Bygd litt på strukturen til masteroppgaven og lest igjennom oppgaven til Eggum, spesielt mtp. proxier.

#### Hva vi snakket om
Først sette opp Web Service og klient og proxier uten å tenke på sikkerhet. Kristoffer Karud skriver om optimalisering av applikasjonservere, spesefikt Glassfish. Det burde jeg se på mtp. å bruke optimaliseringstipsene.
##### Valg av applikasjonserver
Glassfish vs. Tomcat. Glassfish flere muligheter for utvilkere av Web Services. Tomcat mer lettvekt og enklere  bruke. Karud så på optimalisering av Glassfish. Det endelige valget burde diskuteres i masteroppgaven.

##### Prioritering av evaluering av proxy
Hvis tid i prosjektet: Legg på realistisk overhead mtp. sikkerhet.

1. Netem u/sikkerhet
2. Netem m/sikkerhet
3. SOAP sikkerhet.
4. Radio - Kan være vanskelig å få tilgang til labben på ffi.

##### Annet
* Apache CFX - Det store Web Service stacken innenfor Java.
* Diff-serv. Singaliserer trafikk-klasser på internett-laget. Kan være viktig for optimalisering. Burde hvertfall diskuteres i related work.
* Web Servicen jeg bruker burde bruke ulike størelser på data, for å simulere realistiske data. Kan kanskje få FFI-testdata/FFI-WebServices.
* IPSEC - Veldig interessant å undersøke. Separat testsett.
* Timeout-verdier på TCP, HTTP-layer kan være nødvendig å tunes.
* IP-fragmentering kan være et problem, spesielt når man tester over radiolinker.

#### Til neste gang
Prøve å få på plass ambisjoner på oppgaven i masteroppgaven.
Skrive om valg av applikasjonserver.
Skrive om DIL - paperet til Michael er veldig bra.
CAMEL Application Part - En hos FFI som har veldig god peiling.
