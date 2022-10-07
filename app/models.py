from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

category_product = db.Table(
    'category_product',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)

brand_product = db.Table(
    'brand_product',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
    db.Column('brand_id', db.Integer, db.ForeignKey('brand.id'))
)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    profile = db.Column(db.String(120), default='/static/profile_pic.jpg')
    admin = db.Column(db.Boolean, default=False)
    user_info = db.relationship('UserInformation', backref='user')

    def __repr__(self):
        return '<ID - {} ,name - {}, username - {}, email - {}, admin - {} '.format(self.id,
                                                                                    self.name,
                                                                                    self.username,
                                                                                    self.email,
                                                                                    self.admin)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_admin(self):
        self.admin = True

    def check_admin(self):
        return self.admin


class UserInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True)
    country = db.Column(db.String(20), unique=False)
    city = db.Column(db.String(30), unique=False)
    address = db.Column(db.String(255), unique=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    desc = db.Column(db.String(500), unique=False, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.relationship("Category", secondary=category_product)
    brand = db.relationship("Brand", secondary=brand_product)

    def __repr__(self):
        return '<ID - {} ,Product_name - {}, desc - {}, price - {}, quantity - {}, category - {}, brand - {}' \
            .format(self.id, self.name, self.desc, self.price, self.quantity, self.category, self.brand)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<ID - {} ,Category_name - {}'.format(self.id, self.name)

    def add_category(self, category: str):
        search = "%{}%".format(category)
        qry = Category.query.filter(Category.name.like(search)).first()
        print(qry)
        if qry is not None:
            print("Exista deja!!")
        else:
            try:
                db.session.add(Category(name=category))
                db.session.commit()
                print("Succes!")
            except ConnectionError:
                print("Connection error!")


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<ID - {} ,Brand_name - {}'.format(self.id, self.name)
