import json
from booby import Model, fields
from wren.collection import Collection

class Person(Model):
    id = fields.Integer()
    first_name = fields.String(source='firstName')
    last_name = fields.String(source='lastName')
    created_on = fields.String(source='createdOn')
    updated_on = fields.String(source='updatedOn')

    def __repr__(self):
        name_parts = [ s for s in self.first_name, self.last_name if s is not None ]
        return 'Person({})'.format(' '.join(name_parts))


class Parties(Collection):
    model = Person

    @property
    def url(self):
        return '/api/party'

    def deserialize(self, response, data, many=False):
        if many:
            persons = data['parties']['person']
            return super(Parties, self).deserialize(response, persons, many)
        else:
            person = data['person']
            return super(Parties, self).deserialize(response, person, many)
