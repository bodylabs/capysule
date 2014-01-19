from .client import Client
client = Client()

from .resources import parties
Person = parties.Person
Persons = parties.Persons(client)
Parties = parties.Parties(client)

from .resources import history
HistoryItem = history.HistoryItem
History = history.History(client)
