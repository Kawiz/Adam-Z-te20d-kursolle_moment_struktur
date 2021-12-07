
P = 4*3
A = 3.80
T = 4*3+3.80

print ("Jag handlade 3 pennor för",P,"kr och 1 äpple för",A,"kr vilket totalt blev",T,"kr")

print ("Jag handlade 3 pennor för " + str(P) + "kr och 1 äpple för " + str(A) + "kr vilket totalt blev " + str(T) + "kr.")

s = "Jag handlade 3 pennor för " + str(P)
s += "kr och 1 äpple för " + str(A)
s += "kr vilket totalt blev " + str(T)
s += "kr"
print(s)

print("jag handlade 3 pennor för " + str(P), end="")
print(" kr och 1 äpple för " + str(A), end="" )
print(" kr vilket blev totalt " + str(P+A) + "kr")

print("Jag handlade 3 pennor för {0}kr och 1 äpple för {1}kr vilket blev totalt {2}kr". format(P,A,T))

print("Jag handlade 3 pennor för {0}kr,".format(P))
print("och 1 äpple för {0}kr,".format(A))
print("vilket blev totalt {0}kr.".format(T))
