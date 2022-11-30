def roots(a, b, c, d, e, f):
    # Berechnung der Koeffizienten für h+f*g
    c5 = 0
    c4 = a*d
    c3 = (a*e) + (b*d)
    c2 = (a*f) + (b*e) + (c*d)
    c1 = (b*f) + (c*e)
    c0 = c*f
    # Variable um Vorzeichen Wechsel zu speichern
    VorzeichenWechsel = 0
    # Liste mit den Eingabewerten des Nutzers
    DescartesList = [c5, c4, c3, c2, c1, c0]
    DescartesList = [i for i in DescartesList if i != 0]
    print(DescartesList)

    for x in range(0, len(DescartesList)-1):
        if (DescartesList[x] < 0 and DescartesList[x+1] > 0):
            VorzeichenWechsel = VorzeichenWechsel + 1
        elif (DescartesList[x] > 0 and DescartesList[x+1] < 0):
            VorzeichenWechsel = VorzeichenWechsel + 1

    # Prüfen ob Vorzeichenwechsel gerade Anzahl oder ungerade Anzahl
    if (VorzeichenWechsel % 2 == 0):
        return("Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln.")
    else:
        return ("Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln.")


print(roots(1,-2,-1,2,1,2))
print(roots(0,0,0,0,0,0))
print(roots(15,-41,0,0,-90,31))