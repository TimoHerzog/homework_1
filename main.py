import math

#Ich plane ein Fest bei dem Studierende durch einen Sponsor einen Rabatt auf Getränke bekommen. Der Rabatt ist abhängig von der Wahlbeteiligung und wird auf die 1.Nachkommastelle aufgerundet.

def price(old_price, voter_turnout): #Berechnung der Rabatts und der neuen Getränkepreise
    discount = (voter_turnout / 100) * old_price #Berechnung Rabatt
    reduced_price = old_price - discount #Berechnung neuer Preis
    new_price = math.floor(reduced_price * 10) / 10 #Abrunden auf 1.Kommastelle des neuen Preises
    discount = old_price - new_price #Aufgerundeter Rabatt
    return (new_price, discount) 


def discount_complete(discount_alcohol, discount_nonalcohol, number_alcohol, number_nonalcohol): #Berechnung der gesamten Ersparnisse
    saving_alcohol = discount_alcohol * number_alcohol #Ersparnis dur alkoholische Getränke
    saving_nonalcohol = discount_nonalcohol * number_nonalcohol #Ersparnis durch antialkoholische Getränke
    return saving_alcohol + saving_nonalcohol
    

old_price_alcohol = float(input(f"Bitte geben Sie den ursprünglichen Getränkepreis für alkoholische Getränke in € ein: ")) #Eingabe des ursprünglichen Getränkepreises für alkoholische Getränke.
old_price_nonalcohol = float(input(f"Bitte geben Sie den ursprünglichen Getränkepreis für alkoholfreie Getränke in € ein: ")) #Eingabe des ursprünglichen Getränkepreises für antialkoholische Getränke.
voter_turnout = float(input(f"Bitte geben Sie die Wahlbeteiligung in % ein: ")) #ingabe der Wahlbeteiligung.
number_alcohol = float(input("Geben Sie die Anzahl an alkoholischen Getränken ein die Sie trinken: ")) #Eingabe der Anzahl an alkoholishen Getränken
number_nonalcohol = float(input("Geben Sie die Anzahl an antialkoholischen Getränken ein die Sie trinken: ")) #Eingabe der Anzahl an antialkoholishen Getränken
new_price_alcohol, discount_alcohol = price(old_price_alcohol, voter_turnout) #Berechnung des neuen Preises und des Rabatts für alkoholische Getränke
new_price_nonalcohol, discount_nonalcohol = price(old_price_nonalcohol, voter_turnout) #Berechnung des neuen Preises und des Rabatts für antialkoholische Getränke
saving = discount_complete(discount_alcohol, discount_nonalcohol, number_alcohol, number_nonalcohol) #Berechnung der gesamten Ersparnisse
print(f"Bei einer Wahlbeteiligung von {voter_turnout:.2f}% ergibt sich ein Getränkepreis für alkoholische Getränke von {new_price_alcohol:.2f}€. Das ist ein Rabatt von {discount_alcohol:.2f}€. \nFür alkoholfreie Getränke ergibt sich ein Preis von {new_price_nonalcohol:.2f}€. Das ist eine Ersparnis von {discount_nonalcohol:.2f}€. \nDa ich {number_alcohol:.0f} alkoholische und {number_nonalcohol:.0f} antialkoholische Getränke getrunken habe, sparte ich mir {saving:.2f}€.")  #Ausgabefunktion für die neuen Preise und dabei erreichten Rabatte
