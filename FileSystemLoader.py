from jinja2 import Environment, FileSystemLoader


persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

file_loader = FileSystemLoader('templates')  # Из какого подкаталога мы будем брать шаблоны
env = Environment(loader=file_loader)

tm = env.get_template('main.htm')  # Формирует экземпляр класса Template на основе содержимого main.htm
msg = tm.render(users=persons)
print(msg)


# Существуют также другие загрузчики, среди них:

#  * PackageLoader - для загрузки шаблонов из пакета;
#  * DictLoader - для загрузки шаблонов из словаря;
#  * FunctionLoader - для загрузки на основе функции;
#  * PrefixLoader - загрузчик, использующий словарь для построения подкаталогов;
#  * ChoiceLoader - загрузчик, содержащий список других загрузчиков
#                                               (если он не сработает, выбирается следующий);
#  * ModuleLoader - загрузчик для скомпилированных шаблонов
