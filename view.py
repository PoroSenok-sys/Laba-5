import mysql.connector
from datetime import date
#!/usr/bin/env python
class View:
 @staticmethod
 def show_user(list):
    print(f'in database {len(list)} Страна. they are:')
    print(list)
#
 @staticmethod
 def show_np(list):
    print(f'in database {len(list)} Населенный_пункт. they are:')
    print(list)
#
 @staticmethod
 def show_Tour(list):
     print(f'in database {len(list)} Тур. they are:')
     print(list)
 #
 @staticmethod
 def show_pl(list):
     print(f'in database {len(list)} Прайс_лист. they are:')
     print(list)
 #
 @staticmethod
 def show_hotel(list):
     print(f'in database {len(list)} Гостиницы. they are:')
     print(list)
 #
 @staticmethod
 def show_people(list):
     print(f'in database {len(list)} Пользователь. they are:')
     print(list)
 #
 @staticmethod
 def show_copy(list):
     print(f'in database {len(list)} Резервная_копия. they are:')
     print(list)
 #
 @staticmethod
 def get_data(text):
    return input('enter ' + text + ':')
 @staticmethod
 def show_menu():
    print('what do you want:\n'+
        '\t (1) show Страна\n'+
        '\t (2) add Страна\n'+
        '\t (3) show Населенный_пункт\n' +
        '\t (4) add Населенный_пункт\n' +
        '\t (5) show Тур\n' +
        '\t (6) add Тур\n' +
        '\t (7) show Прайс_лист\n' +
        '\t (8) add Прайс_лист\n' +
        '\t (9) show Гостиницы\n' +
        '\t (10) add Гостиницы\n' +
        '\t (11) show Пользователь\n' +
        '\t (12) add Пользователь\n' +
        '\t (13) show Резервная_копия\n' +
        '\t (14) add Резервная_копия\n' +
        '\t (0) exit\n')