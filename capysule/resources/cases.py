from booby import Model, fields
from ..collection import Collection


class Case(Model):
    id = fields.Integer(primary=True)
    status = fields.String(choices=['OPEN', 'CLOSED'])
    name = fields.String(required=True)
    description = fields.String()
    owner = fields.String()
    close_date = fields.String(name='closeDate')

    created_on = fields.String(name='createdOn', read_only=True)
    updated_on = fields.String(name='updatedOn', read_only=True)

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
    url = '/api/kase'

    def encode(self, obj):
        return {'kase': super(Cases, self).encode(obj)}

    def decode(self, data, many=False):
        if data.get('kases') and data['kases'].get('@size') == '0':
            return [] if many else None
        if many:
            obj_or_list = data['kases']['kase']
            if isinstance(obj_or_list, list):
                return super(Cases, self).decode(obj_or_list, many=True)
            else:
                return [super(Cases, self).decode(obj_or_list, many=False)]
        else:
            obj = data['kase']
            return super(Cases, self).decode(obj, many=False)

