import json
import random
import string

#генерируем имя для теста
name = ''.join([random.choice(string.ascii_lowercase) for n in range(8)])

#генерируем email для теста
email = ''.join([random.choice(string.ascii_lowercase) for n in range(8)])

#генерируем result для теста
result = ''.join([random.choice( string.digits  ) for n in range(1,8,2)])


with open('task_1/data.json', 'w') as outfile:
    json.dump({'name': name, 'email': email+'@mail.ru', 'result': result}, outfile)

