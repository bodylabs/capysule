import json
from booby import Model, fields
from wren.collection import Collection

class Person(Model):
    id = fields.Integer(primary=True)
    title = fields.String()
    first_name = fields.String(source='firstName')
    last_name = fields.String(source='lastName')
    job_title = fields.String(source='jobTitle')
    about = fields.String()
    created_on = fields.String(source='createdOn', read_only=True)
    updated_on = fields.String(source='updatedOn', read_only=True)

    def __repr__(self):
        name_parts = [ s for s in self.first_name, self.last_name if s is not None ]
        return 'Person({})'.format(' '.join(name_parts))


class Persons(Collection):
    '''
    For writing person objects.

    '''
    model = Person
    url = '/api/person'

    def serialize(self, obj):
        return {'person': dict(obj)}

class Parties(Collection):
    '''
    For reading person and organization objects.

    '''
    model = Person
    url = '/api/party'

    def __init__(self, *args, **kwargs):
        super(Parties, self).__init__(*args, **kwargs)
        self.persons = Persons(*args, **kwargs)

    def deserialize(self, response, data, many=False):
        if many:
            person_or_persons = data['parties']['person']
            if isinstance(person_or_persons, list):
                return super(Parties, self).deserialize(response, person_or_persons, many=True)
            else:
                return [super(Parties, self).deserialize(response, person_or_persons, many=False)]
        else:
            person = data['person']
            return super(Parties, self).deserialize(response, person, many)

    def add(self, obj):
        if isinstance(obj, Person):
            self.persons.add(obj)
        else:
            raise TypeError('Expected a Person object')
