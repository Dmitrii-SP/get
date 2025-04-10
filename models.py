from peewee import *

db = SqliteDatabase('my.db')


class PC(Model):
    code = IntegerField(primary_key=True)
    model = CharField()
    speed = SmallIntegerField()
    ram = SmallIntegerField()
    hd = FloatField()
    cd = CharField()
    price = DecimalField()

    class Meta:
        database = db
        db_table = 'PC'