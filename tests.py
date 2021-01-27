import unittest
import os
from app import app, db, Hotel, Price, Country, Settlement, Tour
class TestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join('test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home(self):
        result = self.app.get('/')

    def test_hostel(self):
        h = Hotel(title='СеверНаш', Star='4 звезда')
        db.session.add(h)
        db.session.commit()
        assert h.title == 'СеверНаш'
        assert h.Star == '4 звезда'

    def test_price_list(self):
        p = Price(id_tour='1 Тур', title_hostel='Мантикора', price_tour='20 000', date_tour='18.06.2021')
        db.session.add(p)
        db.session.commit()
        assert p.id_tour == '1 Тур'
        assert p.title_hostel == 'Мантикора'
        assert p.price_tour == '20 000'
        assert p.date_tour == '18.06.2021'

    def test_country(self):
        c = Country(title_country='Тут вот живу', country_language='Такой вот язык')
        db.session.add(c)
        db.session.commit()
        assert c.title_country == 'Тут вот живу'
        assert c.country_language == 'Такой вот язык'

    def test_settlement(self):
        s = Settlement(title_settlement='Сургут', settlement_code='221A')
        db.session.add(s)
        db.session.commit()
        assert s.title_settlement == 'Сургут'
        assert s.settlement_code == '221A'

    def test_tour(self):
        t = Tour(type_tour='Прогулка', duration='21 день', title_settlement='Сургут', hotel_availability='Гостиница есть',
                 title_hostel='Мантикора', mode_vehicle='Пешком', point_shipping='Там вот')
        db.session.add(t)
        db.session.commit()
        assert t.type_tour == 'Прогулка'
        assert t.duration == '21 день'
        assert t.title_settlement == 'Сургут'
        assert t.hotel_availability == 'Гостиница есть'
        assert t.title_hostel == 'Мантикора'
        assert t.mode_vehicle == 'Пешком'
        assert t.point_shipping == 'Там вот'

if __name__ == '__main__':
    unittest.main()