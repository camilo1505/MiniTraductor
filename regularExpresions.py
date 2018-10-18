import re

string = "0:30"
string2 = "absj:dasdas"

r = re.compile('[0-9]:[0-9][0-9]')

print(r.match(string2))

if(r.match(string2)):
    print("El patron Coincide.")
else:
    print("El patron no coincide.")