__version__ = '0.1.1'

from .client import Client
try:
    client = Client()
except KeyError:
    pass

from .resources import parties
Person = parties.Person
Persons = parties.Persons(client)
Parties = parties.Parties(client)

from .resources import history
HistoryItem = history.HistoryItem
History = history.History(client)

from .resources import cases
Case = cases.Case
Cases = cases.Cases(client)
