from booby import Model, fields
from wren.collection import Collection


class Case(Model):
    id = fields.Integer(primary=True)
    status = fields.String(choices=['OPEN', 'CLOSED'])
    name = fields.String(required=True)
    description = fields.String()
    owner = fields.String()
    close_date = fields.String(source='closeDate')

    created_on = fields.String(source='createdOn', read_only=True)
    updated_on = fields.String(source='updatedOn', read_only=True)

    party = None

    @property
    def _url(self):
        if getattr(self, '_persisted', False) is True:
            return '/api/kase/%s' % self.id
        if not self.party:
            raise ValidationError('Party is required')
        return '/api/party/%s/kase' % self.party.id


class Cases(Collection):
    model = Case
    url = None

    def serialize(self, obj):
        return {'kase': dict(obj)}
