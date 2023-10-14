from rest_framework.exceptions import ValidationError


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, field):
        link = 'youtube.com'
        val = dict(field).get(self.field)
        if link not in val:
            raise ValidationError('Please, write YouTube link')
