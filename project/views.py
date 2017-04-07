from project import application
from project import database
from models import Person

@application.route('/')
@application.route('/index')
def index():
    return "Hello, World!"

@application.route('/home')
def home():
    data = Person.query.all()
    text = ''
    for person in data:
        text = person.name + "<br />"
    return "You are in home <br>" + text
