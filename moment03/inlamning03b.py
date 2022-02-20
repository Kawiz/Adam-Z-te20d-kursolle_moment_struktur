#fråga där x summa är din input för lön
inkomst = int(input("Vad är din månadslön: "))
 
#Kommunalskatt = 21.36%
kommunalskatt = 0.2136
 
#Landstingsskatt = 11, 48%
landstignsskatt = 0.1148

#årslön som är variabeln för din lön x 12mån
arslön = inkomst * 12 
 
#Utskrift för summa av respektive andel
print("utskrift:")
print("månadslön:", inkomst,"kr")
print("kommunalskatt:", int(inkomst * kommunalskatt),"kr")
print("landstingsskatt:", int(inkomst * landstignsskatt),"kr")
 
#Variabler inför beräkningar
kvar_efter_förstaskatt = inkomst * landstignsskatt
kvar_efter_andraskatt = inkomst * kommunalskatt
kvar_efter_tredjeskatt = kvar_efter_förstaskatt + kvar_efter_andraskatt
kvar_efter_fjärdeskatt = inkomst - kvar_efter_tredjeskatt
 
#Utskriften för summa pengar efterskatt.
print("Kvar efter skatt:" , int(kvar_efter_fjärdeskatt),"kr")

#I detta fall så använder jag mig utav if för att ge programet ett förslag
#till vad programet ska göra ifall det stöter på en sådan summa.
#Därmed kunde jag använda mig utav else funktionen för att visa vad den
#vanligtvis borde göra men det skulle bara bli onödig kod och man vill ju ha en 
#kod som är så simpel som möjligt för att minimera fel riskerna.
if arslön <= 19247:
    print("Men eftersom du tjänar under brytpunkten betalar du ingen skatt ")    
