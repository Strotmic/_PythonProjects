from mijnPackageh4.celcius import Celcius

def verwerking():
  objcelcius = Celcius()

  resultaat = objcelcius.to_farenheid()
  message = "{0} graden celcius is {1} graden farenheid"
  message = message.format(objcelcius.temperatuur, resultaat)
  print(message)


verwerking()  