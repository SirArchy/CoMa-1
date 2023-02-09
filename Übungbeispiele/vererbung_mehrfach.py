# vererbung_mehrfach.py

class Person:
    
    def __init__(self, vorname, nachname, geburtsdatum):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        
    def __str__(self):
        return self.vorname + " " + self.nachname + ", " + self.geburtsdatum
        
class TU_Mitarbeiter_in(Person):
    
    def __init__(self, vorname, nachname, geburtsdatum, personalnr):
        ## korrekte Variante:
        Person.__init__(self, vorname, nachname, geburtsdatum)
        ## fuehrt zu Fehler bei Tutor_in:
        # super().__init__(vorname, nachname, geburtsdatum)
        self.personalnr = personalnr
        
    def __str__(self):
        ## fuehrt zu fehlender Matrikelnr. bei TU_Tutor_in:
        # return Person.__str__(self) + ", " + self.personalnr
        ## Korrekte Variante:
        return super().__str__() + ", " + self.personalnr

class TU_Student_in(Person):
    
    def __init__(self, vorname, nachname, geburtsdatum, matrikelnr):
        ## beide Varianten sind moeglich:
        # Person.__init__(self, vorname, nachname, geburtsdatum)
        super().__init__(vorname, nachname, geburtsdatum)
        self.matrikelnr = matrikelnr
        
    def __str__(self):
        ## beide Varianten sind moeglich:
        # return Person.__str__(self) + ", " + self.matrikelnr
        return super().__str__() + ", " + self.matrikelnr
        
class TU_Tutor_in(TU_Mitarbeiter_in,TU_Student_in):
    
    def __init__(self, vorname, nachname, geburtsdatum,  matrikelnr, personalnr):
        TU_Mitarbeiter_in.__init__(self, vorname, nachname, geburtsdatum, personalnr)
        TU_Student_in.__init__(self, vorname, nachname, geburtsdatum, matrikelnr)
        
    def __str__(self):
        return super().__str__() + ", " + "Tutor_in"

x = Person("Emily", "Shuckburgh", "?")
y = TU_Mitarbeiter_in("Alice", "Weiß", "12.05.1993", "0749")
z = TU_Student_in("Thomas", "Schwarz", "17.03.2002", "405589")
t = TU_Tutor_in("Amina", "Annabi", "19.11.1998", "401031","0521")
print(x)
print(y)
print(z)
print(t)
