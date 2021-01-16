#!/usr/bin/env python
from model import Страна
from model import Населенный_пункт
from model import Тур
from model import Прайс_лист
from model import Гостиницы
from model import Пользователь
from model import Резервная_копия
from view import View
class Controller:
 def show_user(self):
    users = Страна.get_user()
    return View.show_user(users)
 def add_user(self):
    ID_strani = View.get_data('ID_strani')
    name_strani = View.get_data('name_strani')
    language_strani = View.get_data('language_strani')
    Locality_item_code = View.get_data('Locality_item_code')
    users = Страна.add_user(ID_strani, name_strani, language_strani, Locality_item_code)
#
 def show_np(self):
    np = Населенный_пункт.get_user()
    return View.show_np(np)
 def add_np(self):
    population_code = View.get_data('population_code')
    name_of_the_population = View.get_data('name_of_the_population')
    Tour_ID_Tour = View.get_data('Tour_ID_Tour')
    np = Населенный_пункт.add_user(population_code, name_of_the_population, Tour_ID_Tour)
#
 def show_Tour(self):
     Tour = Тур.get_user()
     return View.show_Tour(Tour)
 def add_Tour(self):
     ID_Tour = View.get_data('ID_Tour')
     type_tour = View.get_data('type_tour')
     duration = View.get_data('duration')
     availability_of_hotels = View.get_data('availability_of_hotels')
     number_of_star_hotels = View.get_data('number_of_star_hotels')
     mode_of_vehicle = View.get_data('mode_of_vehicle')
     point_of_shipping = View.get_data('point_of_shipping')
     Tour = Тур.add_user(ID_Tour, type_tour, duration, availability_of_hotels,
              number_of_star_hotels, mode_of_vehicle, point_of_shipping)
 #
 def show_pl(self):
     pl = Прайс_лист.get_user()
     return View.show_pl(pl)
 def add_pl(self):
     ID_Price_list = View.get_data('ID_Price_list')
     price_tour = View.get_data('price_tour')
     date_tour = View.get_data('date_tour')
     Tour_ID_Tour = View.get_data('Tour_ID_Tour')
     pl = Прайс_лист.add_user(ID_Price_list, price_tour, date_tour, Tour_ID_Tour)
 #
 def show_hotel(self):
     hotel = Гостиницы.get_user()
     return View.show_pl(hotel)
 def add_hotel(self):
     ID_Hotels = View.get_data('ID_Hotels')
     number_of_stars = View.get_data('number_of_stars')
     hotel_name = View.get_data('hotel_name')
     ID_Price_list = View.get_data('ID_Price_list')
     Tour_ID_Tour = View.get_data('Tour_ID_Tour')
     hotel = Гостиницы.add_user(ID_Hotels, number_of_stars, hotel_name, ID_Price_list, Tour_ID_Tour)
 #
 def show_people(self):
     people = Пользователь.get_user()
     return View.show_people(people)

 def add_people(self):
     Passport_number = View.get_data('Passport_number')
     NAMES = View.get_data('NAMES')
     Birth_date = View.get_data('Birth_date')
     people = Пользователь.add_user(Passport_number, NAMES, Birth_date)
 #
 def show_copy(self):
     copy = Резервная_копия.get_user()
     return View.show_copy(copy)

 def add_copy(self):
     ID_backup_copy = View.get_data('ID_backup_copy')
     Creation_date = View.get_data('Creation_date')
     copy = Резервная_копия.add_user(ID_backup_copy, Creation_date)
 #
 def run(self):
    choice = -1
    choices = {1 : lambda : self.show_user(),2 : lambda : self.add_user(),3 : lambda : self.show_np()
               ,4 : lambda : self.add_np(),5 : lambda : self.show_Tour(),6 : lambda : self.add_Tour()
               ,7 : lambda : self.show_pl(),8 : lambda : self.add_pl(),9 : lambda : self.show_hotel()
               ,10 : lambda : self.add_hotel(),11 : lambda : self.show_people(),12 : lambda : self.add_people()
               ,13 : lambda : self.show_copy(),14 : lambda : self.add_copy()}
    while (choice != 0):
       View.show_menu()
       choice = int(View.get_data('choice option'))
       if choice in choices:
           choices[choice]()
if __name__ == '__main__':
 Controller().run()