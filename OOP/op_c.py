
"""
ООП - обьектно орентированное программированиею

Класс - это шаблон для создания обьекта. Он определеняет атрибуты и методы, которые
будут именть все обьекты созданые на его основе.

Обьект - это экземпляр класса. Он имеет собственный набор атрибутов и может вызывать методы, определенные в классе
"""

class Human:
    def __init__(self, age, name, gender, sex) -> None: # <- __init__ конструктор (дандер метод)
        self.age = age
        self.name = name
        self.gender = gender
        self.sex = sex

    def go(self): # <- методы класса
        return 'Пошел'

    def stop(self):
        return 'Остановился'

    def eat(self):
        return 'Поел'

human_one = Human(25, 'Nikita', 'Боевой верталет', 'netral')
human_two = Human(36, 'Boris', 'Стажер', 'male')



class User: # <- название клааса

    count = 0 # <- статический атрибут

    def __init__(self, login, password) -> None: # <- конструктор класса
        self.login = login
        self.password = password
        User.count += 1

    def get_login(self):# <- метод класса
        return self.login
    
    def get_password(self): # <- метод класса
        return self.password
    
    def update_login(self, new_login): # <- метод класса
        self.login = new_login
        return self.login
    
    def update_password(self, new_password): # <- метод класса
        self.password = new_password
        return self.password
    

user_one = User('Girasd@gmail.com', 'h43hgsdg3asfs') # <- создаём экземпляр класса User
print(user_one.get_login())
print(user_one.count, 'user_one')
user_two = User('Jibma@gmail.com', 'h5jhrg4gtsf5')
print(user_two.count, 'user_two')
print(user_one.count, 'user_one')
user_one.update_login('Antsiferov@gmail.com')
print(user_one.get_login())
print(user_two.get_login())