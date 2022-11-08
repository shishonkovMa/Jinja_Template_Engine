from jinja2 import Template


cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Scoda', 'price': 17300},
    {'model': 'Volvo', 'price': 44300},
    {'model': 'Volkswagen', 'price': 21300}
]

tpl = "Суммарная цена автомобилей: {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)


# Другой пример с суммой списка

digs = [1, 2, 3, 4, 5]
tpl = "Суммарная цена автомобиля: {{ cs | sum }}"
tm = Template(tpl)
msg = tm.render(cs=digs)
print(msg)


# Если хотим вывести название модели с максимальной ценой

tpl = "Максимальная цена среди автомобилей: {{ (cs | max(attribute='price')).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)


# Выбрать рандомную запись

tpl = "Автомобиль: {{ cs | random }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)


# Замена букв

tpl = "Автомобиль: {{ cs | replace('o', 'O') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)


# Существует множество других фильтров, среди них:
# last, min, unique и т.д.
