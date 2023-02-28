import re
def speciale_tekens(string):
    charRe = re.compile('[^a-zA-Z0-9]')
    string = charRe.search(string)
    return bool(string)

print(speciale_tekens("ABCDEFabcdef123450")) 
print(speciale_tekens("*&%@#!}{"))