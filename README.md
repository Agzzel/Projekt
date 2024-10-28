<h3> Crypto Tool </h3>

Används för att kryptera och dekryptera textsträngar med hjälp av en krypteringsnyckel.
Om det inte redan finns en färdiggenererad nyckel måste kommandot "generate" köras för att skapa en. Skriptet generate_key.py används för detta. Den krypterade strängen sparas i en fil.

<b>Exempelkörning</b>:

python3 crypto_tool.py generate secret.key # Genererar en krypteringsnyckel med namn secret.key<br>
python3 crypto_tool.py encrypt HelloWorld secret.key # Krypterar strängen HelloWorld med krypteringsnyckeln

<b>Kända begränsningar:</b>

Verktyget kan inte kryptera mer än en rad per körning.

<h3> Scanner </h3>

Skannar ett nätverk med nmap och visar vilka program som körs på vilka portar. Skriptet kan antingen
skanna en IP-adress som anges som argument, eller flera IP-adresser från en fil som argument.

<b>Exempelkörning:</b>

python3 scanner.py scan_ip 127.0.0.1 # Skannar localhost

<h3> Sniffer </h3>

Avlyssnar packets som skickas och tas emot på ett nätverk. Detta skript måste köras med root-behörigheter. Skriptet tar emot antal packets som ska sparas, vilket protokoll som ska användas
(standard är tcp) samt namnet på filen där alla packets sparas. Det går även att specificera vilket nätverksgränssnitt som ska avlyssnas, detta argument är valfritt.

<h3>Exempelkörning</h3>

sudo python3 sniffer.py 10 tcp results.pcap --interface wlp1s0 # Samlar in 10 tcp-packets som skickas via wi-fi och sparar dem i filen results.pcap.

<h3>Kända begränsningar</h3>

Användaren måste specificera ett antal packets att samla in, detta gör att skriptet inte är lämpligt 
om användaren inte vet hur många packets som är relevanta att samla in.