from jinja2 import Template, escape


link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''
tm = Template("{{ link | e}}")  # флаг "e" - для экранирование специальных символов
msg = tm.render(link=link)
print(msg)


# Можно сделать тоже самое, используя уже написанный модуль:

msg = escape(link)
print(msg)
