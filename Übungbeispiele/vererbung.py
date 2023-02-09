# vererbung.py

class Person:
    
    def __init__(self, vorname, nachname, geburtsdatum):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        
    def __str__(self):
        return self.vorname + " " + self.nachname + ", " + self.geburtsdatum
        
class TU_Mitarbeiter_in(Person):
    
    def __init__(self, vorname, nachname, geburtsdatum, personalnr):
        Person.__init__(self, vorname, nachname, geburtsdatum)
        ## alternativ:
        # super().__init__(vorname, nachname, geburtsdatum)
        self.personalnr = personalnr
        
    def __str__(self):
        return Person.__str__(self) + ", " + self.personalnr
        ## alternativ:
        # return super().__str__() + ", " + self.personalnr

class TU_Student_in(Person):
    
    def __init__(self, vorname, nachname, geburtsdatum, matrikelnr):
        Person.__init__(self, vorname, nachname, geburtsdatum)
        ## alternativ:
        # super().__init__(vorname, nachname, geburtsdatum)
        self.matrikelnr = matrikelnr
        
    def __str__(self):
        return Person.__str__(self) + ", " + self.matrikelnr
        ## alternativ:
        # return super().__str__() + ", " + self.matrikelnr

x = Person("Emily", "Shuckburgh", "?")
y = TU_Mitarbeiter_in("Alice", "Weiß", "12.05.1993", "0749")
z = TU_Student_in("Thomas", "Schwarz", "17.03.2002", "405589")
print(x)
print(y)
print(z)
