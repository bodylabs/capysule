from .client import Client
client = Client()

from .resources import Persons as _Persons
from .resources import Parties as _Parties
Persons = _Persons(client)
Parties = _Parties(client)

from .resources import Person
