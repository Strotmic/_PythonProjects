from mijnPackageh4.teller import Teller

def uitvoeren(): 
  objteller = Teller()
  objteller.tellerstaataan = True
  objteller.tellerstaataan = False

  toestand = objteller.tellerstaataan

  print ("de toestand van de teller is :" , toestand)
  
  stand = objteller.waarde      
  print ("de teller staat nu op " , stand)
  

uitvoeren()
