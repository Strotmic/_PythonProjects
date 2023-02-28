from mijnPackageh4.auto import Auto

def uitvoeren():
  auto = Auto(0)

  auto.autostaataan = True
  auto.versnellen()
  message = "de auto rijd {0} km per uur"
  message = message.format(auto.snelheid)
  print(message)

uitvoeren()