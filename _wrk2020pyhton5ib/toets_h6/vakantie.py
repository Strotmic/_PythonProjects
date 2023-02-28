from package.student import Student

def vakantie():
  """hier maken we een 2 nieuwe studenten genaaamd objstudent1 en objstudent2"""
  objstudent1 = Student("Bollie", 80)
  objstudent2 = Student("Nerdie", 60)
  #objstudent1 is Bollie,80kg en objstudent2 is Nerdie, 60kg


  objstudent1.snoepen()  
  objstudent1.snoepen()
  #Bollie snoept 2x

  objstudent2.studeren()
  objstudent2.studeren()
  #objstudent studeert 2x

  message1 = "objstudent1 is {0} en weegt {1}"
  message2 = "objstudent2 is {0} en weegt {1}"
  message1 = message1.format(objstudent1.naam, objstudent1.gewicht)
  message2 = message2.format(objstudent2.naam, objstudent2.gewicht)
  #hier hebben we 2 messages gemaakt met elk hun eigen output


  print(message1)
  print(message2)
  #hier printen we de 2 messages

vakantie()