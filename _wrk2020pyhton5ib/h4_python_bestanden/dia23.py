from mijnPackageh4.teller import Teller


def uitvoeren():
  '''dit is een fucntie waarmee we alles uitvoeren'''
  objteller = Teller()

  objteller.increment()

  objteller.tellerstaataan = True

  objteller.increment()
  objteller.increment() 
  objteller.verdubbel()
  print("de teller staat op ", objteller.waarde)

uitvoeren()


