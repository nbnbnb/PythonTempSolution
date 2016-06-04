class Person(object):
    name = 'ZhangJin'

p=Person()

print(p.name)
print(Person.name)
print(dir(p))
p.name=u'张进'
print(dir(p))
print(p.name)
print(Person.name)
print(dir(Person))