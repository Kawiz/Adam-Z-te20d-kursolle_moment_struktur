#fråga där x summa är din input för lön
inkomst = int(input("Vad är din månadslön: "))
 
#Kommunalskatt = 21.36%
kommunalskatt = inkomst * 0.2136
 
#Landstingsskatt = 11, 48%
landstignsskatt = inkomst * 0.1148

#årslön som är variabeln för din lön x 12mån
arslön = inkomst * 12

#Den statliga skatten är 20%
statligskatt = inkomst * 0.2

#Denna är värnskatt som apliceras då din årslön överstiger respektive summa.
varnskatt = inkomst * 0.05

#Dessa print kommandon visas obligatoriskt vid varje summa även om du inte behöver betala skatt.
print("utskrift:")
print("månadslön:", (inkomst),"kr", "årsinkomst" ,(arslön),"kr")
print("kommunalskatt:", (kommunalskatt),"kr")
print("landstingsskatt:" ,(landstignsskatt),"kr")

#Detta stycke visas om respektive lön överstiker ena men håller sig innanför andra summan.
if arslön > 468700 and arslön < 675700:
    print("Statlig skatt",(statligskatt))
    print("Kvar efter skatt",(inkomst)-(kommunalskatt)-(landstignsskatt)-(statligskatt))
#Denna kod gäller om respektive lön överstiger denna typ utav summa.
#Då gäller det att visa hur mycket skatt som går till varje område och total mängd kvar.
elif arslön >= 675700:
    print("Statlig skatt",(statligskatt))
    print("Värnskatt",(varnskatt))
    print("Kvar efter skatt",(inkomst)-(kommunalskatt)-(landstignsskatt)-(statligskatt)-(varnskatt))
else:
    print("Kvar efter skatt",(inkomst)-(kommunalskatt)-(landstignsskatt))
#Denna kod visas om respektive lön visas vara under respektive årslön.
if arslön <= 19247:
    print("Eftersom du tjänar inte över skatt gränsen så betalar du ingen skatt.")
 
 
   
 
 
