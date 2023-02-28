from string import Template
import re

name = 'Tim'
surname = "Bleuze"

x = 'Hello, %s %s' % (name, surname)
print(x)

name = 'Tim'
surname = "Bleuze"

x = 'Hello, %(name)s %(surname)s' % {"surname":surname,"name": name}
print(x)

x = 'Hello, {0} {1}'.format(name,surname)
print(x)
x = 'Hello, {name} {surname}'.format(surname=surname,name=name)
print(x)

x = f'Hello, {name} {surname}'
print(x)

a=10
b=5

x = f'{a+b} / {2*(a+b)}'
print(x)

def test(name,surname):
    return "Hallo:" + name + ' '+surname

def test2(name,surname):
    return f"Hallo: {name} {surname}"

print(test("tim","bleuze"))
print(test2("tim","bleuze"))

t = Template('Hallo, $name $surname')
print(t.substitute(name=name,surname=surname))

x = 'Hallo, name sur'
x=re.sub("name",name,x)
x=re.sub("sur",surname,x)
print(x)

