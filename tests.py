from app.models import User
from app import db

u = User.query.first()
print(u.id)
u.set_admin()
print(u.admin)

# u = User.query.all()
# print(u)
# for uzers in u:
#     print(uzers.id , uzers.email, uzers.admin)
# u = User.query.filter_by(id=1).delete()
# print(u)
# db.session.commit()

# u = User(name='garry',username='garry',email='garry@yahoo.com',password='1234')
# db.session.add(u)
# db.session.commit()
