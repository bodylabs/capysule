import unittest
from nose.plugins.attrib import attr

class TestParties(unittest.TestCase):

    # def setUp(self):
    #     import logging
    #     logger = logging.getLogger('dj_capysule')
    #     logger.addHandler(logging.StreamHandler())
    #     logger.setLevel(logging.DEBUG)

    def test_that_person_decodes(self):
        sample_person = '''
        {
          "parties": {
            "@size": "1",
            "person": {
              "id": "55809173",
              "contacts": {
                "address": {
                  "id": "107608500",
                  "street": "Bag End, The Shire",
                  "city": "New York",
                  "state": "NY",
                  "zip": "10003",
                  "country": "United States"
                },
                "email": {
                  "id": "107608498",
                  "type": "Work",
                  "emailAddress": "frodo@shire.com"
                },
                "phone": {
                  "id": "107608497",
                  "type": "Mobile",
                  "phoneNumber": "7185551212"
                },
                "website": {
                  "id": "107608499",
                  "webAddress": "http://facebook.com/frodo",
                  "webService": "FACEBOOK",
                  "url": "http://facebook.com/frodo"
                }
              },
              "pictureURL": "https://d365sd3k9yw37.cloudfront.net/a/1391523488/theme/default/images/person_avatar_70.png",
              "createdOn": "2014-02-10T00:37:23Z",
              "updatedOn": "2014-02-10T00:37:23Z",
              "title": "Mr",
              "firstName": "Frodo",
              "lastName": "Baggins",
              "organisationId": "55809172",
              "organisationName": "Shire"
            }
          }
        }
        '''
        import capysule, json
        from capysule.resources import parties

        result = capysule.Parties.decode(json.loads(sample_person), many=True)
        self.assertIsInstance(result, list)
        self.assertEquals(len(result), 1)

        person = result[0]
        self.assertEquals(person.id, '55809173')
        self.assertEquals(person.first_name, 'Frodo')
        self.assertEquals(person.last_name, 'Baggins')
        self.assertEquals(person.title, 'Mr')
        self.assertEquals(person.organisation_name, 'Shire')
        self.assertIsInstance(person.contacts, parties.Person.Contacts)

        address = person.contacts.address
        self.assertIsInstance(address, parties.Person.Contacts.Address)
        self.assertEquals(address.street, 'Bag End, The Shire')
        self.assertEquals(address.city, 'New York')
        self.assertEquals(address.state, 'NY')
        self.assertEquals(address.zip, '10003')
        self.assertEquals(address.country, 'United States')

        email = person.contacts.email
        self.assertIsInstance(email, parties.Person.Contacts.Email)
        self.assertEquals(email.type, 'Work')
        self.assertEquals(email.email_address, 'frodo@shire.com')

    @attr('integration')
    def test_create_and_read_person(self):
        import capysule
        
        new_person = capysule.Person(first_name='Bilbo', last_name='Baggins')
        new_person.set_email_address('bilbo@shire.com')
        capysule.Parties.add(new_person)
        self.assertIsInstance(new_person.id, basestring)
        self.assertGreater(len(new_person.id), 0)

        fetched_person = capysule.Parties.get(new_person.id)
        self.assertEquals(fetched_person.first_name, 'Bilbo')
        self.assertEquals(fetched_person.last_name, 'Baggins')
        self.assertEquals(fetched_person.contacts.email.email_address, 'bilbo@shire.com')

    @attr('integration')
    def test_read_nonexistent_person(self):
        import capysule, uuid
        from ...collection import NotFound

        with self.assertRaises(NotFound) as ctx:
            capysule.Parties.get(str(uuid.uuid4()))
