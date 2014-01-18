from booby import Model, fields
from wren.collection import Collection


class Person(Model):        
    class Contacts(Model):
        class Address(Model):
            type = fields.String()
            street = fields.String()
            city = fields.String()
            state = fields.String()
            zip = fields.String()
            country = fields.String()

        class Email(Model):
            type = fields.String()
            email_address = fields.String(source='emailAddress')

        class Phone(Model):
            type = fields.String()
            phone_number = fields.String(source='phoneNumber')

        class Website(Model):
            type = fields.String()
            web_service = fields.String(source='webService',
                choices='URL SKYPE TWITTER FACEBOOK LINKED_IN XING FEED GOOGLE_PLUS FLICKR GITHUB YOUTUBE'.split(' ')
            )
            web_address = fields.String(source='webAddress')

        address = fields.Embedded(Address)
        email = fields.Embedded(Email)
        phone = fields.Embedded(Phone)
        website = fields.Embedded(Website)

    id = fields.Integer(primary=True)
    title = fields.String()
    first_name = fields.String(source='firstName')
    last_name = fields.String(source='lastName')
    job_title = fields.String(source='jobTitle')
    organisation_name = fields.String(source='organisationName')
    contacts = fields.Embedded(Contacts)
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
