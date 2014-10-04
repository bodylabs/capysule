from booby import Model, fields
from ..collection import Collection


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
            email_address = fields.String(name='emailAddress')

        class Phone(Model):
            type = fields.String()
            phone_number = fields.String(name='phoneNumber')

        class Website(Model):
            type = fields.String()
            web_service = fields.String(name='webService',
                choices='URL SKYPE TWITTER FACEBOOK LINKED_IN XING FEED GOOGLE_PLUS FLICKR GITHUB YOUTUBE'.split()
            )
            web_address = fields.String(name='webAddress')

        address = fields.Embedded(Address)
        email = fields.Embedded(Email)
        phone = fields.Embedded(Phone)
        website = fields.Embedded(Website)

    id = fields.Integer(primary=True)
    title = fields.String()
    first_name = fields.String(name='firstName')
    last_name = fields.String(name='lastName')
    job_title = fields.String(name='jobTitle')
    organisation_name = fields.String(name='organisationName')
    contacts = fields.Embedded(Contacts)
    about = fields.String()

    created_on = fields.String(name='createdOn', read_only=True)
    updated_on = fields.String(name='updatedOn', read_only=True)

    def set_email_address(self, email_address):
        '''
        Convenience method sets email address.

        This just modifies the instance. It's the caller's
        responsibility to persist the change by re-adding
        the object.

        '''
        if self.contacts is None:
            self.contacts = self.Contacts()
        if self.contacts.email is None:
            self.contacts.email = self.Contacts.Email()
        self.contacts.email.email_address = email_address

    def __repr__(self):
        name_parts = [ s for s in self.first_name, self.last_name if s is not None ]
        return 'Person({})'.format(' '.join(name_parts))


class Persons(Collection):
    '''
    For writing person objects.

    '''
    model = Person
    url = '/api/person'

    def encode(self, obj):
        return {'person': super(Persons, self).encode(obj)}


class Parties(Collection):
    '''
    For reading person and organization objects.

    '''
    model = Person
    url = '/api/party'

    def __init__(self, *args, **kwargs):
        super(Parties, self).__init__(*args, **kwargs)
        self.persons = Persons(*args, **kwargs)

    def decode(self, data, many=False):
        if data.get('parties') and data['parties'].get('@size') == '0':
            return [] if many else None
        if many:
            obj_or_list = data['parties']['person']
            if isinstance(obj_or_list, list):
                return super(Parties, self).decode(obj_or_list, many=True)
            else:
                return [super(Parties, self).decode(obj_or_list, many=False)]
        else:
            obj = data['person']
            return super(Parties, self).decode(obj, many=False)

    def add(self, obj):
        if isinstance(obj, Person):
            self.persons.add(obj)
        else:
            raise TypeError('Expected a Person object')
