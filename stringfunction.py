#w="welcome"
#print(w.find('e',2))
#w="welcome"
#print(w.index('o'))

#ISALPHA
w="welcome"
print(w.isalpha())#true
w="welcome123"
print(w.isalpha())#false

w="123245"
print(w.isdigit())#true

w="welcome1223"
print(w.isalnum())#true

w="wel123@!"
print(w.isalnum())#false


