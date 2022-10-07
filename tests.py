from app.models import *
from app import db

#
# u = User.query.all()
#
# for x in u:
#     db.session.delete(x)
# db.session.commit()


# u = User.query.filter_by(id=1).first()
# u.set_admin()
# db.session.commit()
# print(u)
# for uzers in u:
#     print(uzers.id, uzers.email, uzers.admin)

# info = UserInformation(phone='0766666666', country='Romania', city='Constanta', address="Ceva alee", id_user=1)
# db.session.add(info)
# db.session.commit()

# u_info = UserInformation.query.filter_by(id_user=1).first()
# print(u_info.phone, u_info.country, u_info.city, u_info.address, u_info.id_user)
#
# u_info = UserInformation.query.filter_by(id_user=1).all()
# print(u_info)
# for x in u_info:
#     print(x)

# u = User.query.filter_by(id=1).delete()
# print(u)
# db.session.commit()
# x = Category()
# f = x.add_category(category="Pants")
# print(f)
# z = Category.add_category(x, "T-Shirt")
# print(z)
# p = Product.query.first()
# print(p)
# p.brand.append(Brand.query.first())
# p.category.append(Category.query.first())
# c = Category.query.first()
# print(c)
# b = Brand.query.first()
# print(b)
# db.session.commit()
# nike_tshirt = Product(name='T-shirt Nike unisex', desc='Bumbac t-shirt nike for everybody', price=60
#                       , quantity=300)
# db.session.add(nike_tshirt)
# db.session.commit()
# tshirt = Category(name='T-Shirt')
# db.session.add(tshirt)
# db.session.commit()
# nike = Brand(name='Nike')
# db.session.add(nike)
# db.session.commit()
# u = User(name='garry',username='garry',email='garry@yahoo.com',password='1234')
# db.session.add(u)
# db.session.commit()
#
# from datetime import datetime
# import calendar
# current_date = '08 05 2015'
# day = datetime.strptime(current_date, '%m %d %Y').weekday()
# print(calendar.day_name[day])


# while True:
#     try:
#         t = int(input())
#         if not (1 <= t <= 1000):
#             raise ValueError  # this will send it to the print message and back to the input option
#         break
#     except ValueError:
#         print("Invalid integer.")
#
# for i in range(0, t):
#     while True:
#         try:
#             a, b, c = map(int, input().split())
#             if not (1 <= a <= 1000) or not (1 <= b <= 1000) or not (1 <= c <= 1000):
#                 raise ValueError  # this will send it to the print message and back to the input option
#             if a + b + c == 0 or -a + b + c == 0 or a - b + c == 0 or a + b - c == 0 or -a - b + c == 0 or a - b - c == 0 \
#                     or - a - b - c == 0:
#                 print('yes')
#             else:
#                 print('no')
#             break
#         except ValueError:
#             print("Invalid integer.")
