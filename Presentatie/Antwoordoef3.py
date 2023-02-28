import re

def time(string):
    char = re.compile("^[0-23]{2}:[0-59]{2}$")
    string = char.findall(string)
    return (string)

string = ("12:25","68:25","12:","23:59","00:00")
for i in string:
    print(time(i))



