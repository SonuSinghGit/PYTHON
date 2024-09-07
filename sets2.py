a={23,34,45,56,7}
for i in a:
    print(i)

a.add(12)
print(a)

a.pop()
print(a)

a.remove(45)
print(a)
a.discard(23)
print(a)

a.clear()
print(a)
#update
a={23,34,45,56,7}
b={23,59,95,3}
a.update(b)
print(a)