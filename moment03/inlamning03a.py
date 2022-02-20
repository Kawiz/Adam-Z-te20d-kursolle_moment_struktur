#fråga där x summa är din input för lön
inkomst = int(input("Vad är din månadslön: "))
 
#Kommunalskatt = 21.36%
kommunalskatt = 0.2136
 
#Landstingsskatt = 11, 48%
landstignsskatt = 0.1148
 
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
 
 

