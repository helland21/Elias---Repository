# Definere "klassen" for en student
class Student:
    def __init__(self, navn, student_id):
        self.navn = navn
        self.student_id = student_id

# Definer "klassen" for Grupper - for å funksjonalisere forholdet mellom student og gruppe
class Gruppe:
    def __init__(self, gruppenavn, studenter):
        self.gruppenavn = gruppenavn
        self.studenter = studenter

#Funksjonen som finner ut hvilken gruppe en student hører til basert på student_id og gruppenr. 
def finn_gruppe_for_student(student_id, grupper):
    for gruppe in grupper:
        for student in gruppe.studenter:
            if student.student_id == student_id:
                return gruppe.gruppenavn
    return "Studenten tilhører ingen gruppe" 


# Eksempler som tar utgangspunkt i funksjonen
student1 = Student("Kristian", 2004)
student2 = Student("Nicolai", 2001)
student3 = Student("Endi", 2005)
student4 = Student("Brage", 2003)

gruppe1 = Gruppe("Gruppe Alfa", [student1, student2])
gruppe2 = Gruppe("Gruppe Beta", [student3, student4])

#Tilgjengelige grupper
grupper = [gruppe1, gruppe2]

print(finn_gruppe_for_student(2001, grupper)) #Output: Gruppe Alfa
print(finn_gruppe_for_student(2003, grupper)) #Output: Gruppe Beta
print(finn_gruppe_for_student(1945, grupper)) #Output: Studenten tilhører ingen gruppe 