# Hilfe zur schnellen Orientierung in einem Supermarkt mit Eingabe von Artikeln durch Kunden an z. B Tablett am Eingang
# Das Sortiment kann beliebig ergänzt oder erweitert werden (Oberbegriff, Art, Markenartikel)
# Im Supermarkt befinden sich angenommen 10 Gänge mit jeweils 10 Regalen und 5 Fächern

print()
print("Eier = 1", "Mehl = 2", "Zucker = 3", "Wurst = 4", "Käse = 5", "Milch = 6", "Lakritz = 7", "Saft = 8", "Butter = 9", "Brot = 10")
print()

def liste_eins():
 print("Eier sind im Gang 1, Regal 1, Fach 2")
def liste_zwei():
 print("Mehl ist im Gang 1, Regal 2, Fach 4")
def liste_drei():
 print("Zucker ist im Gang 1, Regal 3, Fach 3")
def liste_vier():
    print("Wurst ist im Gang 2, Regal 4, Fach 3")
def liste_fünf():
    print("Käse ist im Gang 2, Regal 1, Fach 2")
def liste_sechs():
    print("Milch ist im Gang 3, Regal 5, Fach 2")
def liste_sieben():
    print("Lakritz ist im Gang 4, Regal 4, Fach 1")
def liste_acht():
    print("Saft ist im Gang 5, Regal 4, Fach 1")
def liste_neun():
    print("Butter ist im Gang 6, Regal 4, Fach 5")
def liste_zehn():
    print("Brot ist im Gang 7, Regal 4, Fach 5")

print("Herzlich Willkommen im Supermarkt ...")
print("Jedes vorhandende Produkt befindet sich in an einem bestimmten Ort!")
print()

Auswahl = int(input("Geben Sie eine Zahl zwischen 1 und 10 ein für das gesuchte Produkt:" ))
print()

if Auswahl <= 1:
    liste_eins()
elif Auswahl <= 2:
    liste_zwei()
elif Auswahl <= 3:
    liste_drei()
elif Auswahl <= 4:
   liste_vier()
elif Auswahl <= 5:
   liste_fünf()
elif Auswahl <= 6:
    liste_sechs()
elif Auswahl <= 7:
   liste_sieben()
elif Auswahl <= 8:
   liste_acht()
elif Auswahl <= 9:
   liste_neun()
else:
   Auswahl <= 10
   liste_zehn()

print()
print("Vielen Dank für Ihren Einkauf!")
print("Der tatsächliche Bestand wird nun abgefragt:")
print("Der Mitarbeiter muss die vorhandenen Waren aber zur Sicherheit zählen!")
print()
def wochentage_liste():
    print("Mo = 9", "Die = 8", "Mit = 7", "Do = 6", "Fr = 5", "Sa = 4", "So = 3")
wochentage_liste()
print()
Auswahl2 = int(input("Geben Sie eine zweite Zahl ein zwischen 1 und 9 für den jeweiligen Wochentag:" ))
print()
for Einkauskorb in range(1):
    print(Auswahl2)
    print("Stück sind noch vorhanden")
    print()
if Auswahl2 < 5:
    print("ACHTUNG! Es muss nachbestellt werden")
    print()
else:
    print("Der momentane Bestand reicht aus...")
    print()

print("Sollten Sie nicht mit uns zufrieden sein können Sie gerne zu der Konkurrenz gehen")
print("Wir geben Ihnen Alternativen in der unmittelbaren Nähe vor")
print("Dort können Sie auch nach Artikeln suchen")
print()
Sortiment = input("Geben Sie einen Artikelnamen ein:")
print()
print(Sortiment)
print("IST LEIDER AUSVERKAUFT!")
print("Das war ein Scherz lol")
def Supermarkt_list():
   print("Norma = 1", "Lidl = 2", "Aldi = 3", "Kaufland = 4", "REWE = 5")
print()
Supermarkt_list()

Auswahl3 = int(input("Geben Sie den Namen eines Supermarktes ein:" ))
print()
if Auswahl3 < 1:
   print("Norma")
   print("Ist leider nicht in Ihrer Nähe")
elif Auswahl3 <= 2:
   print("Lidl")
   print("Ist in Ihrer Nähe")
elif Auswahl3 <= 3:
   print("Kaufland")
   print("Ist leider nicht in Ihrer Nähe")
else:
   print("REWE")
   print("Ist in Ihrer Nähe")
print()
print("Informationen für den Weg aus dem Internet entnehmen")
print("Ich hoffe Ihnen hat das Program gefallen :-)")