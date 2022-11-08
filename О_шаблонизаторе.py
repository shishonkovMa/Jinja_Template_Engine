from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


per = Person('Федор', 33)

tm = Template('Мне {{ p.getAge() }} лет и зовут {{ p.getName() }}.')
msg = tm.render(p=per)
print(msg)

# Можно при использовании словаря
per = {'name': "Федор", 'age': 34}
tm = Template('Мне {{ p["age"] }} лет и зовут {{ p["name"] }}.')
msg = tm.render(p=per)
print(msg)
