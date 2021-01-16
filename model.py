import mysql.connector
from datetime import date
#!/usr/bin/env python
class Страна:
 def __init__(self, ID_strani=0, name_strani=None, language_strani=None, Locality_item_code=None):
    self.ID_strani = ID_strani
    self.name_strani = name_strani
    self.language_strani = language_strani
    self.Locality_item_code = Locality_item_code
 @property
 def info(self):
    return f'{self.ID_strani} | {self.name_strani} | {self.language_strani} | {self.Locality_item_code}'

 @staticmethod
 def get_user():
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    result = []
    client = conn.cursor()
    client.execute('select * from Страна')
    for i in client:
         result.append(i)
         client.close()
         conn.close()
         return i

 @staticmethod
 def add_user(ID_strani, name_strani, language_strani, Locality_item_code):
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    c = conn.cursor()
    c.execute('insert into Страна values(%s, %s, %s, %s)',(int(ID_strani), name_strani, language_strani, int(Locality_item_code)))
    conn.commit()
    c.close()
    conn.close()
###################################################
class Населенный_пункт:
 def __init__(self, population_code=0, name_of_the_population=None, Tour_ID_Tour=0):
    self.population_code = population_code
    self.name_of_the_population = name_of_the_population
    self.Tour_ID_Tour = Tour_ID_Tour
 @property
 def info(self):
    return f'{self.population_code} | {self.name_of_the_population} | {self.Tour_ID_Tour}'

 @staticmethod
 def get_user():
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    result = []
    client = conn.cursor()
    client.execute('select * from Населенный_пункт')
    for i in client:
         result.append(i)
         return i

 @staticmethod
 def add_user(population_code, name_of_the_population, Tour_ID_Tour):
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    c = conn.cursor()
    c.execute('insert into Населенный_пункт values(%s, %s, %s)',(int(population_code), name_of_the_population, int(Tour_ID_Tour)))
    conn.commit()
    c.close()
    conn.close()
###################################################
class Тур:
 def __init__(self, ID_Tour=0, type_tour=None, duration=0, availability_of_hotels=None,
              number_of_star_hotels=0, mode_of_vehicle=None, point_of_shipping=None):
    self.ID_Tour = ID_Tour
    self.type_tour = type_tour
    self.duration = duration
    self.availability_of_hotels = availability_of_hotels
    self.number_of_star_hotels = number_of_star_hotels
    self.mode_of_vehicle = mode_of_vehicle
    self.point_of_shipping = point_of_shipping
 @property
 def info(self):
    return f'{self.ID_Tour} | {self.type_tour} | {self.duration} | {self.availability_of_hotels}' \
           f' | {self.number_of_star_hotels} | {self.mode_of_vehicle} | {self.point_of_shipping}'

 @staticmethod
 def get_user():
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    result = []
    client = conn.cursor()
    client.execute('select * from Тур')
    for i in client:
         result.append(i)
         return i

 @staticmethod
 def add_user(ID_Tour, type_tour, duration, availability_of_hotels,
              number_of_star_hotels, mode_of_vehicle, point_of_shipping):
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    c = conn.cursor()
    c.execute('insert into Тур values(%s, %s, %s, %s, %s, %s, %s)',(int(ID_Tour),
                                                        type_tour, int(duration),
                                                        availability_of_hotels,int(number_of_star_hotels),
                                                        mode_of_vehicle,point_of_shipping))
    conn.commit()
    c.close()
    conn.close()
###################################################
class Прайс_лист:
 def __init__(self, ID_Price_list=0, price_tour=0, date_tour=None, Tour_ID_Tour=0):
    self.ID_Price_list = ID_Price_list
    self.price_tour = price_tour
    self.date_tour = date_tour
    self.Tour_ID_Tour = Tour_ID_Tour
 @property
 def info(self):
    return f'{self.ID_Price_list} | {self.price_tour} | {self.date_tour} | {self.Tour_ID_Tour}'

 @staticmethod
 def get_user():
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    result = []
    client = conn.cursor()
    client.execute('select * from Прайс_лист')
    for i in client:
         result.append(i)
         return i

 @staticmethod
 def add_user(ID_Price_list, price_tour, date_tour, Tour_ID_Tour):
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    c = conn.cursor()
    c.execute('insert into Прайс_лист values(%s, %s, %s, %s)',(int(ID_Price_list), float(price_tour),
                                                               date.fromisoformat(date_tour), int(Tour_ID_Tour)))
    conn.commit()
    c.close()
    conn.close()
###################################################
class Гостиницы:
 def __init__(self, ID_Hotels=0, number_of_stars=0, hotel_name=None, ID_Price_list=0, Tour_ID_Tour=0):
    self.ID_Hotels = ID_Hotels
    self.number_of_stars = number_of_stars
    self.hotel_name = hotel_name
    self.ID_Price_list = ID_Price_list
    self.Tour_ID_Tour = Tour_ID_Tour
 @property
 def info(self):
    return f'{self.ID_Hotels} | {self.number_of_stars} | {self.hotel_name} ' \
           f'| {self.ID_Price_list} | {self.Tour_ID_Tour}'

 @staticmethod
 def get_user():
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    result = []
    client = conn.cursor()
    client.execute('select * from Гостиницы')
    for i in client:
         result.append(i)
         return i

 @staticmethod
 def add_user(ID_Hotels, number_of_stars, hotel_name, ID_Price_list, Tour_ID_Tour):
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    c = conn.cursor()
    c.execute('insert into Гостиницы values(%s, %s, %s, %s, %s)',(int(ID_Hotels), int(number_of_stars),
                                                               hotel_name,int(ID_Price_list),
                                                              int(Tour_ID_Tour)))
    conn.commit()
    c.close()
    conn.close()
###################################################
class Пользователь:
 def __init__(self, Passport_number=0, NAMES=None, Birth_date=None):
    self.Passport_number = Passport_number
    self.NAMES = NAMES
    self.Birth_date = Birth_date
 @property
 def info(self):
    return f'{self.Passport_number} | {self.NAMES} | {self.Birth_date}'

 @staticmethod
 def get_user():
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    result = []
    client = conn.cursor()
    client.execute('select * from Пользователь')
    for i in client:
         result.append(i)
         return i

 @staticmethod
 def add_user(Passport_number, NAMES, Birth_date):
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    c = conn.cursor()
    c.execute('insert into Пользователь values(%s, %s, %s)',(int(Passport_number), NAMES,
                                                             date.fromisoformat(Birth_date)))
    conn.commit()
    c.close()
    conn.close()
###################################################
class Резервная_копия:
 def __init__(self, ID_backup_copy=0, Creation_date=None):
    self.ID_backup_copy = ID_backup_copy
    self.Creation_date = Creation_date
 @property
 def info(self):
    return f'{self.ID_backup_copy} | {self.Creation_date}'

 @staticmethod
 def get_user():
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    result = []
    client = conn.cursor()
    client.execute('select * from Резервная_копия')
    for i in client:
         result.append(i)
         return i

 @staticmethod
 def add_user(ID_backup_copy, Creation_date):
    conn = mysql.connector.connect(user='user', password='123456789qweR', host='localhost', database='db1')
    c = conn.cursor()
    c.execute('insert into Резервная_копия values(%s, %s)',(int(ID_backup_copy),
                                                             date.fromisoformat(Creation_date)))
    conn.commit()
    c.close()
    conn.close()
###################################################