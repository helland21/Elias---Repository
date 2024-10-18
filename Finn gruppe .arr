use context starter2024
#Opprett studenter 
#student1 = Student "(Elias Helland, 1, gruppe1) 
#student2 = Student "(Seline Helland, 2, gruppe1) 
#student3 = Student "(Brage Olsen, 3, gruppe2) 
#student4 = Student "(Trym Jansen, 4, gruppe2) 
#student5 = Student "(Nicolai Østerhus, 5, gruppe1)

students = table: 
  firstName, studentID, group 
  row: "Elias Helland", "1", "Gruppe1"
  row: "Seline Helland", "2", "Gruppe1"
  row: "Brage Olsen", "3", "Gruppe2"
  row: "Trym Jansen", "4", "Gruppe2"
  row: "Nicolai Østerhus", "5", "Gruppe1"
end 

fun finngruppe(navn, liste): 
  liste. filter(lam(row): row ["firstName"] == navn 
    end)
end

#Test funksjonen 

finngruppe("Seline Helland", students)