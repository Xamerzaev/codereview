class Person():
    pass
    def see_the_sign(signs):
        print('Загружаю...')
        for sign in signs:
            print(f'Этот знак называется - {sign}')

# базовый экземпляр
class Sign:
    def __init__(self, id, name):
        self.id = id
        self.name = name