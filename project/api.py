from flask_restful import Resource, reqparse, fields, marshal
from flask import request

from project import ws_api
from models import Person

person_fields = {
    'person_id': fields.Integer,
    'name': fields.String,
    'address': fields.String
}


class PersonsList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser(bundle_errors=True)
        self.reqparse.add_argument('person_id', type=int, required=True,
                                   help='Debe indicar la clave de la persona.', location=['form', 'json'])
        super(PersonsList, self).__init__()

    def get(self):
        persons = Person.query.all()
        return {'persons': map(lambda p: marshal(p, person_fields), persons)}

    def post(self):
        args = self.reqparse.parse_args()

        person_id = request.json['person_id']
        person = Person.query.filter_by(person_id=person_id).first()

        return {'person': marshal(person, person_fields)}

    def put(self):
        return {'data': False}

ws_api.add_resource(PersonsList, '/personsList')
