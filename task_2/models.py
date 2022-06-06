from run import BaseModel
from peewee import *

class User(BaseModel):
    user_id = AutoField(column_name='UserId')
    name = TextField(column_name='Name', null=True)
    email = TextField(column_name='Email', null=True)

    class Meta:
        table_name = 'Users'


class Subject(BaseModel):
    subject_id = AutoField(column_name='UserId')
    name = TextField(column_name='Name', null=True)

    class Meta:
        table_name = 'Subjects'


class Result(BaseModel):
    result_id = AutoField(column_name='ResultId')
    result = IntegerField(column_name='Result', null=True)
    email = TextField(column_name='Email', null=True)
    user_id = ForeignKeyField(User, related_name='name_result', null=True)
    subject_id = ForeignKeyField(Subject, related_name='subject_result', null=True)

    class Meta:
        table_name = 'Results'

