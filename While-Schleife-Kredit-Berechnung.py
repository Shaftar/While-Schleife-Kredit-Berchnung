""" Rueckzahlung eines Kredites Berchnen
    Autor: Mohamad Shaftar
    Datum: 28.09.2019
    """

import datetime  # Datum importieren

kredithoehe = int(input('Kreditsumme in Euro: '))  # Kredithoehe eingeben
zinsen = int(input('Zinssatz in Prozent: '))  # Zinssatz eingeben
zahlungsbetrag = int(input('Jaehrlicher Rueckzahlungsbetrag in Euro: '))  # Rueckzahlungsbetrag eingeben
while kredithoehe <= 0 or zinsen <= 0 or zahlungsbetrag <= 0:  # Eingabe ueberpruefen
    # Falls die Eingabe falsch ist, soll der Benutzer nochmal eingeben
    kredithoehe = int(input('Kreditsumme nochmal eingeben: '))
    zinsen = int(input('Zinssatz nochmal eingeben: '))
    zahlungsbetrag = int(input('Jaehrlicher Rueckzahlungsbetrag nochmal eingeben: '))
    continue  # Wenn Eingabe richtig ist
zinssatz = 0  # Zinssatz anfangswert, wird sich aendern
geldbezahlt = 0  # Rueckzahlung ohne Zinsen
rest = 0  # Rest ohne Zinsen
counter = 1  # Dauerzeit
gesamtesumme = kredithoehe  # Insgesamtezahlung
restmitzins = 0  # Zur Berechnung von Zinssatz letzter Zahlung
aktuellesjahr = datetime.date.today().year  # Aktulles Jahr
while True:  # Endlos Schleife, weil wir keine andere Moeglichkeit haben
    print('.....................', str(aktuellesjahr), ': ')  # Das Jahr entsprechend ausgebnen
    zinssatz = kredithoehe * zinsen / 100  # Zinssatz berechnen
    print('Zinsen: ', round(zinssatz), ' Euro')  # Zinssatz Ausgabe
    geldbezahlt = zahlungsbetrag - zinssatz  # Was man tatsaechlich rueckzahlt
    print('Tiglung: ', round(geldbezahlt), ' Euro')  # Was man bezahlt hat, soll ausgeben
    rest = kredithoehe - geldbezahlt  # Die eigentliche Rest, Was man zu zahlen hat
    kredithoehe = rest  # Alter Wert wird von neuen Wert ersaetzt
    print('Rest: ', round(rest), ' Euro')  # Rest Ausgabe
    aktuellesjahr += 1  # Jahr um 1 erhoeht
    counter += 1  # Dauer Jahren berchnen
    gesamtesumme += zinssatz  # gesamte Summe mit Zinssatz
    if kredithoehe < geldbezahlt:  # Wenn die Zuzahlungssumme kleiner als was man zahlen muss
        restmitzins = kredithoehe * 10 / 100  # Berechnen von Zinssatz
        kredithoehe += restmitzins  # Rest mit Zinssatz
        print('.....................',str(aktuellesjahr), ': ')  # Letzte Jahr ausgeben
        print('Rest: ', round(kredithoehe))  # Rest ausgeben
        print('Sie zahlen insgesamt: ', round(gesamtesumme + restmitzins), ' Euro in ', counter,
              ' Jahren')  # Ausgabe wenn mann wissen will, was und in wie viele Jahren zahlen muss
        break      # While Schleife beenden
