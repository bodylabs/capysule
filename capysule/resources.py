import json
from booby import Model, fields
from wren.collection import Collection

class Person(Model):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    created_on = fields.String()
    updated_on = fields.String()

    def parse(self, response):
        return parse_party(response.json())

    def __repr__(self):
        return 'Person({} {})'.format(self.first_name, self.last_name)


class Parties(Collection):
    model = Person

    @property
    def url(self):
        return '/api/party'

    def parse(self, response):
        parties = response.json()['parties']
        return [parse_party(r) for r in parties['person']]


def parse_party(raw):
    mapping = {
        'id': 'id',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'created_on': 'createdOn',
        'updated_on': 'updatedOn',
    }
    return { k: raw[mapping[k]] for k in mapping if mapping[k] in raw }
