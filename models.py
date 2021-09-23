from peewee import *

db = SqliteDatabase('data.db')


class List(Model):
    Name = CharField()
    Fio = CharField()
    Vts = CharField()
    City = CharField()
    Kab = CharField()

    class Meta:
        database = db
