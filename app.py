from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Star = db.Column(db.Integer, nullable=True)
    title = db.Column(db.String(100), nullable=False)
    tours = db.relationship('Tour', backref = 'name_hostel', lazy = 'dynamic')

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.title)


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_tour = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False)
    title_hostel = db.Column(db.String(100), nullable=False)
    price_tour = db.Column(db.Integer, nullable=False)
    date_tour = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Price %r>' % self.id


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_country = db.Column(db.String(100), nullable=False)
    country_language = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Country %r>' % self.id


class Settlement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_settlement = db.Column(db.String(100), nullable=False)
    settlement_code = db.Column(db.Integer, nullable=False)
    tours = db.relationship('Tour', backref = 'name_settlement', lazy = 'dynamic')

    def __repr__(self):
        return '<Settlement %r>' % self.id


class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_tour = db.Column(db.String(100), nullable=False)
    duration  = db.Column(db.Integer, nullable=False)
    title_settlement = db.Column(db.String(100), db.ForeignKey('settlement.title_settlement'), nullable=False)
    hotel_availability = db.Column(db.String(20), nullable=False)
    title_hostel = db.Column(db.String(100), db.ForeignKey('hotel.title'), nullable=True)
    mode_vehicle = db.Column(db.String(100), nullable=False)
    point_shipping = db.Column(db.String(100), nullable=False)
    price_lists = db.relationship('Price', backref = 'aidi', lazy = 'dynamic')

    def __repr__(self):
        return '<Tour %r>' % self.id


@app.route('/the_tour')
def the_tour():
    tour = Tour.query.order_by(Tour.id.desc()).all()
    return render_template("the_tour.html", tour =tour)


@app.route('/the_tour/<int:id>/update', methods=['POST', 'GET'])
def tour_update(id):
    tour = Tour.query.get(id)
    if request.method == "POST":
        tour.type_tour = request.form['type_tour']
        tour.duration = request.form['duration']
        tour.title_settlement = request.form['title_settlement']
        tour.hotel_availability = request.form['hotel_availability']
        tour.title_hostel = request.form['title_hostel']
        tour.mode_vehicle = request.form['mode_vehicle']
        tour.point_shipping = request.form['point_shipping']

        try:
            db.session.commit()
            return redirect('/the_tour')
        except:
            return "При радактировании тура произошла ошибка"
    else:
        return render_template("обновление_тура.html", tour=tour)


@app.route('/the_tour/<int:id>')
def tour_detail(id):
    tour = Tour.query.get(id)
    return render_template("tour_detail.html", tour=tour)


@app.route('/the_tour/<int:id>/del')
def tour_delete(id):
    tour = Tour.query.get_or_404(id)

    try:
        db.session.delete(tour)
        db.session.commit()
        return redirect('/the_tour')
    except:
        return "При удалении тура произошла ошибка"


@app.route('/создание_тура', methods=['GET', 'POST'])
def tour_create():
    if request.method == "POST":
        type_tour = request.form['type_tour']
        duration = request.form['duration']
        title_settlement = request.form['title_settlement']
        hotel_availability = request.form['hotel_availability']
        title_hostel = request.form['title_hostel']
        mode_vehicle = request.form['mode_vehicle']
        point_shipping = request.form['point_shipping']

        tour = Tour(type_tour=type_tour, duration=duration,title_settlement=title_settlement,
                              hotel_availability=hotel_availability, title_hostel=title_hostel,
                              mode_vehicle=mode_vehicle, point_shipping=point_shipping)

        try:
            db.session.add(tour)
            db.session.commit()
            return redirect('/the_tour')
        except:
            return "При добавлении тура произошла ошибка"
    else:
        return render_template("создание_тура.html")


@app.route('/settlement')
def settlement():
    township = Settlement.query.order_by(Settlement.id.desc()).all()
    return render_template("settlement.html", township =township)


@app.route('/settlement/<int:id>/update', methods=['POST', 'GET'])
def settlement_update(id):
    township = Settlement.query.get(id)
    if request.method == "POST":
        township.title_settlement = request.form['title_settlement']
        township.settlement_code = request.form['settlement_code']

        try:
            db.session.commit()
            return redirect('/settlement')
        except:
            return "При радактировании населенного пункта произошла ошибка"
    else:
        return render_template("обновление_населенного_пункта.html", township=township)


@app.route('/создание_населенный пункта', methods=['GET', 'POST'])
def settlement_create():
    if request.method == "POST":
        title_settlement = request.form['title_settlement']
        settlement_code = request.form['settlement_code']

        township = Settlement(title_settlement=title_settlement, settlement_code=settlement_code)

        try:
            db.session.add(township)
            db.session.commit()
            return redirect('/settlement')
        except:
            return "При добавлении населенного пункта произошла ошибка"
    else:
        return render_template("создание_населенный пункта.html")


@app.route('/settlement/<int:id>/del')
def settlement_delete(id):
    township = Settlement.query.get_or_404(id)

    try:
        db.session.delete(township)
        db.session.commit()
        return redirect('/settlement')
    except:
        return "При удалении населенного пункта произошла ошибка"


@app.route('/settlement/<int:id>')
def settlement_detail(id):
    township = Settlement.query.get(id)
    return render_template("settlement_detail.html", township=township)


@app.route('/country')
def country():
    land = Country.query.order_by(Country.id.desc()).all()
    return render_template("country.html", land =land)


@app.route('/country/<int:id>/del')
def country_delete(id):
    land = Country.query.get_or_404(id)

    try:
        db.session.delete(land)
        db.session.commit()
        return redirect('/country')
    except:
        return "При удалении страны произошла ошибка"


@app.route('/country/<int:id>/update', methods=['POST', 'GET'])
def country_update(id):
    land = Country.query.get(id)
    if request.method == "POST":
        land.title_country = request.form['title_country']
        land.country_language = request.form['country_language']

        try:
            db.session.commit()
            return redirect('/country')
        except:
            return "При радактировании страны произошла ошибка"
    else:
        return render_template("обновление_страны.html", land=land)


@app.route('/создание_страны', methods=['GET', 'POST'])
def country_create():
    if request.method == "POST":
        title_country = request.form['title_country']
        country_language = request.form['country_language']

        land = Country(title_country=title_country, country_language=country_language)

        try:
            db.session.add(land)
            db.session.commit()
            return redirect('/country')
        except:
            return "При добавлении страны произошла ошибка"
    else:
        return render_template("создание_страны.html")


@app.route('/country/<int:id>')
def country_detail(id):
    land = Country.query.get(id)
    return render_template("country_detail.html", land=land)


@app.route('/price_list')
def price_list():
    price = Price.query.order_by(Price.date_tour.desc()).all()
    return render_template("price_list.html", price=price)


@app.route('/price_list/<int:id>')
def price_list_detail(id):
    price = Price.query.get(id)
    return render_template("price_list_detail.html", price=price)


@app.route('/price_list/<int:id>/del')
def price_list_delete(id):
    price = Price.query.get_or_404(id)

    try:
        db.session.delete(price)
        db.session.commit()
        return redirect('/price_list')
    except:
        return "При удалении прайс-листа произошла ошибка"


@app.route('/price_list/<int:id>/update', methods=['POST', 'GET'])
def price_list_update(id):
    price = Price.query.get(id)
    if request.method == "POST":
        price.id_tour = request.form['id_tour']
        price.title_hostel = request.form['title_hostel']
        price.price_tour = request.form['price_tour']
        price.date_tour = request.form['date_tour']

        try:
            db.session.commit()
            return redirect('/price_list')
        except:
            return "При радактировании прайс-листа произошла ошибка"
    else:
        return render_template("обновление_прайс_листов.html", price=price)


@app.route('/создание_прайс_листов', methods=['GET', 'POST'])
def price_list_create():
    if request.method == "POST":
        id_tour = request.form['id_tour']
        title_hostel = request.form['title_hostel']
        price_tour = request.form['price_tour']
        date_tour = request.form['date_tour']

        price = Price(id_tour=id_tour, title_hostel=title_hostel, price_tour=price_tour, date_tour=date_tour)

        try:
            db.session.add(price)
            db.session.commit()
            return redirect('/price_list')
        except:
            return "При добавлении прайс-листа произошла ошибка"
    else:
        return render_template("создание_прайс_листов.html")


@app.route('/posts')
def posts():
    hotels = Hotel.query.order_by(Hotel.id.desc()).all()
    return render_template("posts.html", hotels=hotels)


@app.route('/posts/<int:id>')
def post_detail(id):
    hotel = Hotel.query.get(id)
    return render_template("post_detail.html", hotel=hotel)


@app.route('/posts/<int:id>/del')
def post_delete(id):
    hotel = Hotel.query.get_or_404(id)

    try:
        db.session.delete(hotel)
        db.session.commit()
        return redirect('/posts')
    except:
        return "При удалении Гостиницы произошла ошибка"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def hotels_update(id):
    hotel = Hotel.query.get(id)
    if request.method == "POST":
        hotel.Star = request.form['Star']
        hotel.title = request.form['title']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "При радактировании Гостиницы произошла ошибка"
    else:
        return render_template("hotels_update.html", hotel=hotel)


@app.route('/создание_Гостиниц', methods=['GET', 'POST'])
def hotels():
    if request.method == "POST":
        Star = request.form['Star']
        title = request.form['title']

        hotel = Hotel(Star=Star, title=title)

        try:
            db.session.add(hotel)
            db.session.commit()
            return redirect('/posts')
        except:
            return "При добавлении Гостиницы произошла ошибка"
    else:
        return render_template("создание_Гостиниц.html")


if __name__ == "__main__":
    app.run(debug=True)