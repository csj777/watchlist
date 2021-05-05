from app import User, Movie, db

user = User(name='csj')
m1 = Movie(title='Lemo',year='1996')
m2 = Movie(title='Mahjong', year='1996')
db.session