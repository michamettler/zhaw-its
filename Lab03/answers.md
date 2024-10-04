### Frage 1
Sie werden feststellen, dass man beim mit AES_ECB verschlüsselten png File den Tux nach wie
vor erkennt, beim gif File jedoch nicht. Warum ist das so?

Die Anzahl der Farben ist bei GIF viel tiefer.

### Frage 2
Warum erkennt man bei AES_CBC und AES_GCM in keinem der verschlüsselten Bilder den Tux?

Aufgrund des Initialisierungsvektors. XOR Verlinkung bei CBC.

### Frage 3
Wie gelangen Sie zum Initialisierungsvektor, welcher in ihrem Code verwendet wird? Und falls Sie
das verschlüsselte Bild jemandem schicken möchten, woher würde der Empfänger den IV kennen?
(Sie müssen keinen Code dazu schreiben, aber eine plausible Antwort liefern können).

Der Initialisierungsvektor wird zufällig erstellt (get_random_bytes()) mit der Anzahl AES.block_size, die auch für das Padding genutzt wird. Dem Empfänger kann ich den IV mitteilen da dieser nicht geheim sein muss.

### Frage 4
Falls Sie eine AI als Hilfe für die Code Generierung verwendet haben: Welchen Mode hat Sie vorgeschlagen? Was denken Sie, warum hat sie diesen Mode vorgeschlagen? Ist der gewählte Mode
eine gute Wahl? Welche Schlüsse ziehen Sie sonst aus der Wahl des Modes von der AI?

Der ECB Mode wurde vorgeschlagen, vermutlich weil ich vermutlich während des Programmierens noch keinen IV definiert hatte.