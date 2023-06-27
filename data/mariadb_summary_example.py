#!/bin/env python3
import sqlalchemy
dialect = 'mariadb'
dbapi = 'mariadbconnector'
url_object = sqlalchemy.URL.create(
    drivername='+'.join([dialect, dbapi]),
    username='mariadb-user',
    password='mariadb-pass',
    host='127.0.0.1',
    port=3306,
    database='mariadb-demo'
)
engine = sqlalchemy.create_engine(url_object)

from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase): pass
class Movie(Base):
    __tablename__ = 'movie'
    title = sqlalchemy.orm.mapped_column(sqlalchemy.String(length=255), primary_key=True)
    year = sqlalchemy.orm.mapped_column(sqlalchemy.Integer)
    score = sqlalchemy.orm.mapped_column(sqlalchemy.Float)
Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
movies = [
    Movie(title="P1nder", year=2023, score=6.9),
    Movie(title="Painsec", year=2022, score=7.1),
    Movie(title="Pv1", year=2021, score=9.6),
]
for movie in movies:
    session.add(movie)
session.commit()
from datetime import datetime
statement = sqlalchemy.select(Movie).where(Movie.year > (datetime.now().year - 2)).order_by(Movie.score.desc())
result = session.execute(statement)
for movie in result.scalars():
    print(f'{movie.title!r} is a {movie.score} scored recent movie')
