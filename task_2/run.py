from peewee import *
from .models import *

conn = SqliteDatabase('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

class BaseModel(Model):
    class Meta:
        database = conn  

User.create(name='1-Qwerty')

conn.close()