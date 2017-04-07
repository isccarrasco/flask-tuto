from project import database

class Person(database.Model):
    person_id = database.Column(database.Integer, primary_key=True, unique=True)
    name = database.Column(database.String)
    address = database.Column(database.String)
    birth_day = database.Column(database.DateTime)
