
#Exo 3: Programme informatique pour enregistrer les etudiants a Marien Ngouabi	
class Etudiant:

	def __init__(self, name_student, school_level, student_certificate):
		self.name = name_student
		self.school_level = school_level
		self.student_certificate = student_certificate
my_student = Etudiant("Precieuse", "Debutant", "Baccalaureat")

#print("my_student")
print(my_student.name, my_student.school_level, my_student.student_certificate)

	
		
